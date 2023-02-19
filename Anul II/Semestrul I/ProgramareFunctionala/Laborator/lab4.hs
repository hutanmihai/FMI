-- import GHC.Types (Nat)

{-
[ x^2 |x <- [1..10], x `rem` 3 == 2] = [4,25,64]
[(x,y)| x<- [1..5], y <- [x..(x+2)]] = [(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(4,5),(4,6),(5,5),(5,6),(5,7)]
[(x,y)| x<-[1..3], let k = x^2, y <- [1..k]] = [(1,1),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9)]
[ x | x<- "Facultatea de Matematica si Informatica", elem x ['A'..'Z']] = "FMI"
[[x..y]| x <- [1..5], y <- [1..5], x < y] = [[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[2,3],[2,3,4],[2,3,4,5],[3,4],[3,4,5],[4,5]]
-}

--EX1
--Folosind numai metoda prin selectie definiti o functie
--astfel încât factori n întoarce lista divizorilor pozitivi ai lui n.
factori :: Int -> [Int]
factori n = [ x | x <- [1..n], rem n x == 0]

--EX2
--Folosind functia factori, definiti predicatul prim n care întoarce True dacă si numai dacă n este număr prim.
prim :: Int -> Bool
prim n = length (factori n) == 2

--EX3
--Folosind numai metoda prin selectie si functiile definite anterior,
--definiti functia astfel încât numerePrime n întoarce lista numerelor prime din intervalul [2..n].
numerePrime :: Int -> [Int]
numerePrime n = [ x | x <- [2..n], prim x ]

--EX4
--Definiti functia myzip3 care se comportă asemenea lui zip dar are trei argumente:
myzip3 :: [a] -> [a] -> [a] -> [(a,a,a)]
myzip3 x y z = [(a, b, c) | ((a, b), c) <- zip (zip x y) z]

--EX5
--Scrieti o functie generică firstEl care are ca argument o listă de perechi
-- de tip (a,b) si întoarce lista primelor elementelor din fiecare pereche
firstEl :: [(a, b)] -> [a]
firstEl = map fst

--EX6
-- Scrieti functia sumList care are ca argument o listă de liste de valori Int
-- si întoarce lista sumelor elementelor din fiecare listă (suma elementelor
-- unei liste de întregi se calculează cu functia sum)
sumList :: [[Int]] -> [Int]
sumList = map sum

--EX7
-- Scrieti o functie prel2 care are ca argument o listă de Int si întoarce o listă
-- în care elementele pare sunt înjumătătite, iar cele impare sunt dublate:
prel2 :: [Int] -> [Int]
prel2 = map (\x -> if odd x then 2*x else div x 2)

--EX8
-- Scrieti o functie care primeste ca argument un caracter si o listă de siruri,
-- rezultatul fiind lista sirurilor care contin caracterul respectiv (folositi functia elem)
functie :: Char -> [String] -> [String]
functie x = filter (elem x)

--EX9
--Scrieti o functie care primeste ca argument o listă de întregi si întoarce lista pătratelor numerelor impare.
functie2 :: [Int] -> [Int]
functie2 = map (\x -> if odd x then x^2 else x)

--EX10
--Scrieti o functie care primeste ca argument o listă de întregi si întoarce lista pătratelor
--numerelor din pozitii impare. Pentru a avea acces la pozitia elementelor folositi zip.
functie3 :: [Int] -> [Int]
functie3 l = map (\(a,b) -> a * a) (filter (odd . snd) (zip l [1..length l]))

--EX11
-- Scrieti o functie care primeste ca argument o listă de siruri de caractere
-- si întoarce lista obtinută prin eliminarea consoanelor din fiecare sir.
charToString :: Char -> String
charToString c = [c]

aux :: String -> String
aux "" = ""
aux (h:t) =
    if xs `elem` "aeiouAEIOU"
        then charToString h ++ aux t
        else aux t
numaiVocale :: [String] -> [String]
numaiVocale lista = map (aux) lista

--EX12
-- Definiti recursiv functiile mymap si myfilter cu aceeasi functionalitate ca si
-- functiile predefinite
mymap :: (a -> b) -> [a] -> [b]
mymap fct [] = []
mymap fct (x:xs) = fct x : mymap fct xs

myfilter :: (a -> Bool) -> [a] -> [a]
myfilter fct [] = []
myfilter fct (x:xs) =
    if fct x
        then x : myfilter fct xs
        else myfilter fct xs
