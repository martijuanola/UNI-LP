-- P93632   Haskell - Ús de funcions d'ordre superior (1)

eql :: [Int] -> [Int] -> Bool
eql l1 l2 = length l1 == length l2 && and (zipWith (==) l1 l2)

------------------------------------------------------------------------

prod :: [Int] -> Int
prod = foldl (*) 1

------------------------------------------------------------------------

prodOfEvens :: [Int] -> Int
prodOfEvens l = foldl (*) 1 $ filter even l

------------------------------------------------------------------------

powersOf2 :: [Int]
powersOf2 = iterate (*2) 1

------------------------------------------------------------------------

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct l1 l2 = sum $ zipWith (*) l1 l2

------------------------------------------------------------------------
