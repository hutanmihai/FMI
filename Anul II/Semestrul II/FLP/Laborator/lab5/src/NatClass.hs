module NatClass where

import Prelude (Show(..), (<>), Num(fromInteger), undefined, ($))
import qualified GHC.Natural as Natural

import MyPrelude
import BoolClass
import MaybeClass
 
-- | The class of Natural-like types (types having a notion of
-- 'zero', 'succ'essor, and 'iter'ation).
-- Instances should satisfy the following:
--
-- [Zero Iterations] @'iter' f i 'zero' = i@
-- [Successor Iterations]  @'iter' f i ('succ' n) = f ('iter' f i n)@
class NatClass n where
  zero :: n
  succ :: n -> n
  iter :: (a -> a) -> a -> n -> a

instance NatClass Natural.Natural where
  zero = 0
  succ n = n `Natural.plusNatural` 1
  iter f i 0 = i
  iter f i n = f (iter f i (n `Natural.minusNatural` 1))

one :: NatClass n => n
one = succ zero

-- >>> one :: Natural.Natural
-- 1

-- | The isZero function returns 'true' iff its argument is 'zero'.
isZero :: NatClass n => n -> CBool
isZero n = iter (const false) true n

-- >>> isZero (one :: Natural.Natural)
-- CFalse

-- | Usual natural numbers addition
add :: NatClass n => n -> n -> n
add n1 n2 = iter succ n1 n2

-- >>> add one one :: Natural.Natural
-- 2

-- | Usual natural numbers multiplication
mul :: NatClass n => n -> n -> n
mul n1 n2 = iter (add n1) zero n2

-- >>> mul one one :: Natural.Natural
-- 1

-- | Usual natural numbers exponentiation (@exp m n@ is @m ^ n@)
exp :: NatClass n => n -> n -> n
exp n1 n2 = iter (mul n1) one n2

-- >>> exp (add one one) (add one one) :: Natural.Natural
-- 4

-- | Predecessor of a natural number ('nothing' for 'zero')
pred :: NatClass n => n -> CMaybe n
pred n = iter (\m -> maybe (just zero) (just . succ) m) nothing n

-- >>> pred zero :: CMaybe Natural.Natural
-- CNothing

-- | Difference between natural numbers as a 'MaybeClass' ('nothing' if first is smaller)
sub :: NatClass n => n -> n -> CMaybe n
sub n1 n2 = iter (\m -> maybe nothing (pred) m) (just n1) n2


-- >>> sub (exp (add one one) (add one one)) one :: CMaybe Natural.Natural
-- CJust 3

-- | (Strictly-)Less-Than predicate for natural numbers.
lt :: NatClass n => n -> n -> CBool
lt n1 n2 = isNothing (sub n1 n2)

-- >>> lt (one :: Natural.Natural) one
-- CFalse

-- | (Strictly-)Greater-Than predicate for natural numbers.
gt :: NatClass n => n -> n -> CBool
gt n1 n2 = ite (isJust (sub n1 n2) && (lt n2 n1)) true false

-- >>> gt (one :: Natural.Natural) one
-- CFalse

-- | Greater-Than-or-Equal-To predicate for natural numbers.
gte :: NatClass n => n -> n -> CBool
gte n1 n2 = not (lt n1 n2)

-- >>> gte (zero :: Natural.Natural) zero
-- CTrue

-- | Less-Than-or-Equal-To predicate for natural numbers.
lte :: NatClass n => n -> n -> CBool
lte n1 n2 = not (gt n1 n2)
-- >>> lte (zero :: Natural.Natural) zero
-- CTrue

-- | Equality predicate for natural numbers.
eq :: NatClass n => n -> n -> CBool
eq n1 n2 = lte n1 n2 && gte n1 n2

-- >>> eq (zero :: Natural.Natural) zero
-- CTrue

-- >>> eq (zero :: Natural.Natural) one
-- CFalse

-- | Returns the greater between its two arguments
max :: NatClass n => n -> n -> n
max n1 n2 = ite (gte n1 n2) n1 n2

-- >>> max (zero :: Natural.Natural) one
-- 1

newtype CNat = CNat { getCNat :: forall a . (a -> a) -> a -> a }

instance NatClass CNat where
  iter f i n = getCNat n f i
  zero = CNat (\_ z -> z)
  succ n = CNat (\f x -> f (getCNat n f x))

-- | converting between different instances of 'NatClass'
fromNatClass :: (NatClass n, NatClass m) => n -> m
fromNatClass = iter succ zero

-- | 'Show' instance for 'CNat' (via transformation into Haskell Natural)
instance Show CNat where
  show cn = "C" <> show (fromNatClass cn :: Natural.Natural)

-- | to allow recognizing natural numbers as 'CNat'
instance Num CNat where
  fromInteger n = fromNatClass (fromInteger n :: Natural.Natural)

-- >>> 1 :: CNat
-- C1

-- >>> isZero (1 :: CNat)
-- CFalse

-- >>> add 3 5 :: CNat
-- C8

-- >>> mul 2 7 :: CNat
-- C14

-- >>> exp 2 10 :: CNat
-- C1024

-- >>> pred 0 :: CMaybe CNat
-- CNothing

-- >>> sub 5 5 :: CMaybe CNat
-- CJust C0

-- >>> lt 7 (7 :: CNat)
-- CFalse

-- >>> gt (one :: CNat) one
-- CFalse

-- >>> gte (zero :: CNat) zero
-- CTrue

-- >>> lte (zero :: CNat) zero
-- CTrue

-- >>> eq (zero :: CNat) zero
-- CTrue

-- >>> eq (zero :: CNat) one
-- CFalse

-- >>> max (zero :: CNat) one
-- C1
