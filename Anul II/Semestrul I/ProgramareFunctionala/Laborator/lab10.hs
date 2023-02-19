import Data.Sequence (insertAt)
import Distribution.Simple (UserHooks(instHook))

-- Laboratorul 10 - Functor

{-
class Functor f where
fmap : : ( a -> b ) -> f a -> f b
-}

-- Scrieti instante ale clasei Functor pentru tipurile de date descrise mai jos

newtype Identity a = Identity a
                        deriving Show

instance Functor Identity where
    fmap f (Identity a) = Identity (f a)

data Pair a = Pair a a
    deriving Show

instance Functor Pair where
    fmap f (Pair x b) = Pair (f b) (f b)

data Constant a b = Constant b
    deriving Show

instance Functor (Constant a) where
    fmap f (Constant b) = Constant (f b)

data Two a b = Two a b
    deriving Show

instance Functor (Two a) where
    fmap f (Two a b) = Two a (f b)

data Three a b c = Three a b c
    deriving Show

instance Functor (Three a b) where
    fmap f (Three a b c) = Three a b (f c)

data Three' a b = Three' a b b
    deriving Show

instance Functor (Three' a) where
    fmap f (Three' a b c) = Three' a (f b) (f c)

data Four a b c d = Four a b c d
    deriving Show

instance Functor (Four a b c) where
    fmap f (Four a b c d) = Four a b c (f d)

data Four'' a b = Four'' a a a b
    deriving Show

instance Functor (Four'' a) where
    fmap f (Four'' a b c d) = Four'' a b c (f d)

data Quant a b = Finance | Desk a | Bloor b
    deriving Show

instance Functor (Quant a) where
    fmap f (Bloor b) = Bloor (f b)
    fmap f (Desk a) = Desk a
    fmap f Finance = Finance

data LiftItOut f a = LiftItOut (f a)
    deriving Show

instance Functor f => Functor (LiftItOut f) where
    fmap v (LiftItOut fa) = LiftItOut (fmap v fa)

data Parappa f g a = DaWrappa (f a) (g a)
    deriving Show

instance (Functor f,Functor g) =>Functor (Parappa f g) where
    fmap v (DaWrappa fa ga) = DaWrappa (fmap v fa) (fmap v ga)

data IgnoreOne f g a b = IgnoringSomething (f a) (g b)
    deriving Show

instance Functor g => Functor (IgnoreOne f g a) where
    fmap v (IgnoringSomething fa gb) = IgnoringSomething fa (fmap v gb)

data Notorious g o a t = Notorious (g o) (g a) (g t)
    deriving Show

instance Functor g => Functor (Notorious g o a) where
    fmap v (Notorious go ga gt) = Notorious go ga (fmap v gt)

data GoatLord a = NoGoat | OneGoat a | MoreGoats (GoatLord a) (GoatLord a) (GoatLord a)
    deriving Show

instance Functor GoatLord where
    fmap v NoGoat = NoGoat
    fmap v (OneGoat a) = OneGoat (v a)
    fmap v (MoreGoats fa fb fc) = MoreGoats (fmap v fa) (fmap v fb) (fmap v fc)

data TalkToMe a = Halt | Print String a | Read (String -> a)

instance Functor TalkToMe where
    fmap v Halt = Halt
    fmap v (Print c a) = Print c (v a)
    fmap v (Read f) = Read (v . f)