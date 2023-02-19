--EX1
--Să se scrie o functie poly2 care are patru argumente de tip Double, a,b,c,x si calculează a*xˆ2+b*x+c. Scrieti si signatura functiei (poly :: ceva)
poly2 :: Double -> Double -> Double -> Double -> Double
poly2 a b c x = a*x*x+b*x+c

--EX2
--Să se scrie o functie eeny care întoarce “eeny” pentru input par si “meeny” pentru input impar. Hint: puteti folosi functia even
eeny :: Integer -> String
eeny x =
        if even x
            then "eeny"
            else "yeeny"

--EX3
{--
Să se scrie o functie fizzbuzz care întoarce “Fizz” pentru numerele divizibile cu 3, “Buzz” pentru
numerele divizibile cu 5 si “FizzBuzz” pentru numerele divizibile cu ambele. Pentru orice alt număr se
întoarce sirul vid. Pentru a calcula modulo a două numere puteti folosi functia mod. Să se scrie această
functie în 2 moduri: folosind if si folosind gărzi (conditii)
--}
fizzbuzz :: Integer -> String
fizzbuzz x
        | mod x 5 == 0 && mod x 3 == 0 =  "FizzBuzz"
        | mod x 5 == 0 = "Buzz"
        | mod x 3 == 0 = "Fizz"
        | otherwise = ""

--Recursivitate
fibonacciCazuri :: Integer -> Integer
fibonacciCazuri n
            | n < 2 = n
            | otherwise = fibonacciCazuri (n - 1) + fibonacciCazuri (n - 2)

fibonacciEcuational :: Integer -> Integer
fibonacciEcuational 0 = 0
fibonacciEcuational 1 = 1
fibonacciEcuational n =
            fibonacciEcuational (n - 1) + fibonacciEcuational (n - 2)


--EX4
--Numerele tribonacci
tribonacci :: Integer -> Integer
tribonacci x
        | x == 1 = 1
        | x < 4 = x - 1
        | otherwise = tribonacci (x-1) + tribonacci (x-2) + tribonacci (x-3)

--EX5
{--
Să se scrie o functie care calculează coeficientii binomiali, folosind recursivitate.
Acestia sunt determinati folosind urmatoarele ecuatii:
 B(n,k) = B(n-1,k) + B(n-1,k-1)
 B(n,0) = 1
 B(0,k) = 0
--}
binomial :: Integer -> Integer -> Integer
binomial n k
        | k == 0 = 1
        | n == 0 = 0
        | otherwise = binomial (n-1) k + binomial (n-1)  (k-1)

-- binomial n 0 = 1
-- binomial 0 k = 0
-- binomial n k = binomial (n-1) k + binomial (n-1) (k-1)


--Liste

--EX6 Să se implementeze următoarele functii folosind liste:
--a) verifL - verifică dacă lungimea unei liste date ca parametru este pară
verifL :: [Int] -> Bool
verifL x
        | even (length x) = True
        | otherwise = False

{--
b) takefinal - pentru o listă dată ca parametru si un număr n, întoarce lista cu ultimele n elemente.
Dacă lista are mai putin de n elemente, se intoarce lista nemodificată
--}
takefinal :: [Int] -> Int -> [Int]
takefinal x n 
        | length x < n = x
        | otherwise = drop (length x - n) x

--Cum trebuie să modificăm prototipul functiei pentru a putea fi folosită si pentru siruri de caractere?

{--
c) remove - pentru o listă si un număr n se întoarce lista din care se sterge elementul de pe pozitia n.
(Hint: puteti folosi functiile take si drop). Scrieti si prototipul functiei.
--}
remove :: [Int] -> Int -> [Int]
remove x n
        | length x < n = x
        | otherwise = concat[take (n-1) x, takefinal x (length x - n)]


--Recursivitate pe Liste
-- semiPareRec [0,2,1,7,8,56,17,18] == [0,1,4,28,9]
semiPareRec :: [Int] -> [Int]
semiPareRec [] = []
semiPareRec (h:t)
            | even h = h `div` 2 : t'
            | otherwise = t'
            where t' = semiPareRec t

--EX7 Să se scrie urmatoarele functii folosind recursivitate:
-- a) myreplicate - pentru un întreg n si o valoare v întoarce lista de lungime n ce are doar elemente egale cu v. Să se scrie si prototipul functiei.
myreplicate :: Int -> Int -> [Int]
myreplicate 0 v = []
myreplicate n v = v:myreplicate (n-1) v

--b) sumImp - pentru o listă de numere întregi, calculează suma valorilor impare. Să se scrie si prototipul functiei.
sumImp :: [Int] -> Int
sumImp [] = 0
sumImp (x:xs) = 
        if even x
            then sumImp xs
            else x + sumImp xs

--c) totalLen - pentru o listă de siruri de caractere, calculează suma lungimilor sirurilor care încep cu caracterul ‘A’.
totalLen :: [String] -> Int
totalLen [] = 0
totalLen (x:xs) =
        if head x == 'A'
            then length x+ totalLen xs
            else totalLen xs
