-- P29040   Haskell - Ordenació

insert :: [Int] -> Int -> [Int]
insert [] e = [e]
insert (x:xs) e
    | x >= e    = e:x:xs 
    | otherwise = x : insert xs e

------------------------------------------------------------------------

isort :: [Int] -> [Int]
isort [] = []
isort (x:xs) = insert (isort xs) x

------------------------------------------------------------------------

remove :: [Int] -> Int -> [Int]
remove [] _ = []
remove (x:xs) e
    | x == e = xs
    | otherwise = x : remove xs e

------------------------------------------------------------------------

ssort :: [Int] -> [Int]
ssort [] = []
ssort xs = m : ssort (remove xs m)
    where
        m = minimum xs

------------------------------------------------------------------------

merge :: [Int] -> [Int] -> [Int]
merge [] xs = xs
merge xs [] = xs
merge (x:xs) (y:ys)
    | x < y = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

------------------------------------------------------------------------

msort :: [Int] -> [Int]
msort [] = []
msort [e] = [e]
msort xs = merge (msort (take h xs)) (msort (drop h xs))
    where
        h = div (length xs) 2
-- not tested
-- msort xs = merge (msort l1) (msort l2)
--    where
--       (l1, l2) = splitAt (div (len + 1) 2) xs

------------------------------------------------------------------------

qsort :: [Int] -> [Int]
qsort [] = []
qsort (x:xs) = qsort lower ++ [x] ++ qsort higher
    where
        lower = [y | y <- xs, y <= x]
        higher = [y | y <- xs, y > x]

------------------------------------------------------------------------

genQsort :: Ord a => [a] -> [a]
genQsort [] = []
genQsort (x:xs) = genQsort lower ++ [x] ++ genQsort higher
    where
        lower = [y | y <- xs, y <= x]
        higher = [y | y <- xs, y > x]





