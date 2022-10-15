s :: (Maybe Int) -> (Maybe Int) -> (Maybe Int)
s a b = do
    a' <- a
    b' <- b
    return (a' + b')

main :: IO()
main = do
    putStrLn("hola prova")
    print(s (Just 1) (Just 2))