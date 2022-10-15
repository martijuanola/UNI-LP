-- P87082   Haskell - Índex de massa corporal


imcText :: String -> String
imcText line = nom ++ ": " ++ (interpretacio $ imc m h)
    where
        nom = head $ words line
        [m,h] = map read $ tail $ words line :: [Float]

imc :: Float -> Float -> Float
imc m h = m/(h^2)

interpretacio :: Float -> String
interpretacio imcVal
    | imcVal < 18 = "magror"
    | imcVal < 25 = "corpulencia normal"
    | imcVal < 30 = "sobrepes"
    | imcVal < 40 = "obesitat"
    | otherwise = "obesitat morbida"

main = do
    line <- getLine
    if line /= "*" then do
       putStrLn $ imcText line
       main
    else
       return ()