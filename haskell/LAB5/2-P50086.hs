-- P50086	Haskell - Cua (2)

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
------------------------------------------------------------------------


instance Functor Queue where
    fmap f (Queue l1 l2) = (Queue (map f l1) (map f l2))

------------------------------------------------------------------------

translation :: Num b => b -> Queue b -> Queue b
translation b q = fmap (+b) q

------------------------------------------------------------------------

q2l :: (Queue a) -> [a]
q2l (Queue l1 l2) = l1 ++ (reverse l2)

instance Applicative Queue where
    pure x = (Queue [] [x])
    qf <*> q = (Queue l [])
        where l = (q2l qf) <*> (q2l q)


instance Monad Queue where
    return x = (Queue [] [x])
    q >>= f = (Queue l [])
        where l = (q2l q) >>= (q2l . f)

------------------------------------------------------------------------

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter f q = do
    x <- q
    if(f x) then return x else (Queue [] [])






