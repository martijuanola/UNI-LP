--   P58738   Haskell - Arbres amb talla

data STree a = Nil | Node Int a (STree a) (STree a)
    deriving (Show)

talla :: STree a -> Int
talla Nil = 0
talla (Node t _ _ _) = t

isOk :: STree a -> Bool 
isOk Nil = True
isOk (Node t _ st1 st2) = (isOk st1) && (isOk st2) && (t == (talla st1) + (talla st2) + 1)

nthElement :: STree a -> Int -> Maybe a
nthElement Nil _ = Nothing
nthElement (Node t n st1 st2) i
    | i > t = Nothing
    | t1 >= i = nthElement st1 i
    | t1+1 == i = Just n
    | otherwise = nthElement st2 $ i-(t1+1)
    where 
        t1 = talla st1

mapToElements :: (a -> b) -> STree a -> [Int] -> [Maybe b]
mapToElements f t l = map (fmap f) $ map (nthElement t) l

instance Functor STree where
    fmap f Nil = Nil
    fmap f (Node t n st1 st2) = (Node t (f n) (fmap f st1) (fmap f st2))