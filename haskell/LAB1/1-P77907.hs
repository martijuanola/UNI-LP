-- P77907   Haskell - Funcions amb nombres

absValue :: Int -> Int
absValue n
    | n >= 0      = n
    | otherwise   = -n

------------------------------------------------------------------------

power :: Int -> Int -> Int
power _ 0 = 1
power x p
    | even p      = y * y
    | otherwise   = y * y * x
    where 
        y = power x (div p 2)

------------------------------------------------------------------------

isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime n = null divisors
    where 
        divisors = [x | x <- [2 .. n-1], mod n x == 0]

------------------------------------------------------------------------

slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2)

------------------------------------------------------------------------

quickFib :: Int -> Int
quickFib 0 = 0
quickFib 1 = 1
quickFib n = quickFibAux 0 1 (n-1)
    where
        quickFibAux _ b 0 = b
        quickFibAux a b c = quickFibAux b (a+b) (c-1)
