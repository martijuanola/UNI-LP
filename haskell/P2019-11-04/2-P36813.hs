--   P36813   Haskell - P2 Parcial 2019-11-04

import Data.List

degree :: Eq a => [(a, a)] -> a -> Int
degree [] e = 0
degree ((a, b):t) e
    | a == e = 1 + rest
    | b == e = 1 + rest
    | otherwise = rest
    where
       rest = degree t e


degree' :: Eq a => [(a, a)] -> a -> Int
degree' l e = length $ filter (\(a,b) -> (a == e) || (b == e)) l


neighbors :: Ord a => [(a, a)] -> a -> [a]
neighbors l e = sort $ map (getNeighbor e) $ filter (\(a,b) -> (a == e) || (b == e)) l


getNeighbor :: Eq a => a -> (a, a) -> a
getNeighbor e (a,b)
    | a == e = b
    | otherwise = a