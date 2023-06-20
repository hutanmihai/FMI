module Exp where

import Numeric.Natural

newtype Var = Var { getVar :: String }
  deriving (Show)

data ComplexExp                         --  ComplexExp ::= "(" ComplexExp ")"
  = CX Var                              --          |   Var
  | Nat Natural                           --        |   Natural
  | CLam Var ComplexExp                 --          |   "\" Var "->" ComplexExp
  | CApp ComplexExp ComplexExp          --          |   ComplexExp ComplexExp
  | Let Var ComplexExp ComplexExp       --          |   "let" Var ":=" ComplexExp "in"
  | LetRec Var ComplexExp ComplexExp    --          |   "letrec" Var ":=" ComplexExp "in"
  | List [ComplexExp]                   --          |   "[" {ComplexExp ","}* "]"
  deriving (Show)

data IndexedVar = IndexedVar { ivName :: String, ivCount :: Int } deriving (Eq, Read, Show)

data Exp = X IndexedVar
  | Lam IndexedVar Exp
  | App Exp Exp
  deriving (Show)

vars :: Exp -> [IndexedVar]
vars (X x) = [x]
vars (App t1 t2) = vars t1 `union` vars t2
vars (Lam x t) = [x] `union` vars t

freeVars :: Exp -> [IndexedVar]
freeVars (X x) = [x]
freeVars (App t1 t2) = freeVars t1 `union` freeVars t2
freeVars (Lam x t) = delete x $ freeVars t

occursFree :: IndexedVar -> Exp -> Bool
occursFree x t = elem x $ freeVars t

freshVar :: IndexedVar -> [IndexedVar] -> IndexedVar
freshVar x xs = x { ivCount = m + 1}
  where
    nxs = [ivCount y | y <-x : xs, ivName x == ivName y]
    m = if null nxs then 0 else maximum nxs

renameVar :: IndexedVar -> IndexedVar -> Exp -> Exp
renameVar toReplace replacement = go
  where
    go (X x) = if x == toReplace then X replacement else X x
    go (App t1 t2) = App (go t1) (go t2)
    go (Lam x t) = Lam x (if x == toReplace then t else go t)

substitute :: IndexedVar -> Exp -> Exp -> Exp
substitute toReplace replacement = go
  where
    go (X x) = if x == toReplace then replacement else X x
    go (App t1 t2) = App (go t1) (go t2)
    go (Lam x t) = Lam x (if x == toReplace then t else go t)

sugar :: Exp -> ComplexExp
sugar (X x) = CX $ Var $ ivName x
sugar (App t1 t2) = CApp (sugar t1) (sugar t2)
sugar (Lam x t) = CLam (Var $ ivName x) (sugar t)

desugar :: ComplexExp -> Exp
desugar (CX x) = X $ IndexedVar (getVar x) 0
desugar (CApp t1 t2) = App (desugar t1) (desugar t2)
desugar (CLam x t) = Lam (IndexedVar (getVar x) 0) (desugar t)