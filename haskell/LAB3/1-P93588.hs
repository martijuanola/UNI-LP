-- P93588   Haskell - Ús de llistes per comprensió

myMap :: (a -> b) -> [a] -> [b]
myMap f l = [f x | x <- l]

------------------------------------------------------------------------

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f l = [x | x <- l, f x]

------------------------------------------------------------------------

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f l1 l2 = [ f a b | (a,b) <- (zip) l1 l2]

------------------------------------------------------------------------

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify l1 l2 = [(a,b) | a <- l1, b <- l2, mod a b == 0]

------------------------------------------------------------------------

factors :: Int -> [Int]
factors e = [f | f <- [1 .. e], mod e f == 0]




