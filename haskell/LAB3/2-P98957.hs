-- P98957   Haskell - Llistes infinites

ones :: [Integer]
ones = iterate (+0) 1
-- ones = 1 : ones

------------------------------------------------------------------------

nats :: [Integer]
nats = iterate (+1) 0
-- nats = 0 : map (+1) nats

------------------------------------------------------------------------

ints :: [Integer]
ints = scanl (+) 0 $ zipWith (*) (iterate (+1) 1) $ iterate (*(-1)) 1
-- es pot fer amb zip de positius i negatius i després un scanl on separa els (a,b)
-- també es pot fer amb estil dels de dalt, amb una funció auxiliar recursiva

------------------------------------------------------------------------

triangulars :: [Integer]
-- triangulars = map (\x -> div x 2) $ zipWith (*) nats $ map (+1) nats
-- tirangulars = 0 : zipWith (+) triangulars (tail nats)
triangulars = scanl (+) 0 $ tail nats

------------------------------------------------------------------------

factorials :: [Integer]
factorials = scanl (*) 1 $ tail nats

------------------------------------------------------------------------

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

------------------------------------------------------------------------

primes :: [Integer]
primes = garbell $ iterate (+1) 2
    where
        garbell (p : xs) = p : garbell [x | x <- xs, x `mod` p /= 0]

------------------------------------------------------------------------

hammings :: [Integer]
hammings = 1 : merge h2 (merge h3 h5)
    where
        h2 = map (*2) hammings
        h3 = map (*3) hammings
        h5 = map (*5) hammings


merge :: [Integer] -> [Integer] -> [Integer]
merge (x:xs) (y:ys)
    | x < y = x : merge xs (y:ys)
    | x > y = y : merge (x:xs) ys
    | otherwise = x : merge xs ys

------------------------------------------------------------------------

lookNsay :: [Integer]
lookNsay = iterate lookNsayVal 1

lookNsayVal :: Integer -> Integer
lookNsayVal n = read $ lookNsayCalc $ show n

lookNsayCalc :: [Char] -> [Char]
lookNsayCalc [] = []
lookNsayCalc s = (show count) ++ [h] ++ lookNsayCalc t
    where
        count = length $ takeWhile ( == h) s
        h = head s
        t = dropWhile ( == h) s

------------------------------------------------------------------------

tartaglia :: [[Integer]]
tartaglia = iterate tartRow [1]
    where
        tartRow l = zipWith (+) ([0] ++ l) (l ++ [0])

------------------------------------------------------------------------

