module REPLCommand where

import Lab2
import Control.Applicative (many, (<|>))

data REPLCommand
  = Quit
  | Load String
  | Eval String

quit :: Parser REPLCommand
quit = do
  symbol ":q" <|> symbol ":quit"
  return Quit

load :: Parser REPLCommand
load = do
  symbol ":l" <|> symbol ":load"
  file <- many anyChar
  return $ Load file

eval :: Parser REPLCommand
eval = do
  exp <- many anyChar
  return $ Eval exp

replCommand :: Parser REPLCommand
replCommand = quit <|> load <|> eval


