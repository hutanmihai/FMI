module Parsing where

import Exp
import Lab2
import Control.Applicative (some, many, (<|>))
import Data.Char (isAlpha, isAlphaNum)

-- miniHaskellDef :: LanguageDef st
-- miniHaskellDef = undefined

-- miniHs :: TokenParser st
-- miniHs = makeTokenParser miniHaskellDef

parseFirst :: Parser a -> String -> Maybe a
parseFirst p s
  = case apply p s of
      [] -> Nothing
      (a,_):_ -> Just a

haskellId :: Parser String
haskellId = identifier (satisfy isAlpha) (satisfy isAlphaNum)

haskellOp :: Parser String
haskellOp = identifier isOp isOp
    where
        isOp = satisfy (\x -> elem x ":!#$%&*+./<=>?@\\^|-~")

var :: Parser Var
-- var = Var <$> haskellId
var = do
    x <- haskellId
    return $ Var x

varExp :: Parser ComplexExp
varExp = do
    x <- var
    return $ CX x

lambdaExp :: Parser ComplexExp
lambdaExp = do
    symbol "\\"
    x <- var
    symbol "->"
    e <- expr
    return $ CLam x e

letExp :: Parser ComplexExp
letExp = do
    symbol "let"
    x <- var
    symbol ":="
    e1 <- expr
    symbol "in"
    e2 <- expr
    return $ Let x e1 e2

letrecExp :: Parser ComplexExp
letrecExp = do
    symbol "letrec"
    x <- var
    symbol ":="
    e1 <- expr
    symbol "in"
    e2 <- expr
    return $ LetRec x e1 e2

------TEMA-------

{-
Pentru list folositi parser-ul din laboratorul 2
aveti brackets -> verifica sa aveti [, ] si un parser intre ele
parserul dintre paranteze trebuie sa fie un parser peste "," - commaSep,
deja definit
-}

listExp :: Parser ComplexExp
listExp = do
    symbol "["
    es <- commaSep1 expr
    symbol "]"
    return $ List es

natExp :: Parser ComplexExp
natExp = read <$> some (digit) >>= return . Nat

parenExp :: Parser ComplexExp
parenExp = do
    symbol "("
    e <- expr
    symbol ")"
    return e

basicExp :: Parser ComplexExp
basicExp = varExp <|> lambdaExp <|> letExp <|> letrecExp <|> listExp  <|> parenExp <|> natExp

expr :: Parser ComplexExp
expr = do
  exps <- some basicExp
  return $ foldl1 CApp exps

-- TODO
exprParser :: Parser ComplexExp
exprParser = do
  symbol "let"
  x <- var
  symbol ":="
  n <- natExp
  symbol "in"
  symbol "\\"
  y <- var
  symbol "->"
  exp <- expr
  return $ Let x n (CLam y exp)
