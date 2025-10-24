--ej 1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--ej 1.2 
ultimo :: [t] -> t
ultimo (xs) = head (reverso(xs))

--ej 1.3 
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio (xs)

--ej 1.4
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso (xs) ++ [x]

--ej 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece t [] = False
pertenece t (x:xs)
    | t == x = True
    | otherwise = pertenece t xs

--ej 2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs)
    | x == y = todosIguales (y:xs)
    | x /= y = False

--ej 2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:y:xs)
    | x == y = False
    | x /= y && todosDistintos (x:xs) && todosDistintos (y:xs) = True
    | otherwise = False

--ej 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos xs
    | todosDistintos xs == True = False
    | otherwise = True

--ej 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar t (x:xs)
    | t == x = xs
    | otherwise = (x:(quitar t xs)) 

--ej 2.6 
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos t [] = []
quitarTodos t (x:xs)
    | pertenece t (x:xs) == False = (x:xs)
    | pertenece t (x:xs) && t == x = quitarTodos t xs
    | otherwise = (x:(quitarTodos t xs))

--ej 2.7
eliminarRepetidos :: (Eq t) => [t] -> [t] --funciona bien pero me cambia el orden: me deja al final los que no estaban repetidos
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = reverso(eliminarRepetidos(quitarTodos x (x:xs)) ++ [x])

--ej 2.8
lista1ContenidaenLista2 :: (Eq t) => [t] -> [t] -> Bool
lista1ContenidaenLista2 [] [] = True
lista1ContenidaenLista2 [] (y:ys) = True
lista1ContenidaenLista2 (x:xs) [] = False
lista1ContenidaenLista2 (x:xs) (y:ys)
    | pertenece x (y:ys) = lista1ContenidaenLista2 xs (y:ys)
    | otherwise = False

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys
    | lista1ContenidaenLista2 (eliminarRepetidos xs) (eliminarRepetidos ys) && lista1ContenidaenLista2 (eliminarRepetidos ys) (eliminarRepetidos xs) = True
    | otherwise = False

--ej 2.9
capicua :: (Eq t) => [t] -> Bool
capicua xs 
    | xs == reverso xs = True
    | otherwise = False

--ej 3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--ej 3.2
productoria :: [Integer] -> Integer
productoria [] = 0
productoria [x] = x
productoria (x:xs) = x * productoria xs

--ej 3.3
maximo :: [Integer] -> Integer
maximo (x:[]) = x
maximo (x:y:xs) 
    | x >= y = maximo (x:xs)
    | otherwise = maximo (y:xs)

minimo :: [Integer] -> Integer
minimo (x:[]) = x
minimo (x:y:xs) 
    | x <= y = minimo (x:xs)
    | otherwise = minimo (y:xs)

--ej 3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (n+x) : sumarN n xs

--ej 3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

--ej 3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo xs = sumarN (head(reverso xs)) xs

--ej 3.7
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)
    | mod x 2 == 0 = x : pares xs
    | otherwise = pares xs

--ej 3.8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs)
    | mod x n == 0 = x : multiplosDeN n xs
    | otherwise = multiplosDeN n xs

--ej 3.9
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar l = ordenar (quitar (maximo l) l ) ++ [maximo l]

--ej 4a
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs)
    | x == y && x == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x : sacarBlancosRepetidos (y:xs)

--ej 4b
contarPalabras :: [Char] -> Integer
contarPalabras xs = contarEspacios(sacarBlancosRepetidos(sacarEspaciosFinal(sacarEspaciosInicio xs)))

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs)
    | x == ' ' = 1 + contarEspacios xs
    | otherwise = contarEspacios xs

sacarEspaciosInicio :: [Char] -> [Char]
sacarEspaciosInicio [] = []
sacarEspaciosInicio (x:xs)
    | x == ' ' = xs
    | otherwise = (x:xs)

sacarEspaciosFinal :: [Char] -> [Char]
sacarEspaciosFinal [] = []
sacarEspaciosFinal xs 
    | head(reverso xs) == ' ' = reverso(tail (reverso xs))
    | otherwise = xs

--ej 4c
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras [x] = [[x]]
palabras (x:xs) = (primeraPalabra (x:xs)) : palabras (eliminarPrimeraPalabra (x:xs))


primeraPalabra :: [Char] -> [Char] --asume que no empieza por espacio
primeraPalabra [] = []
primeraPalabra (x:xs) 
    | x /= ' ' = x : (primeraPalabra xs)
    | x == ' ' = []

eliminarPrimeraPalabra :: [Char] -> [Char] -- tmb asume que no empieza en espacio
eliminarPrimeraPalabra [] = []
eliminarPrimeraPalabra (x:xs)
    | x == ' ' = sacarBlancosRepetidos xs --parece que no hace nada el sacarBlancosRepetidos
    | x /= ' ' = sacarBlancosRepetidos (eliminarPrimeraPalabra xs)

--ej 4d --NO FUNCIONA. REVISAR
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga (x:xs)
    | longitud (palabras (x:xs) [0]) < longitud (palabras(x:xs)[1]) = palabraMasLarga (eliminarPrimeraPalabra(x:xs))
    | otherwise = palabraMasLarga (primeraPalabra (x:xs) : eliminarPrimeraPalabra(eliminarPrimeraPalabra(x:xs)))

--ej 8
multiplicarFilas :: [[Integer]] -> [Integer]
multiplicarFilas [] = []
multiplicarFilas (x:xs) = multiplicar x : multiplicarFilas xs

multiplicar :: [Integer] -> Integer
multiplicar [x] = x
multiplicar (x:xs)= x* (multiplicar xs)

--ej 8.2
cantidadDeApariciones :: Integer -> [[Integer]] -> Integer
cantidadDeApariciones _ [] = 0
cantidadDeApariciones a (x:xs) = aparicionesLista a x + cantidadDeApariciones a xs

aparicionesLista :: Integer -> [Integer] -> Integer
aparicionesLista a [] = 0
aparicionesLista a (x:xs)
    | a == x = 1 + aparicionesLista a xs
    | otherwise = aparicionesLista a xs