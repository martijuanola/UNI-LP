-- P90677   Haskell - Definició de funcions d'ordre superior (1)

myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl f b [] = b
myFoldl f b (a:as) = myFoldl f (f b a) as

------------------------------------------------------------------------

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr f b [] = b
myFoldr f b (a:as) = f a $ myFoldr f b as

------------------------------------------------------------------------

myIterate :: (a -> a) -> a -> [a]
myIterate f a = a : myIterate f (f a)

------------------------------------------------------------------------

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil c f a
    | c a = a
    | otherwise = myUntil c f (f a)

------------------------------------------------------------------------

myMap :: (a -> b) -> [a] -> [b]
myMap f l = foldr (\e lp -> [f e] ++ lp) [] l

------------------------------------------------------------------------

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f as = [a | a <- as, f a]

------------------------------------------------------------------------

myAll :: (a -> Bool) -> [a] -> Bool
myAll f as = and $ myMap f as

------------------------------------------------------------------------

myAny :: (a -> Bool) -> [a] -> Bool
myAny f as = or $ myMap f as

------------------------------------------------------------------------

myZip :: [a] -> [b] -> [(a, b)]
myZip _ [] = []
myZip [] _ = []
myZip (a:as) (b:bs) = (a,b) : myZip as bs

------------------------------------------------------------------------

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f as bs = [f a b | (a,b) <- myZip as bs]

------------------------------------------------------------------------

