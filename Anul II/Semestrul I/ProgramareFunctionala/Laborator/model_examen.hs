-- Subiectul 1 [ADT + Clase]  [2pct] 
 
-- Se dau următoarele: 
 
-- Un tip de date ce reprezinta puncte cu numar variabil de coordonate intregi: 
data Point = Pt [Int]  
        deriving Show 
 
-- Un tip de date ce reprezinta arbori binari de cautare (cu nodurile sortate): 
data Arb = Empty | Node Int Arb Arb 
        deriving Show 
 
-- O clasă de tipuri ToFromArb 
class ToFromArb a where 
        toArb :: a -> Arb  
        fromArb :: Arb -> a 
 
-- Sa se faca o instanta a clasei ToFromArb pentru tipul Point.
--  Inserarea in arbore se va face tinand 
-- cont de proprietatea arborelui de a fi sortat. 
instance ToFromArb Point where
        toArb (Pt []) = Empty
        toArb (Pt (h:t)) = Node h (toArb (Pt (filter (<h) t))) (toArb (Pt (filter (>=h) t)))
        fromArb Empty = Pt []
        fromArb (Node x Empty Empty) = Pt [x]
        fromArb (Node x st dr) = Pt (ask(fromArb st) ++ [x] ++ ask(fromArb dr))
                where
                        ask (Pt lista) = lista

--------------------------------------------------------------------------------------------------------------

-- Subiectul 2 [Liste + Monade] [3 pct] 
 
-- Sa se scrie o functie care primeste doua numere intregi si o lista de numere intregi si construieste din 
-- lista initiala, lista numerelor aflate in intervalul definit de cele doua numere. Sa se rezolve problema in 
-- doua moduri (o solutie fara monade si o solutie cu monade).  

-- Selectie
getFromInterval :: Int -> Int -> [Int] -> [Int]
getFromInterval x y list = [ n | n <- list, x<=n && n<=y ]

-- Monade
getFromIntervalMonad :: Int -> Int -> [Int] -> [Int]
getFromIntervalMonad x y list =
        do
                n <- list
                if x <= n && n <= y then return n else []
 
-- getFromInterval 5 7 [1..10] == [5,6,7]

--------------------------------------------------------------------------------------------------------------

-- Subiectul 3 [Monade] [1 pct] 
 
-- Se da tipul de date  
newtype ReaderWriter env a = RW {getRW :: env-> (a,String)} 
 
-- Sa se scrie instanta completa a clasei Monad pentru tipul ReaderWriter, astfel incat sa pastreze 
-- proprietatea de monada, env fiind o memorie nemodificabila si concatenand toate stringurile. Nu este 
-- nevoie sa faceti instante si pentru clasele Applicative si Functor.

instance Monad (ReaderWriter env) where
  return va = RW (\_ -> (va,""))
  ma >>= k = RW f 
      where f env = let (va, str1) = getRW ma env
                        (vb, str2)  = getRW (k va) env
                    in (vb, str1 ++ str2)

instance Applicative (ReaderWriter env) where
  pure = return
  mf <*> ma = do
    f <- mf
    va <- ma
    return (f va)       

instance Functor (ReaderWriter env) where              
  fmap f ma = pure f <*> ma
