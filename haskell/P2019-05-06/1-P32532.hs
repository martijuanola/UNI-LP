--    P32532   Haskell - Nombres molt compostos

divisors :: Int -> [Int]
divisors n = [x | x <- [1..n], mod n x == 0]


nbDivisors :: Int -> Int
nbDivisors n = length $ divisors n


moltCompost :: Int -> Bool
moltCompost n = [] == [x | x <- [1..n-1], nbDivisors x >= nbDivisors n]