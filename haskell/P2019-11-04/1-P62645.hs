-- P62645   Haskell - P1 Parcial 2019-11-04

addList :: [Int] -> Int
addList l = foldl (+) 0 l

main = do
    text <- getContents
    putStrLn $ show $ addList $ map read $ words text


