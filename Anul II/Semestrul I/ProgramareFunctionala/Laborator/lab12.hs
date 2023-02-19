import Data.Monoid

-- Exercitii pentru Foldable

-- 1. Implementati următoarele functii folosind foldMap si/sau foldr din clasa Foldable,
-- apoi testati-le cu mai multe tipuri care au instantă pentru Foldable

elem1 :: (Foldable t, Eq a) => a -> t a -> Bool
elem1 a = foldr (\a' acc -> a'== a || acc) False

null1 :: (Foldable t) => t a -> Bool
null1 = foldr (\_ _-> False) True

length1 :: (Foldable t) => t a -> Int
length1 = foldr (\_ l -> l + 1) 0 

toList1 :: (Foldable t) => t a -> [a]
toList1 = foldr (\h t -> h:t) []  

-- fold combină elementele unei structuri folosind structura de monoid a acestora.

fold1 :: (Foldable t, Monoid m) => t m -> m
fold1 = foldMap id

-- 2. Scrieti instante ale lui Foldable pentru următoarele tipuri,
-- implementand functia foldMap
data Constant a b = Constant b

instance Foldable (Constant a) where
    foldMap f (Constant b) = f b

data Two a b = Two a b

instance Foldable (Two a) where
    foldMap f (Two a b) = (f b)

data Three a b c = Three a b c

instance Foldable (Three a b) where
    foldMap f (Three a b c) = (f c)

data Three' a b = Three' a b b

instance Foldable (Three' a) where
    foldMap f (Three' a b c) = (f c)

data Four' a b = Four' a b b b

instance Foldable (Four' a) where
    foldMap f (Four' a b c d) = (f b) `mappend` (f c) `mappend` (f d)

data GoatLord a = NoGoat | OneGoat a | MoreGoats (GoatLord a) (GoatLord a) (GoatLord a)

instance Foldable GoatLord where
    foldMap f NoGoat = mempty
    foldMap f (OneGoat a) = f a
    foldMap f (MoreGoats a b c) = (foldMap f a) `mappend` (foldMap f b) `mappend` (foldMap f c)
