-- P71775   Haskell - Definició de funcions d'ordre superior (2)

countIf :: (Int -> Bool) -> [Int] -> Int
countIf f l = foldl (\x y -> y+x+1) 0 $ map (\x -> 0) $ filter f l

------------------------------------------------------------------------

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam l lf = map (\f -> map f l) lf

------------------------------------------------------------------------

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 l lf = map (\e -> map ($ e) lf) l

------------------------------------------------------------------------

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl c f x l = foldl f x $ filter c l

------------------------------------------------------------------------

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert r l x = takeWhile (\a -> r a x) l ++ [x] ++ dropWhile (\a -> r a x) l
--insert r (h:t) x
--    | r x h = x:h:t
--    | otherwise = h:(insert r t x)


insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort r l = foldl (insert r) [] l

------------------------------------------------------------------------

