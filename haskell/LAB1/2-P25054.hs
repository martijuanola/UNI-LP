-- P25054   Haskell - Funcions amb llistes

myLength :: [Int] -> Int
myLength [] = 0
myLength (h:t) = 1 + myLength t

------------------------------------------------------------------------

myMaximum :: [Int] -> Int
myMaximum [h] = h
myMaximum (h:t) = max h (myMaximum t)

------------------------------------------------------------------------

average :: [Int] -> Float
average a = (realToFrac (sum a)) / (realToFrac (length a))

------------------------------------------------------------------------

buildPalindrome :: [Int] -> [Int]
buildPalindrome a = reverse a ++ a
-- buildPalindrome (x:xs) buildPalindrome xs ++ [x,x] ++ xs

------------------------------------------------------------------------

remove :: [Int] -> [Int] -> [Int]
remove [] _ = []
remove (x:xs) ys
    | elem x ys = remove xs ys
    | otherwise = x : remove xs ys  

------------------------------------------------------------------------

flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs) = x ++ flatten xs

------------------------------------------------------------------------

oddsNevens :: [Int] -> ([Int],[Int])
oddsNevens xs = ([e | e <- xs, odd e], [e | e <- xs, even e])

------------------------------------------------------------------------

primeDivisors :: Int -> [Int]
primeDivisors x = [d | d <- [2 .. x], mod x d == 0, isPrime d]


isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime n = null divisors
    where 
        divisors = [x | x <- [2 .. n-1], mod n x == 0]
