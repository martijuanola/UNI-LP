-- P97301   Haskell - FizzBuzz

fizzBuzz :: [Either Int String]
fizzBuzz = map fbTransform (iterate (+1) 0)

fbTransform :: Int -> Either Int String
fbTransform n 
	| mod n 3 == 0 && mod n 5 == 0 = Right "FizzBuzz"
	| mod n 3 == 0 = Right "Fizz"
	| mod n 5 == 0 = Right "Buzz"
	| otherwise = Left n