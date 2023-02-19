-- Amintiti-vă clasele Functor si Applicative, rulati si analizati următoarele exemple.

{- 
class Functor f where 
     fmap :: (a -> b) -> f a -> f b 
class Functor f => Applicative f where
    pure :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b

Just length <*> Just "world"

Just (++" world") <*> Just "hello,"
pure (+) <*> Just 3 <*> Just 5
pure (+) <*> Just 3 <*> Nothing
(++) <$> ["ha","heh"] <*> ["?","!"]
-}

-- Exercitii

-- 1. Se dă tipul de date
data List a = Nil
            | Cons a (List a)
        deriving (Eq, Show)

-- Să se scrie instante Functor si Applicative pentru tipul de date List.
instance Functor List where
    fmap f Nil = Nil
    fmap f (Cons a b) = Cons (f a) (fmap f b)

applicative :: List a -> List a -> List a
applicative Nil Nil = Nil
applicative Nil b = b
applicative (Cons a c) b = Cons a (applicative c b)

instance Applicative List where
    pure a = Cons a Nil
    (<*>) Nil _ = Nil
    (<*>) _ Nil = Nil
    (<>) (Cons a b) c = applicative (fmap a c) (b <> c) 

-- Exemple
f = Cons (+1) (Cons (*2) Nil)
v = Cons 1 (Cons 2 Nil)
test1 = (f <*> v) == Cons 2 (Cons 3 (Cons 2 (Cons 4 Nil)))

-- 2. Se dă tipul de date
data Cow = Cow {
        name :: String
        , age :: Int
        , weight :: Int
        } deriving (Eq, Show)

-- a) Să se scrie functiile noEmpty, respectiv noNegative care valideaza
-- un string, respectiv un intreg
noEmpty :: String -> Maybe String
noEmpty "" = Nothing
noEmpty a = Just a

noNegative :: Int -> Maybe Int
noNegative a
    | a < 0     = Nothing
    | otherwise = Just a

test21 = noEmpty "abc" == Just "abc"
test22 = noNegative (-5) == Nothing 
test23 = noNegative 5 == Just 5 

-- b) Sa se scrie o functie care construieste un element de tip Cow
-- verificând numele, varsta si greutatea cu functiile de la a).
cowFromString :: String -> Int -> Int -> Maybe Cow
cowFromString nume varsta greutate
    | noEmpty nume == Nothing       = Nothing
    | noNegative varsta == Nothing  = Nothing
    | noNegative greutate == Nothing= Nothing
    | otherwise                     = Just (Cow nume varsta greutate)

test24 = cowFromString "Milka" 5 100 == Just (Cow {name = "Milka", age = 5, weight = 100})

-- 3. Se dau următoarele tipuri de date:
newtype Name = Name String deriving (Eq, Show)
newtype Address = Address String deriving (Eq, Show)

data Person = Person Name Address
    deriving (Eq, Show)

-- a) Să se implementeze o functie validateLength care validează
-- lungimea unui sir (sa  fie mai mică decât numărul dat ca parametru).
validateLength :: Int -> String -> Maybe String
validateLength a b
    | length b < a      = Just b
    | otherwise          = Nothing

test31 = validateLength 5 "abc" == Just "abc"

-- b) Să se implementeze functiile mkName si mkAddress care transformă un sir de
-- caractere într-un element din tipul de date asociat, validând stringul cu functia
-- validateLength (numele trebuie sa aiba maxim 25 caractere iar adresa maxim 100)
mkName :: String -> Maybe Name
mkName a
    | validateLength 25 a == Nothing    = Nothing
    | otherwise                         = Just (Name a)

mkAddress :: String -> Maybe Address
mkAddress a
    | validateLength 100 a == Nothing    = Nothing
    | otherwise                         = Just (Address a)

test32 = mkName "Gigel" ==  Just (Name "Gigel")
test33 = mkAddress "Str Academiei" ==  Just (Address "Str Academiei")

-- c) Să se implementeze functia mkPerson care primeste ca argument două siruri de
-- caractere si formeaza un element de tip Person daca sunt validate conditiile,
-- folosind functiile implementate mai sus.
mkPerson :: String -> String -> Maybe Person
mkPerson a b
    | mkName a == Nothing     = Nothing
    | mkAddress b == Nothing  = Nothing
    | otherwise               = Just (Person (Name a) (Address b))

test34 = mkPerson "Gigel" "Str Academiei" == Just (Person (Name "Gigel") (Address "Str Academiei"))
