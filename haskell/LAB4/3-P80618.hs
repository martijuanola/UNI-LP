-- P80618   Haskell - Cua (1)

data Queue a = Queue [a] [a]
     deriving (Show)

------------------------------------------------------------------------

create :: Queue a
create = Queue [] []

------------------------------------------------------------------------

push :: a -> Queue a -> Queue a
push x (Queue l1 l2) = Queue l1 (x:l2)

------------------------------------------------------------------------

pop :: Queue a -> Queue a
pop (Queue (h:t) l2) = (Queue t l2) 
pop (Queue [] l2) = Queue (reverse $ init l2) []


------------------------------------------------------------------------

top :: Queue a -> a
top (Queue (h:t) _) = h
top (Queue [] l2) = head $ reverse l2

------------------------------------------------------------------------

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty _ = False

------------------------------------------------------------------------

instance Eq a => Eq (Queue a)
    where
        (Queue [] []) == (Queue [] []) = True
        (Queue [] []) == _ = False
        _ == (Queue [] []) = False
        a == b = (top a == top b) && (pop a == pop b)

    --where (Queue l1 l2) == (Queue s1 s2) = l1 ++ reverse l2 == s1 ++ reverse s2
    
------------------------------------------------------------------------






