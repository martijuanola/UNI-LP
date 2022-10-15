-- P37072   Haskell - Arbre binari

data Tree a = Node a (Tree a) (Tree a) | Empty
    deriving (Show)

------------------------------------------------------------------------

size :: Tree a -> Int
size Empty = 0
size (Node v left right) = 1 + size left + size right

------------------------------------------------------------------------

height :: Tree a -> Int
height Empty = 0
height (Node v left right) = 1 + max (height left) (height right)

------------------------------------------------------------------------

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty = True
equal Empty (Node _ _ _) = False
equal (Node _ _ _) Empty = False
equal (Node v1 left1 right1) (Node v2 left2 right2) = (v1 == v2) && (equal left1 left2) && (equal right1 right2)

------------------------------------------------------------------------

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty = True
isomorphic Empty (Node _ _ _) = False
isomorphic (Node _ _ _) Empty = False
isomorphic (Node v1 left1 right1) (Node v2 left2 right2) = (v1 == v2) && (((isomorphic left1 left2) && (isomorphic right1 right2)) || ((isomorphic left1 right2) && (isomorphic left2 right1)))

------------------------------------------------------------------------

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node v1 left1 right1) = v1 : preOrder left1  ++ preOrder right1

------------------------------------------------------------------------

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node v1 left1 right1) = postOrder left1 ++ postOrder right1 ++ [v1]

------------------------------------------------------------------------

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node v1 left1 right1) = inOrder left1 ++ [v1] ++ inOrder right1

------------------------------------------------------------------------

breadthFirst :: Tree a -> [a]
breadthFirst t = cua [t]

cua :: [Tree a] -> [a]
cua [] = []
cua (Empty:tail) = cua tail
cua ((Node v1 left right) : tail) = v1 : cua (tail ++ [left] ++ [right])

------------------------------------------------------------------------

build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build (ph:pt) (i) = (Node ph (build pl il) (build pr ir))
    where
        (il, _:ir) = span (/= ph) i
        (pl, pr) = splitAt (length il) pt


------------------------------------------------------------------------

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ t Empty = t
overlap _ Empty t = t
overlap f (Node v1 left1 right1) (Node v2 left2 right2) = Node (f v1 v2) (overlap f left1 left2) (overlap f right1 right2)



