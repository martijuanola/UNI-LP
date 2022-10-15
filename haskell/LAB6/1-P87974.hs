-- P87974	Haskell - Hola maco/a!

main = do
    nom <- getLine
    if elem (last nom) ['a','A'] then do
        putStrLn $ "Hola maca!"
    else
        putStrLn $ "Hola maco!"