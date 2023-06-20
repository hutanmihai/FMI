module Main where

import System.IO

import Exp
import Parsing
import Printing
import REPLCommand
import Lab2

main :: IO ()
main = do
  putStr "miniHaskell> "
  s <- getLine
  case parseFirst replCommand s of
    Nothin -> putStrLn  "Invalid command" >> main
    Just Quit -> return ()
    Just (Load _) -> putStrLn "Not implemented" >> main
    Just (Eval es) -> case parseFirst exprParser es of
      Nothing -> putStrLn "Error: cannot parse expression" >> main
      Just e -> putStrLn (showExp e) >> main
