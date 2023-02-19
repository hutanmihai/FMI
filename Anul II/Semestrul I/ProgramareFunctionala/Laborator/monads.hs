data Maybe2 a = Just2 a | Nothing2 deriving Show

instance Functor Maybe2 where
    fmap f Nothing2 = Nothing2
    fmap f (Just2 j) = Just2 (f j)

instance Applicative Maybe2 where
    pure = Just2
    Just2 f <*> j = fmap f j
    Nothing2 <*> n = Nothing2

instance Monad Maybe2 where
    Nothing2 >>= f = Nothing2
    Just2 j >>= f = f j


data Tree a = Tip a | Branch (Tree a) (Tree a) deriving Show

instance Functor Tree where
    fmap f (Tip a) = Tip (f a)
    fmap f (Branch left right) = Branch (fmap f left) (fmap f right)

instance Applicative Tree where
    pure = Tip
    Tip f <*> t = fmap f t
    Branch left right f <*> t = Branch (left <*> t) (right <*> t)

instance Monad Tree where
    Tip a >>= f = f a
    Branch left right >>= f = Branch (left >>= f) (right >>= f)
