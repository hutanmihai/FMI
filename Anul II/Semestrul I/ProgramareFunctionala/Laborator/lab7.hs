-- 1. Expresii si Arbori
-- Se dau următoarele tipuri de date reprezentând expresii si arbori de expresii:

data Expr = Const Int -- integer constant
          | Expr :+: Expr -- addition
          | Expr :*: Expr -- multiplication
           deriving Eq

data Operation = Add | Mult deriving (Eq, Show)

data Tree = Lf Int -- leaf
          | Node Operation Tree Tree -- branch
           deriving (Eq, Show)

-- 1.1. Să se instantieze clasa Show pentru tipul de date Expr,
-- astfel încât să se afiseze mai simplu expresiile
instance Show Expr where
  show (Const a) = show a
  show (b :+: a) = "(" ++ show b ++ " + " ++ show a ++ ")"
  show (b :*: a) = "(" ++ show b ++ " * " ++ show a ++ ")"

-- 1.2. Să se scrie o functie evalExp :: Expr -> Int care evaluează o expresie
-- determinând valoarea acesteia
evalExp :: Expr -> Int
evalExp (Const a) = a
evalExp (b :+: a) = evalExp a + evalExp b
evalExp (b :*: a) = evalExp a * evalExp b

-- Exemplu:
exp1 = ((Const 2 :*: Const 3) :+: (Const 0 :*: Const 5))
exp2 = (Const 2 :*: (Const 3 :+: Const 4))
exp3 = (Const 4 :+: (Const 3 :*: Const 3))
exp4 = (((Const 1 :*: Const 2) :*: (Const 3 :+: Const 1)) :*: Const 2)
test11 = evalExp exp1 == 6
test12 = evalExp exp2 == 14
test13 = evalExp exp3 == 13
test14 = evalExp exp4 == 16


-- 1.3. Să se scrie o functie evalArb :: Tree -> Int care evaluează o expresie modelată
-- sub formă de arbore, determinând valoarea acesteia.
evalArb :: Tree -> Int
evalArb (Lf a) = a
evalArb (Node Add a b) = evalArb a + evalArb b
evalArb (Node Mult a b) = evalArb a * evalArb b


arb1 = Node Add (Node Mult (Lf 2) (Lf 3)) (Node Mult (Lf 0)(Lf 5))
arb2 = Node Mult (Lf 2) (Node Add (Lf 3)(Lf 4))
arb3 = Node Add (Lf 4) (Node Mult (Lf 3)(Lf 3))
arb4 = Node Mult (Node Mult (Node Mult (Lf 1) (Lf 2)) (Node Add (Lf 3)(Lf 1))) (Lf 2)

test21 = evalArb arb1 == 6
test22 = evalArb arb2 == 14
test23 = evalArb arb3 == 13
test24 = evalArb arb4 == 16

-- 1.4. Să se scrie o functie expToArb :: Expr -> Tree care
-- transformă o expresie în arborele corespunzător
expToArb :: Expr -> Tree
expToArb (Const a) = Lf a
expToArb (a :+: b) = Node Add (expToArb a) (expToArb b)
expToArb (a :*: b) = Node Mult (expToArb a) (expToArb b)

-- 2. Clasa Collection
-- In acest exercitiu vom exersa manipularea listelor si tipurilor de date prin
-- implementarea catorva colectii de tip tabela asociativa cheie-valoare.
-- Aceste colectii vor trebui sa aiba urmatoarele facilitati
-- • crearea unei colectii vide
-- • crearea unei colectii cu un element
-- • adaugarea/actualizarea unui element intr-o colectie
-- • cautarea unui element intr-o colectie
-- • stergerea (marcarea ca sters a) unui element dintr-o colectie
-- • obtinerea listei cheilor
-- • obtinerea listei valorilor
-- • obtinerea listei elementelor

-- 2.1. Adaugati definitii implicite (in functie de functiile celelalte) pentru
-- a. keys
-- b. values
-- c. fromList

class Collection c where
      empty :: c key value
      singleton :: key -> value -> c key value
      insert
            :: Ord key
            => key -> value -> c key value -> c key value
      lookup :: Ord key => key -> c key value -> Maybe value
      delete :: Ord key => key -> c key value -> c key value
      keys :: c key value -> [key]
      keys c = [x | (x,i) <- toList(c)]
      values :: c key value -> [value]
      values c = [i | (x,i) <- toList(c)]
      toList :: c key value -> [(key, value)]
      fromList :: Ord key => [(key,value)] -> c key value
      fromList [] = empty
      fromList ((k,v):t) = insert k v (fromList t)


-- 2.2. Fie tipul listelor de perechi de forma cheie-valoare:
newtype PairList k v
  = PairList { getPairList :: [(k, v)] }

-- Faceti PairList instanta a clasei Collection.
instance Collection PairList  where
  empty = PairList []
  singleton k v = PairList [(k,v)]
  insert k v (PairList l) = PairList ((k,v): filter (\(x,y) -> x /= k) l)
  clookup k (PairList l) = lookup k l
  delete k (PairList l) = PairList (filter (\(x,y) -> x /= k) l)
  toList (PairList l) = l

-- 2.3. Fie tipul arborilor binari de cautare (ne-echilibrati):
data SearchTree key value
  = Empty
  | BNode
      (SearchTree key value) -- elemente cu cheia mai mica
      key                    -- cheia elementului
      (Maybe value)          -- valoarea elementului
      (SearchTree key value) -- elemente cu cheia mai mare

-- Observati ca tipul valorilor este Maybe value. Acest lucru se face pentru a reduce timpul
-- operatiei de stergere prin simpla marcare a unui nod ca fiind sters. 
-- Un nod sters va avea valoarea Nothing.
-- Faceti SearchTree instanta a clasei Collection.
instance Collection SearchTree where
  empty = Empty
  singleton k v = BNode Empty k (Just v) Empty
  insert k v Empty = singleton k v
  insert k v (BNode t1 k1 mv1 t2)
    | k == k1 = BNode t1 k1 (Just v) t2
    | k < k1  = BNode (insert k v t1) k1 mv1 t2
    | otherwise = BNode t1 k1 mv1 (insert k v t2)
  delete k (BNode t1 k1 mv1 t2)
    | k == k1 = BNode t1 k1 Nothing t2
    | k < k1  = BNode (delete k t1) k1 mv1 t2
    | otherwise = BNode t1 k1 mv1 (delete k t2)
  clookup k Empty = Nothing
  clookup k (BNode t1 k1 mv1 t2)
    | k == k1   = mv1
    | k < k1    = clookup k t1
    | otherwise = clookup k t2
  toList Empty = []
  toList (BNode t1 k1 mv1 t2) = toList t1 ++ embed k1 mv1 ++ toList t2
      where
        embed k1 Nothing = []
        embed k1 (Just a) = [(k1,a)]
