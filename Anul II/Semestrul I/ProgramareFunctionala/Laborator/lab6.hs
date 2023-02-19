
-- EX1
-- Vom începe prin a scrie câteva functii definite folosind tipul de date Fruct:
data Fruct
            = Mar String Bool
            | Portocala String Int

-- O expresie de tipul Fruct este fie un Mar String Bool sau o Portocala String Int. Vom
-- folosi un String pentru a indica soiul de mere sau portocale, un Bool pentru a indica
-- dacă mărul are viermi si un Int pentru a exprima numărul de felii dintr-o portocală.

-- De exemplu:
-- ionatanFaraVierme = Mar "Ionatan" False
-- goldenCuVierme = Mar "Golden Delicious" True
-- portocalaSicilia10 = Portocala "Sanguinello" 10
-- listaFructe = [Mar "Ionatan" False,
--                         Portocala "Sanguinello" 10,
--                         Portocala "Valencia" 22,
--                         Mar "Golden Delicious" True,
--                         Portocala "Sanguinello" 15,
--                         Portocala "Moro" 12,
--                         Portocala "Tarocco" 3,
--                         Portocala "Moro" 12,
--                         Portocala "Valencia" 2,
--                         Mar "Golden Delicious" False,
--                         Mar "Golden" False,
--                         Mar "Golden" True]

-- a) Scrieti o functie ePortocalaDeSicilia care indică dacă un fruct 
-- este o portocală de Sicilia sau nu. Soiurile de portocale din
-- Sicilia sunt Tarocco, Moro si Sanguinello
ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Mar _ _ ) = False
ePortocalaDeSicilia (Portocala soi felii)
        | soi == "Tarocco" || soi == "Moro" || soi == "Sanguinello" = True
        | otherwise = False

-- test_ePortocalaDeSicilia1 =
--          ePortocalaDeSicilia (Portocala "Moro" 12) == True
-- test_ePortocalaDeSicilia2 =
--          ePortocalaDeSicilia (Mar "Ionatan" True) == False

-- b) Scrieti o functie nrFeliiSicilia care calculează numărul total de felii
--  ale portocalelor de Sicilia dintr-o listă de fructe
nrFeliiPortocala :: Fruct -> Int
nrFeliiPortocala (Portocala _ felii) = felii

nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia [] = 0
nrFeliiSicilia (h:t)
        | ePortocalaDeSicilia h == True = nrFeliiPortocala h + nrFeliiSicilia t
        | otherwise = 0 + nrFeliiSicilia t

-- test_nrFeliiSicilia = nrFeliiSicilia listaFructe == 52

-- c) Screti o functie nrMereViermi care calculează numărul de mere
--  care au viermi dintr-o lista de fructe
nrMarViermi :: Fruct -> Int
nrMarViermi (Mar _ viermi) = if viermi == True then 1 else 0

eMar :: Fruct -> Bool
eMar (Portocala _  _) = False
eMar (Mar _  _) = True

nrMereViermi :: [Fruct] -> Int
nrMereViermi [] = 0
nrMereViermi (h:t)
        | eMar h == True = nrMarViermi h + nrMereViermi t
        | otherwise = nrMereViermi t

-- test_nrMereViermi = nrMereViermi listaFructe == 2

-- SAU !!!
-- nrMereViermi :: [Fruct] -> Int
-- nrMereViermi [] = 0
-- nrMereViermi ((Portocala _ _) : l) = nrMereViermi l
-- nrMereViermi ((Mar soi vierme) : l)
--     | vierme == True = 1 + nrMereViermi(l)
--     | otherwise = 0 + nrMereViermi(l)

-- nrMereViermi1 :: [Fruct] -> Int
-- nrMereViermi1 list = length [ b | Mar s b <- list , b ]

-- EX2
type NumeA = String
type Rasa = String
data Animal = Pisica NumeA | Caine NumeA Rasa
            deriving Show

-- a) Scrieti o functie care întoarce "Meow!" pentru pisică si "Woof!" pentru câine
vorbeste :: Animal -> String
vorbeste (Pisica _) = "Meow!"
vorbeste (Caine _  _) = "Woof!"

-- b) Va reamintiti de tipul de date predefinit Maybe:
-- data Maybe a = Nothing | Just a
-- Scrieti o functie care întoarce rasa unui câine dat ca parametru
-- sau Nothing dacă parametrul este o pisică
rasa :: Animal -> Maybe String
rasa (Pisica _) = Nothing
rasa (Caine _ rasa) = Just rasa

-- EX3
-- Se dau urmatoarele tipuri de date ce reprezintă matrici cu linii de lungimi diferite:
data Linie = L [Int]
        deriving Show
data Matrice = M [Linie]
        deriving Show

-- a) Scrieti o functie care verifica daca suma elementelor de pe fiecare linie
-- este egala cu o valoare n. Rezolvati cerinta folosind foldr
verifica :: Matrice -> Int -> Bool
verifica (M m) n = foldr( \(L line) result -> result && (foldr (+) 0 line) == n) True m

verifica1 :: Matrice -> Int -> Bool 
verifica1 (M m) n = foldr (\result curent -> result && curent) True  (map (\(L line) -> sum line == n) m)

-- test_veri1 = verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10 == False
-- test_verif2 = verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25 == True


-- b) Scrieti o functie doarPozN care are ca parametru un element de tip Matrice si un
-- numar intreg n, si care verifica daca toate liniile de lungime n din matrice au
-- numai elemente strict pozitive
verif :: Linie -> Int -> Bool 
verif (L line) n =
    if length line == n
        then length (filter (>0) line) == n
        else True 

doarPozN :: Matrice -> Int -> Bool
doarPozN (M m) n = foldr( \(L line) result -> result && verif (L line) n) True m

-- testPoz1 = doarPozN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 == True
-- testPoz2 = doarPozN (M [L[1,2,-3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 == False

-- c) Definiti predicatul corect care verifică dacă toate liniile dintr-o matrice
-- au aceeasi lungime
corect :: Matrice -> Bool
corect (M []) = True 
corect (M [x]) = True
corect (M (x:y:lines)) = 
    if (length first) == (length second)
        then True && corect (M (y:lines))
        else False 
    where 
        first = (\(L x) -> x) x
        second = (\(L y) -> y) y

-- testcorect1 = corect (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) == False
-- testcorect2 = corect (M[L[1,2,3], L[4,5,8], L[3,6,8], L[8,5,3]]) == True
