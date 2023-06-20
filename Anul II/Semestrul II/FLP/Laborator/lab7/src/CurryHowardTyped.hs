import Prelude (undefined)

data False                                        -- empty type

data True = True                                  -- unit type

data And a b = And { proj1 :: a, proj2 :: b }     -- product

data Or a b                                       -- sum
  = Left a
  | Right b

type Not a = a -> False
type Iff a b = And (a -> b) (b -> a)

-- Natural deduction introduction and elimination rules

trueIntro :: True                                   -- true introduction
trueIntro = True

falseElim :: False -> b                             -- false elimination
falseElim x = case x of

implIntro :: (a -> b) -> (a -> b)                   -- implication introduction
implIntro f = f

implElim :: (a -> b) -> a -> b                      -- implication elimination
implElim f = f

andIntro :: a -> b -> And a b                       -- and introduction
andIntro = And

andElimL :: And a b -> a                            -- and elimination 1
andElimL = proj1

andElimR :: And a b -> b                            -- and elimination 2
andElimR = proj2

orIntroL :: a -> Or a b                             -- or introduction 1
orIntroL = Left

orIntroR :: b -> Or a b                             -- or introduction 2
orIntroR = Right

orElim :: (a -> c) -> (b -> c) -> Or a b -> c      -- or elimination
orElim fac fbc or = case or of
      Left a -> fac a
      Right b -> fbc b

notElim :: Not p -> p -> c                          -- not elimination 
notElim p np = falseElim (p np)

notIntro :: (forall p. a -> p) -> Not a             -- not introduction
notIntro f = f

iffIntro :: (a -> b) -> (b -> a) -> Iff a b         -- iff introduction
iffIntro fab fba = andIntro fab fba

iffElimL :: a -> Iff a b -> b                     -- iff elimination 1
iffElimL a iff = andElimL iff a

iffElimR :: b -> Iff a b -> a                    -- iff elimination 1
iffElimR b iff = andElimR iff b

-- Hilbert-style axiomatization for intuitionistic propositional logic

ax1 :: a -> b -> a
ax1 = implIntro (\a -> implIntro (\b -> a))

ax2 :: (a -> b) -> (a -> (b -> c)) -> a -> c
ax2 = implIntro(\f -> implIntro (\g -> implIntro(\a -> implElim (implElim g a) (implElim f a))))

ax3 :: a -> b -> And a b
ax3 = implIntro (\a -> implIntro (\b -> andIntro a b))

ax4 :: And a b -> a
ax4 = implIntro (\andab -> andElimL andab)

ax5 :: And a b -> b
ax5 = implIntro (\andab -> andElimR andab)

ax6 :: a -> Or a b
ax6 = implIntro (\a -> orIntroL a)

ax7 :: b -> Or a b
ax7 = implIntro (\b -> orIntroR b)

ax8 :: (a -> c) -> (b -> c) -> Or a b -> c
ax8 = implIntro (\ac -> implIntro (\bc -> implIntro (\orab -> orElim ac bc orab)))

ax9 :: (a -> b) -> (a -> Not b) -> Not a
ax9 = implIntro (\ab -> implIntro (\anb -> notIntro (\a -> notElim (ab a) (anb a))))

ax10 :: Not a -> a -> b
ax10 = implIntro (\na -> implIntro (\a -> falseElim (na a)))

-- Several tautologies

deMorgan1 :: And (Not p) (Not q) -> Not (Or p q)
deMorgan1 (And np nq) (Left p) = notElim p np
deMorgan1 (And np nq) (Right q) = notElim q nq

deMorgan2 :: Not (Or p q) -> And (Not p) (Not q)
deMorgan2 npq = And (notIntro (\p -> notElim (orIntroL p) npq)) (notIntro (\q -> notElim (orIntroR q) npq))

deMorgan3 :: Or (Not p) (Not q) -> Not (And p q)
deMorgan3 (Left np) (And p q) = notElim p np
deMorgan3 (Right nq) (And p q) = notElim q nq

type DeMorgan4 = forall p q . Not (And p q) -> Or (Not p) (Not q)

-- Classical axioms

type ExcludedMiddle = forall a. Or a (Not a)
type DoubleNegation = forall a. Not (Not a) -> a
type PeirceLaw = forall p q. ((p -> q) -> p) -> p

excludedMiddleImplDoubleNeg :: Or a (Not a) -> Not (Not a) -> a
excludedMiddleImplDoubleNeg = implIntro (\or -> 
    implIntro (\nna -> orElim (\a -> a) (\na -> falseElim (nna na)) or))
