-- foldr op unit [a1, a2, a3, ... , an] =
-- a1 `op`(a2 `op`(a3 `op`.. `op`(an `op`unit)))
-- foldr :: (a -> b -> b) -> b -> [a] -> b
-- foldr op i [] = i
-- foldr op i (x:xs) = x `op`(foldr op i xs)
-- foldl op unit [a1, a2, a3, ... , an] =
-- ((((unit `op`a1) `op`a2) `op`a3) `op`..) `op`an
-- foldl :: (b -> a -> b) -> b -> [a] -> b
-- foldl op i [] = i
-- foldl op i (x:xs) = foldl op (i `op`x) xs
-- ghci> foldr (+) 0 [1..5]
-- 15
-- ghci> foldr (*) 1 [2,3,4]
-- 24
-- ghci> foldr (++) [] ["abc","def","ghi"]
-- "abcdefghi"
-- ghci> foldl (++) "first" ["abc","def","ghi"]
-- "firstabcdefghi"
-- ghci> foldr (++) "last" ["abc","def","ghi"]
-- "abcdefghilast"


-- EX1
-- Calculati suma pătratelor elementelor impare dintr-o listă dată ca parametru
squareSum :: [Int] -> Int
squareSum list = foldr (+) 0 (map (^2) (filter odd list))

-- EX2
-- Scrieti o functie care verifică faptul că toate elementele dintr-o listă sunt True, folosind foldr
areAllTrue :: [Bool] -> Bool
areAllTrue list = foldr (&&) True list

-- EX3
-- Scrieti o functie care verifică dacă toate elementele 
-- dintr-o listă de numere întregi satisfac o proprietate dată ca parametru
allVerifies :: (Int -> Bool) -> [Int] -> Bool
allVerifies param list = foldr (&&) True (map param list)

-- EX4
-- Scrieti o functie care verifică dacă există elemente într-o listă de numere
-- întregi care satisfac o proprietate dată ca parametru
anyVerifies :: (Int -> Bool) -> [Int] -> Bool
anyVerifies param list = foldr (||) False (map param list)

-- EX5
-- Redefiniti functiile map si filter folosind foldr.
-- Le puteti numi mapFoldr si filterFoldr.
mapFoldr :: (a -> b) -> [a] -> [b]
mapFoldr f list = foldr (\x acc -> (f x) : acc) [] list

filterFoldr :: (a -> Bool) -> [a] -> [a]
filterFoldr f list = foldr (\x acc -> if (f x) == True then x:acc else acc) [] list

-- EX6
-- Folosind functia foldl, definiti functia listToInt care transformă o lista de
-- cifre (un număr foarte mare stocat sub formă de listă) în numărul intreg
-- asociat. Se presupune ca lista de intrare este dată corect.
listToInt :: [Int] -> Int
listToInt list = foldl (\x acc -> x * 10 + acc) 0 list

-- EX7
-- a) Scrieti o functie care elimină un caracter din sir de caractere
rmChar :: Char -> String -> String
rmChar ch cuv =  filter (/= ch) cuv

-- b) Scrieti o functie recursivă care elimină toate caracterele din al doilea
-- argument care se găsesc în primul argument, folosind rmChar
rmCharsRec :: String -> String -> String
rmCharsRec [] b = b
rmCharsRec a [] = []
rmCharsRec (h:t) b =
    if h `elem` b
        then rmCharsRec t (rmChar h b)
        else rmCharsRec t b

-- c) Scrieti o functie echivalentă cu cea de la b) care foloseste
-- rmChar si foldr în locul recursiei
rmCharsFold :: String -> String -> String
rmCharsFold a b = foldr rmChar b a
