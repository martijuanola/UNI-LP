-- P70540   Haskell - Expressions

data Expr 
    = Val Int
    | Add Expr Expr
    | Sub Expr Expr
    | Mul Expr Expr
    | Div Expr Expr

------------------------------------------------------------------------

eval1 :: Expr -> Int
eval1 (Val v) = v
eval1 (Add e1 e2) = eval1 e1 + eval1 e2
eval1 (Sub e1 e2) = eval1 e1 - eval1 e2
eval1 (Mul e1 e2) = eval1 e1 * eval1 e2
eval1 (Div e1 e2) = eval1 e1 `div` eval1 e2

------------------------------------------------------------------------

eval2 :: Expr -> Maybe Int
eval2 (Val v) = (Just v)
eval2 (Add e1 e2) = eval2aux e1 e2 (+)
eval2 (Sub e1 e2) = eval2aux e1 e2 (-)
eval2 (Mul e1 e2) = eval2aux e1 e2 (*)
eval2 (Div e1 e2)
    | eval2 e2 == (Just 0) = Nothing
    | otherwise = eval2aux e1 e2 div

eval2aux :: Expr -> Expr -> (Int -> Int -> Int) -> Maybe Int
eval2aux e1 e2 op = do
    v1 <- eval2 e1
    v2 <- eval2 e2
    return $ op v1 v2

------------------------------------------------------------------------

eval3 :: Expr -> Either String Int
eval3 (Val v) = (Right v)
eval3 (Add e1 e2) = eval3aux e1 e2 (+)
eval3 (Sub e1 e2) = eval3aux e1 e2 (-)
eval3 (Mul e1 e2) = eval3aux e1 e2 (*)
eval3 (Div e1 e2)
    | eval3 e2 == (Right 0) = Left "div0"
    | otherwise = eval3aux e1 e2 div

eval3aux :: Expr -> Expr -> (Int -> Int -> Int) -> Either String Int
eval3aux e1 e2 op = do
    v1 <- eval3 e1
    v2 <- eval3 e2
    return $ op v1 v2

------------------------------------------------------------------------





