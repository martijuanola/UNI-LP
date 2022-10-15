--  P24239   Haskell - Parcial 2018-11-06

roman2int :: String -> Int
roman2int "" = 0
roman2int [c] = romanMap c
roman2int (f:s:t)
    | fint >= sint = fint + roman2int (s:t)
    | otherwise = sint - fint + roman2int t
        where
            fint = romanMap f
            sint = romanMap s


roman2int' :: String -> Int
roman2int' l = sum $ zipWith check ((tail list) ++ [0]) $ list
    where
        list = map romanMap l
        check :: Int -> Int -> Int
        check a b
            | a > b = -b
            | otherwise = b

romanMap :: Char -> Int
romanMap c
    | c == 'I' = 1
    | c == 'V' = 5
    | c == 'X' = 10
    | c == 'L' = 50
    | c == 'C' = 100
    | c == 'D' = 500
    | otherwise = 1000


arrels :: Float -> [Float]
arrels x = scanl taylor x $ repeat x
    where  
        taylor :: Float -> Float -> Float
        taylor prev x = (prev + (x/prev)) / 2
        
arrel :: Float -> Float -> Float
arrel x e = arrelAux e $ arrels x
    where
        arrelAux :: Float -> [Float] -> Float
        arrelAux e (x1:x2:t)
            | abs(x1-x2) <= e = x2
            | otherwise = arrelAux e (x2:t)

data LTree a = Leaf a | Node (LTree a) (LTree a)

instance Show a => Show (LTree a) where
    show (Leaf x) = "{" ++ (show x) ++ "}"
    show (Node lt1 lt2) = "<" ++ (show lt1) ++ "," ++ (show lt2) ++ ">"

build :: [a] -> LTree a
build l = buildAux $ map Leaf l
    where
        buildAux :: [LTree a] -> LTree a
        buildAux [x] = x
        buildAux x = (Node (buildAux (take l x)) (buildAux (drop l x)))
            where
                l = div (length x + 1) 2


zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a,b))
zipLTrees (Leaf x) (Leaf y) = Just (Leaf (x,y))
zipLTrees (Leaf x) (Node _ _) = Nothing
zipLTrees (Node _ _) (Leaf y) = Nothing
zipLTrees (Node l1 r1) (Node l2 r2) = do
        lt <- (zipLTrees l1 l2)
        rt <- (zipLTrees r1 r2)
        return (Node lt rt)



-- zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a,b))
-- zipLTrees (Leaf x) (Leaf y) = Just (Leaf (x,y))
-- zipLTrees (Leaf x) (Node _ _) = Nothing
-- zipLTrees (Node _ _) (Leaf y) = Nothing
-- zipLTrees (Node l1 r1) (Node l2 r2) = (fmap Node (zipLTrees l1 l2)) <*> (zipLTrees r1 r2)






