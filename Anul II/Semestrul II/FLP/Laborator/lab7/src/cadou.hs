data False -- empty type, void

data True = True -- unit type

data And a b = And { proj1 :: a, proj2 :: b } 

data Or a b = Left a 
            | Right b

type Not a = a -> False

type Iff a b = And (a -> b) (b -> a)


trueIntro :: True 
trueIntro = Main.True


falseElim :: False -> b
falseElim x = case x of {}

implElim :: (a -> b) -> a -> b
implElim f = f

implIntro :: (a -> b) -> a -> b
implIntro f = f

andIntro :: a -> b -> And a b
andIntro = And

andElimL :: And a b -> a
andElimL = proj1

andElimR :: And a b -> b
andElimR = proj2

orIntroL :: a -> Or a b
orIntroL = Main.Left


orIntroR :: b -> Or a b
orIntroR = Main.Right

orElim :: (a -> c) -> (b -> c) -> Or a b -> c
orElim fac fbc or = case or of
    Main.Left a -> fac a
    Main.Right b -> fbc b

notIntro :: (forall p. a -> p) -> Not a
notIntro f = f

notElim :: p -> Not p -> c
notElim p np = falseElim (np p)

iffIntro :: (a -> b) -> (b -> a) -> Iff a b
iffIntro fab fba = andIntro fab fba

iffElimL :: a -> Iff a b -> b
iffElimL a iff = (andElimL iff) a

iffElimR :: b -> Iff a b -> a
iffElimR b iff = (andElimR iff) b



ax1 :: a -> b -> a
ax1 = implIntro (\a -> implIntro (\b -> a))


ax2 :: (a -> b) -> (a -> (b -> c)) -> a -> c
ax2 = implIntro (\f -> implIntro (\g -> implIntro (\a -> implElim (implElim g a) (implElim f a))))


ax3 :: a -> b -> And a b
ax3 = implIntro (\a -> implIntro (\b -> andIntro a b))


ax4 :: And a b -> a
ax4 = implIntro (\ab -> andElimL ab)


ax5 :: And a b -> b
ax5 = implIntro (\ab -> andElimR ab)

ax6 :: a -> Or a b
ax6 = implIntro (\a -> orIntroL a)

ax7 :: b -> Or a b
ax7 = implIntro (\b -> orIntroR b)

ax8 :: (a -> c) -> (b -> c) -> Or a b -> c
ax8 = implIntro (\fac -> implIntro (\fbc -> implIntro (\or -> orElim fac fbc or)))

ax9 :: (a -> b) -> (a -> Not b) -> Not a
ax9 = implIntro (\fab -> implIntro (\fna -> notIntro (\a -> notElim (fab a) (fna a))))

ax10 :: Not a -> a -> b
ax10 = implIntro (\na -> implIntro (\a -> falseElim (na a)))


deMorgan1 :: And (Not p) (Not q) -> Not (Or p q)
deMorgan1 (And np nq) (Main.Left p) = notElim p np
deMorgan1 (And np nq) (Main.Right q) = notElim q nq


deMorgan2 :: Not (Or p q) -> And (Not p) (Not q)
deMorgan2 npq = And (notIntro (\p -> notElim (orIntroL p) npq)) (notIntro (\q -> notElim (orIntroR q) npq))


deMorgan3 :: Or (Not p) (Not q) -> Not (And p q)
deMorgan3 (Main.Left np) (And p q) = notElim p np
deMorgan3 (Main.Right nq) (And p q) = notElim q nq



excludedMiddleImplDoubleNeg :: Or a (Not a) -> Not (Not a) -> a
excludedMiddleImplDoubleNeg = implIntro (\or -> 
    implIntro (\nna -> orElim (\a -> a) (\na -> falseElim (nna na)) or))
