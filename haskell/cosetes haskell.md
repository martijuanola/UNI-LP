## Cosetes Haskell

[TOC]

------

### Useful Functions

#### GHCi Directives

```haskell
-- GENERAL --
-- Reload file -> :r
:r


-- Get type of expression -> :type
:type expr

-- Get information of Type -> :info | :i
:i Type
```



#### Basic Operators

```haskell
-- Equality -> (==)
(==) :: (Eq a) => a -> a -> Bool


-- Modul -> mod
mod :: Integral a => a -> a -> a


-- Logic AND -> (&&)
(&&) :: Bool -> Bool -> Bool

-- Logic OR -> (||)
(||) :: Bool -> Bool -> Bool

-- Logic NOT -> not
not :: Bool -> Bool


-- Element Append -> (:)
(:) :: a -> [a] -> [a]

-- List Concatenation -> (++)
(++) :: [a] -> [a] -> [a]



```



#### Basic Functions

```haskell
-- Text to Value -> read
Read a => String -> a

-- Value to Text -> show
Show a => a -> String

-- Parse string into Words
words String -> [String]



-- LISTS --
-- First Element -> head
head :: [a] -> a

-- All but last -> init
init ::	[a] -> [a]

-- Element Of -> elem
elem :: (Eq a) => a -> [a] -> Bool
λ> elem 1 [0,1] -- TRUE

-- Take first n elements -> take
take :: Int -> [a] -> [a]

-- Reverse -> reverse
reverse :: [a] -> [a]

-- Separate largest prefix that satisfies a formula -> span
span :: (a -> Bool) -> [a] -> ([a],[a])
λ> span (<3) [1,2,4,5,6] -- ([1,2], [4,5,6])

-- Separate list in index -> splitAt
splitAt :: Int -> [a] -> ([a],[a])
λ> splitAt 5 [1,2,3,4,5,6,7,8,9,10] -- ([1,2,3,4,5],[6,7,8,9,10])


--DICTIONARIES
lookup :: Eq a => a -> [(a,b)] -> Maybe b
λ> lookup 'c' [('a',0),('b',1),('c',2)] -- Just 2

```



#### Higher Order Functions

```haskell
-- Composition -> (.)
(.) :: (b -> c) -> (a -> b) -> a -> c

-- Mappeig -> map
map :: (a -> b) -> [a] -> [b]

-- Descartar els primers que... -> dropWhile
dropWhile :: (a -> Bool) -> [a] -> [a]

-- Agafar els primers que...  -> takeWhile
dropWhile :: (a -> Bool) -> [a] -> [a]

-- Agafar el elements que compleixin una condició -> filter
filter :: (a -> Bool) -> [a] -> [a]

-- Aplicar un conjunt d'elements acumuladament partint d'un element inicial -> foldl
foldl :: (b -> a -> b) -> b -> [a] -> b

```



------

### Types and Classes

Predefined Types

Polimorfic Types

#### Sinonim Types

```haskell
type Euros = Float
type Diccionari = String -> Int
```

#### Enumerated Types

```haskell
data Operador = Suma | Resta | Producte | Divisio
data Jugada = Pedra | Paper | Tisora
    deriving (Eq) -- Eq class instance
data Racional = Racional Int Int        -- numerador, denominador
    deriving (Eq, Show)
```

#### Algebraic Types

```haskell
data Forma
    = Rectangle Float Float         -- alçada, amplada
    | Quadrat Float                 -- mida
    | Cercle Float                  -- radi
    | Punt
```



#### Class Declaration

```haskell
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    
    x == y  = not (x /= y)
    x /= y  = not (x == y)
```

To define instance of Class:

```haskell
data Racional = Racional Int Int        -- numerador, denominador
    deriving (Eq)
    
instance Eq Racional where
    (Racional n1 d1) == (Racional n2 d2) = n1 * d2 == n2 * d1
```



#### Important Classes

- Eq --> **Equality**
- Ord --> **Order**
- Show --> **values** can be converted to **text**
- Read --> **text** can be converted to **values**
- Num --> Basic arithmetic((+), (-), (*),...)



------

### Functors, Aplicatius i Monades

#### Functors

Contenidor genèric al que se li poden aplicar funcions als elements que conté.

```haskell
λ> :info Functor
class Functor f where
    fmap :: (a -> b) -> (f a -> f b)
```

##### Operació Important:

`fmap` --> <$> (en versió infixe)

Aplica una funció a un functor

##### Functors:

- Maybe
- Either a (Either no ho és)
- Llistes []
- Funcions



##### Lleis de Functors

- Identitat: `fmap id ≡ id`
- Composició: `fmap (g1 . g2) ≡ fmap g1 . fmap g2`



#### Aplicatius

##### Operacions Importants:

app --> `<*>` (en versió infixe)

Aplica una funció  a un element els dos dintre del mateix tipus de contenidor.

`pure` -> `pure  :: a -> f a`

Crea un contenidor amb un element a dintre



##### Lleis dels Aplicatius:

- Identitat: `pure id <*> v ≡ v`
- Homomorfisme: `pure f <*> pure x ≡ pure (f x)`
- Intercanvi: `u <*> pure y ≡ pure ($ y) <*> u`
- Composició: `u <*> (v <*> w) ≡ pure (.) <*> u <*> v <*> w`
- Relació amb el Functor: `fmap g x ≡ pure g <*> x`



#### Mònades

```haskell
class Monad m where
    return :: a -> m a
    (>>=)  :: m a -> (a -> m b) -> m b
    (>>)   :: m a -> m b -> m b
    r >> k   =   r >>= (\_ -> k)
```

##### Operació Important:

`return` --> (empaqueta)

`>>=`--> bind (desempaqueta, aplica i empaqueta)

`>>`--> estètica



##### Exemples:

- Monad



##### Lleis de Functors:

- Identitat per l'esquerra: `return x >>= f ≡ f x`
- Identitat per la dreta: `m >>= return ≡ m`
- Associativitat: `(m >>= f) >>= g ≡ m >>= (\x -> f x >>= g)`



FALTA DO!!!



FALTA FUNCIÓNS PER MÒNADES






------

### I/O

Main és una mònada que té per funcions:

```haskell
getChar     :: IO Char              -- obté següent caràcter
getLine     :: IO String            -- obté següent línia
getContents :: IO String            -- obté tota l'entrada

putChar     :: Char -> IO ()        -- escriu un caràcter
putStr      :: String -> IO ()      -- escriu un text
putStrLn    :: String -> IO ()      -- escriu un text i un salt de línia
print       :: Show a => a -> IO () -- escriu qualsevol showable
```



Altres statements que es poden fer servir:

- `if` condition `then do`  statements (`else` statements)+