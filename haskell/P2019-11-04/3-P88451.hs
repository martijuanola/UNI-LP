--   P88451   Haskell - P3 Parcial 2019-11-04

data Tree a = Node a (Tree a) (Tree a) | Empty

instance Show a => Show (Tree a) where
    show Empty = "()"
    show (Node a t1 t2) = "(" ++ (show t1) ++ "," ++ (show a) ++ "," ++ (show t2) ++ ")"

instance Functor Tree where
    fmap f Empty = Empty
    fmap f (Node a t1 t2) = (Node (f a) (fmap f t1) (fmap f t2))

doubleT :: Num a => Tree a -> Tree a
doubleT t = fmap (*2) t

data Forest a = Forest [Tree a]
    deriving (Show)

instance Functor Forest where
    fmap f (Forest ts) = Forest $ map (fmap f) ts


doubleF :: Num a => Forest a -> Forest a
doubleF f = fmap (*2) f