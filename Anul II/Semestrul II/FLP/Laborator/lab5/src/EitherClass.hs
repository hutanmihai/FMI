module EitherClass where

import Prelude (Show(..), (<>), undefined) -- for show instances
import qualified Data.Either as Either (Either (..), either)

import MyPrelude
import BoolClass

-- | The class of Either-like types (types representing a
-- disjoint union of two other types through constructors
-- injecting them in the type: 'left' for the type on the
-- left, and 'right' for the type on the right; as well as
-- a way to do a case analysis on the values and apply 
-- a function for each of the cases.
-- Instances should satisfy the following:
--
-- [Either Left]  @'either' lHandle rHandle ('left' x) = lHandle x@
-- [Either Right] @'either' lHandle rHandle ('right' y ) = rHandle y@
class EitherClass e where
  left :: a -> e a b
  right :: b -> e a b
  either :: (a -> c) -> (b -> c) -> e a b -> c

instance EitherClass Either.Either where 
  left = Either.Left
  right = Either.Right
  either = Either.either

-- | The 'fromLeft' function takes a default value and a 'EitherClass' value.
-- If the 'EitherClass' is 'right' @x@, it returns the default value;
-- otherwise, it returns the value contained in the 'left'.
fromLeft :: (EitherClass e) => a -> e a b -> a
fromLeft a e = either id (const a) e

-- >>> fromLeft true (left false :: Either.Either CBool CBool)
-- CFalse

-- >>> fromLeft true (right false :: Either.Either CBool CBool)
-- CTrue

-- | The 'fromRight' function takes a default value and a 'EitherClass' value.
-- If the 'EitherClass' is  of the form $'left' _@, it returns the default value;
-- otherwise, it returns the value contained in the 'right'.
fromRight :: (EitherClass e) => b -> e a b -> b
fromRight b e = either (const b) id e

-- >>> fromRight true (left false :: Either.Either CBool CBool)
-- CTrue

-- >>> fromRight true (right false :: Either.Either CBool CBool)
-- CFalse

-- | The isLeft function returns 'true' iff its argument is of the form @'left' _@.
isLeft :: (EitherClass e, BoolClass b) => e l r -> b
isLeft e = either (const true) (const false) e

-- >>> isLeft (left false :: Either.Either CBool CBool) :: CBool
-- CTrue

-- | The isRight function returns 'true' iff its argument is of the form @'right' _@.
isRight :: (EitherClass e, BoolClass b) => e l r -> b
isRight e = either (const false) (const true) e

-- >>> isRight (left true :: Either.Either CBool CBool) :: CBool
-- CFalse

-- | The 'left' 'Functor' instance for 'EitherClass'
eitherLeftMap :: EitherClass e => (a -> a') -> e a b -> e a' b
eitherLeftMap f e = either (left . f) right e

-- >>> eitherLeftMap not (left true) :: Either.Either CBool CBool
-- Left CFalse

-- | The 'right' 'Functor' instance for 'EitherClass'
eitherRightMap :: EitherClass e => (b -> b') -> e a b -> e a b'
eitherRightMap f e = either left (right . f) e

-- >>> eitherRightMap not (left true) :: Either.Either CBool CBool
-- Left CTrue

newtype CEither a b = CEither { getCEither :: forall c . (a -> c) -> (b -> c) -> c }

instance EitherClass CEither where
  left x = CEither (\lHandle _ -> lHandle x)
  right y = CEither (\_ rHandle -> rHandle y)
  either lHandle rHandle e = getCEither e lHandle rHandle

-- >>> fromLeft true (left false :: CEither CBool CBool)
-- CFalse

-- >>> fromLeft true (right false :: CEither CBool CBool)
-- CTrue

-- >>> fromRight true (left false :: CEither CBool CBool)
-- CTrue

-- >>> fromRight true (right false :: CEither CBool CBool)
-- CFalse

-- >>> isLeft (left false :: Either.Either CBool CBool) :: CBool
-- CTrue

-- >>> isRight (left true :: CEither CBool CBool) :: CBool
-- CFalse

-- | converting between different instances of 'EitherClass'
fromEitherClass :: (EitherClass m, EitherClass n) => m a b -> n a b
fromEitherClass = either left right

-- | 'Show' instance for 'CEither a b' (via transformation into Haskell Either)
instance (Show a, Show b) => Show (CEither a b) where
  show cm = "C" <> show (fromEitherClass cm :: Either.Either a b)

-- >>> eitherLeftMap not (left true) :: CEither CBool CBool
-- CLeft CFalse

-- >>> eitherRightMap not (left true) :: CEither CBool CBool
-- CLeft CTrue
