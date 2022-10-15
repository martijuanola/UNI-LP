-- P31745   Haskell - Ús de funcions d'ordre superior (2)

flatten :: [[Int]] -> [Int]
flatten = foldl (++) []

------------------------------------------------------------------------

myLength :: String -> Int
myLength s = foldl (\x y -> y+x+1) 0 $ map (\x -> 0) s

------------------------------------------------------------------------

myReverse :: [Int] -> [Int]
myReverse l = foldl (flip (:)) [] l
--myReverse l = foldr (\x y -> y ++ [x]) [] l

------------------------------------------------------------------------

countIn :: [[Int]] -> Int -> [Int]
countIn ll x = map (length . filter (\e -> (==) e x)) ll

------------------------------------------------------------------------

firstWord :: String -> String
firstWord s = takeWhile (/=' ') $ dropWhile (==' ') s