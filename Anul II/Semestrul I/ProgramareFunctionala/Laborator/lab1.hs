import Data.List

myInt = 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555

double :: Integer -> Integer
double x = x+x

triple :: Integer -> Integer
triple x = x*3


--maxim :: Integer -> Integer -> Integer
maxim x y = 
        if (x > y)
            then x
            else y

maxim3 x y z = let u = maxim x y in (maxim  u z)

-- maxim3 x y z =
--         let
--             u = maxim x y
--         in
--             maxim u z

--EX6
-- Să se scrie următoarele functii:
--a) functie cu 2 parametri care calculeaza suma pătratelor celor două numere
squares_sum :: Integer -> Integer -> Integer
squares_sum x y = x^2 + y^2


--b) functie cu un parametru ce întoarce mesajul “par” dacă parametrul este par si “impar” altfel
even_or_odd :: Integer -> String
even_or_odd x =
            if mod x 2 == 0
                then "par"
                else "impar"

--c) functie care calculează factorialul unui număr
factorial :: Integer -> Integer
factorial 0 = 1
factorial x = x * factorial(x-1)
--sau factorial x = product[1..x]

--d) functie care verifică dacă primul parametru este mai mare decât dublul celui de-al doilea parametru
verify :: Integer -> Integer -> Bool
verify x y = x > y*2
