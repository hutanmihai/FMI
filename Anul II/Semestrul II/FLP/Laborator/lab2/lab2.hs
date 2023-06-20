import Control.Applicative
import Data.Char

newtype Parser a = Parser { apply :: String -> [(a, String)] }

satisfy :: (Char -> Bool) -> Parser Char
satisfy p = Parser go
  where
    go [] = []   -- imposibil de parsat șirul vid
    go (c:input)
      | p c = [(c, input)]   -- dacă predicatul ține, întoarce c și restul șirului de intrare
      | otherwise = []       -- în caz contrar, imposibil de parsat

--- | Acceptă orice caracter
anychar :: Parser Char
anychar = satisfy (const True)

--- | acceptă doar caracterul dat ca argument
char :: Char -> Parser Char
char  x = satisfy (== x)

--- | acceptă o cifră
digit :: Parser Char
digit = satisfy isDigit

--- | acceptă un spațiu (sau tab, sau sfârșit de linie -- vedeți funcția din Data.Char )
space :: Parser Char
space = satisfy isSpace

--- | succes doar dacă am șirul de intrare este vid 
endOfInput :: Parser ()
endOfInput  = Parser go
  where
    go "" = [((), "")]
    go _ = []

  -- --- / Definim un parser care accepta ca tokens numere de doua cifre
  -- parseCifra = digitToInt <$> digit
  -- douaCifre c1 c2 = 10 * c1 + c2

instance Functor Parser where
    fmap f pa = Parser (\input -> [(f a, rest) | (a, rest) <- apply pa input])

instance Applicative Parser where
    pure a = Parser (\input -> [(a, input)])
    pf <*> pa = Parser (\input -> [(f a, resta) | (f, restf) <- apply pf input, (a, resta) <- apply pa restf])

parse :: Parser a -> String -> Either String a
parse pa input = case apply pa input of
    -- [(a, input_ramas)] -> if apply (endOfInput) input_ramas == [] then Right a else parse pa input_ramas
    [(a, "")] -> Right a
    [] -> Left "Parse error"
    _ -> Left "Parse error"

instance Monad Parser where
    pa >>= k = Parser (\input -> [(b, restb) | (a, resta) <- apply pa input, (b, restb) <- apply (k a) resta])

cifParanteze :: Parser Int
cifParanteze = do
    char '('
    d <- digit
    char '('
    return (digitToInt d)

isSemn :: Char -> Bool
isSemn c = c == '+' || c == '-'

semn :: Parser Char
semn = satisfy isSemn

cifraSemn :: Parser Int
cifraSemn = do
    s <- semn
    d <- digit
    case s of
      '+' -> return (digitToInt d)
      '-' -> return (-1 * (digitToInt d))

cifSemn :: Parser Int
cifSemn = pure (\s d -> case s of
                            '+' -> digitToInt d
                            '-' -> -1 *(digitToInt d)) <*> semn <*> digit

string :: String -> Parser String
string "" = pure ""   -- cazul de bază: șirul vid este întotdeauna parsat cu succes și întoarce un șir vid
string (c:cs) = do    -- pentru fiecare caracter din șir
  _ <- satisfy (== c) -- aplicăm un parser care verifică dacă caracterul se potrivește
  rest <- string cs   -- și recursiv aplicăm parserul pe restul șirului
  pure (c:rest)       -- întoarcem șirul format din caracterul curent și restul


instance Alternative Parser where
    empty = Parser (const [])
    p <|> p' = Parser (\input -> apply p input ++ apply p' input)

digits :: Parser [Int]
digits = some (fmap digitToInt (satisfy isDigit))

naiveNatural :: Parser Int
naiveNatural = do
  digits <- digits
  pure (foldl (\acc d -> acc * 10 + d) 0 digits)

-- | Elimină zero sau mai multe apariții ale lui `space`
whiteSpace :: Parser ()
whiteSpace = do
    many space
    return ()

-- | parses a natural number (one or more digits)
digit2 :: Parser Int
digit2 = digitToInt <$> satisfy isDigit

nat :: Parser Int
nat = do
  digits <- some digit2
  pure (foldl (\acc d -> acc * 10 + d) 0 digits)

-- | aplică un parser, și elimină spațiile de după
lexeme :: Parser a -> Parser a
lexeme input = do
  x <- input
  whiteSpace
  return x

-- | parses a natural number (one or more digits)
natural :: Parser Int
natural = lexeme $ foldl (\acc d -> acc * 10 + digitToInt d) 0 <$> some (satisfy isDigit)

-- | Parses the string and skips whiteSpace after it
symbol :: String -> Parser String
symbol input = do
  x <- string input
  whiteSpace
  return x

-- | Parses the string, skips whiteSpace, returns unit
reserved :: String -> Parser ()
reserved input = do
  symbol input
  return ()

-- | parsează virgulă, eliminând spațiile de după
comma :: Parser ()
comma = do
  symbol ","
  return ()

-- | parsează argumentul intre paranteze rotunde
--   elimină spațiile de după paranteze
parens :: Parser a -> Parser a
parens input = do
  symbol "("
  x <- input
  symbol ")"
  return x

-- | parsează argumentul intre paranteze pătrate
--   elimină spațiile de după paranteze
brackets :: Parser a -> Parser a
brackets input = do
  symbol "["
  x <- input
  symbol "]"
  return x

-- | una sau mai multe instanțe, separate de virgulă
--   cu eliminarea spațiilor de după fiecare virgulă
--   intoarce lista obiectelor parsate
commaSep1 :: Parser a -> Parser [a]
commaSep1 input = do
  x <- input
  xs <- some (do
    comma
    input)
  return (x:xs)

-- | zero sau mai multe instanțe, separate de virgulă,
--   cu eliminarea spațiilor de după fiecare virgulă
--   intoarce lista obiectelor parsate
commaSep :: Parser a -> Parser [a]
commaSep input = commaSep1 input <|> pure []

-- | date fiind parsere pentru prima literă si pentru felul literelor următoare
--   scrieți un parser pentru un identificator
ident :: Parser Char -> Parser Char -> Parser String
ident is il = do
  x <- is
  xs <- many il
  return (x:xs)

-- | ca mai sus, dar elimină spatiile de după
identifier :: Parser Char -> Parser Char -> Parser String
identifier is il = lexeme (ident is il)
