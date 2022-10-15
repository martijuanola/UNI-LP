--    P91910   Haskell - Parcial 2018-04-11

multEq :: Int -> Int -> [Int]
multEq a b = iterate (*c) 1
    where
       c = a * b

selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
selectFirst l1 l2 l3 = [e | e <- l1, before l2 l3 e]
    where
        before :: [Int] -> [Int] -> Int -> Bool
        before [] _ e = False
        before (h1:t1) [] e
            | h1 == e = True
            | otherwise = before t1 [] e
        before (h1:t1) (h2:t2) e 
            | h1 == e && h2 /= e = True
            | h1 /= e && h2 /= e = before t1 t2 e
            | otherwise = False

myIterate :: (a -> a) -> a -> [a]
myIterate f x = scanl (\x1 x2 -> f x1) x $ repeat 0

type SymTab a = String -> Maybe a

empty :: SymTab a
empty s = Nothing

get :: SymTab a -> String -> Maybe a
get table = table

set :: SymTab a -> String -> a -> SymTab a
set table key value s = if s == key then Just value else table s


data Expr a
     = Val a
     | Var String
     | Sum (Expr a) (Expr a)
     | Sub (Expr a) (Expr a)
     | Mul (Expr a) (Expr a)
     deriving Show

eval :: (Num a) => SymTab a -> Expr a -> Maybe a
eval st (Val x) = Just x
eval st (Var s) = st s
eval st (Sum expr1 expr2) = applyFtoM (+) (eval st expr1) (eval st expr2)
eval st (Sub expr1 expr2) = applyFtoM (-) (eval st expr1) (eval st expr2)
eval st (Mul expr1 expr2) = applyFtoM (*) (eval st expr1) (eval st expr2)

applyFtoM :: (Num a) => (a -> a -> a) -> (Maybe a) -> (Maybe a) -> (Maybe a)
applyFtoM f a b = f <$> a <*> b
















