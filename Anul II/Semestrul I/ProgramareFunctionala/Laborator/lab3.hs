{-# OPTIONS_GHC -Wno-deferred-out-of-scope-variables #-}
import GHC.Float (divideDouble)
import Data.List
import Data.Char

--EX1
--Sa se scrie o functie nrVocale care pentru o lista de siruri de caractere, calculeaza numarul total de vocale ce apar 
--în cuvintele palindrom. Pentru a verifica daca un sir e palindrom,puteti folosi functia reverse, iar pentru a cauta un element într-o lista puteti 
--folosi functia elem. Puteti defini oricâte functii auxiliare.
numarVocaleCuvant :: String -> Int
numarVocaleCuvant [] = 0
numarVocaleCuvant (x:xs) =
        if elem x "aeiouAEIOU"
            then 1 + numarVocaleCuvant xs
            else numarVocaleCuvant xs

nrVocale :: [String] -> Int
nrVocale [] = 0
nrVocale (x:xs) =
        if x == reverse x
            then numarVocaleCuvant x + nrVocale xs
            else nrVocale xs

--EX2
--Sa se scrie o functie care primeste ca parametru un numar 
--si o lista de întregi si adauga elementul dat dupa fiecare 
--element par din lista.
--  Sa se scrie si prototipul functiei.
functie :: Int -> [Int] -> [Int]
functie _ [] = []
functie n (h:t) =
    if even h
        then [h] ++ [n] ++ functie n t
        else [h] ++ functie n t

--Liste definite prin comprehensiune sau selectie
semiPareComp :: [Int] -> [Int]
semiPareComp l = [ x `div`2 | x <- l, even x ]

--EX3
--Sa se scrie o functie care are ca parametru un numar întreg  si determina lista de divizori ai  
--acestui numar. Sa se scrie s i prototipul functiei.

divizori :: Int -> [Int]
divizori n = [ x | x <-[1..n], n `mod` x == 0]

--EX4
--Sa se scrie o functie care are ca parametru o lista de numere întregi 
-- si calculeaza lista listelor  de divizori.
listadiv :: [Int] -> [[Int]]
listadiv [] = [[]]
listadiv ls = [ divizori x | x <- ls]

--EX5
--Scrieti o functie care date fiind limita inferioara si cea superioara (întregi) 
--a unui interval  ̆închis si o lista de numere întregi, calculeaza lista numerelor
-- din lista care apartin intervalului.
--a) doar recursie
inIntervalRec :: Int -> Int -> [Int] -> [Int]
inIntervalRec x y (h:t) = 
    if x <= h && h <= y
        then h : inIntervalRec x y t
        else inIntervalRec x y t

--b) descrieri de liste
inIntervalComp :: Int ->  Int -> [Int] -> [Int]
inIntervalComp x y ls = [ i | i <- ls, i <= y && x <= i]

--EX6
--Scrieti o functie care numara câte numere strict pozitive sunt într-o lista data
--  ca argument.
--a) recursiv
pozitiveRec :: [Int] -> Int
pozitiveRec [] = 0
pozitiveRec (h:t) = 
    if  h > 0
        then 1 + pozitiveRec t
        else pozitiveRec t

--b) descrieri de liste
pozitiveComp :: [Int] -> Int
pozitiveComp [] = 0
pozitiveComp ls = length [ x | x <- ls, x > 0]

--EX7
--Scrieti o functie care data fiind o lista de numere calculeaza lista pozitiilor
-- elementelor impare din lista originala.

--a) recursiv -> pozitiiImpareRec
pozitii :: [Int] -> Int -> [Int]
pozitii [] poz = []
pozitii (h:t) poz  = 
        if odd h
            then poz : pozitii t (poz+1)
            else pozitii t (poz + 1)

pozitiiImpareRec :: [Int] -> [Int]
pozitiiImpareRec l = pozitii l 0

--b) descrieri de liste -> pozitiiImpareComp
pozitiiImpareComp :: [Int] -> [Int]
pozitiiImpareComp ls = [ i | (i, x) <- zip [0..] ls, odd x]

--EX8
--Scrieti o functie care calculeaza produsul tuturor cifrelor care apar în  sirul 
--de caractere dat ca intrare. Daca nu sunt cifre în sir, raspunsul functiei trebuie sa fie 1.

--a)Folositi doar recursie. Denumiti functia multDigitsRec
multDigitsRec :: String -> Int 
multDigitsRec "" = 1
multDigitsRec (h:t) =
        if isDigit h
            then digitToInt h * multDigitsRec t
            else multDigitsRec t

--b)Folositi descrieri de liste.. Denumiti functia multDigitsComp
multDigitsComp :: String -> Int
multDigitsComp "" = 1
multDigitsComp cuv = product [digitToInt i | i <- cuv, isDigit i]
