--ej 1
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

--ej 2
parteEntera :: Float -> Int
parteEntera 0 = 0
parteEntera n 
    | n<1 && n>0 = 0
    | otherwise = 1 + parteEntera (n-1)

--ej 3
esDivisible :: Int -> Int -> Bool
esDivisible n m
    | n == m = True
    | n < m = False
    | n > m = esDivisible (n - m) m

--ej 4
sumaImpares :: Int -> Int
sumaImpares 1 = 1
sumaImpares n = 2*n-1 + sumaImpares (n-1)

--ej 5
medioFact :: Int -> Int
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n-2)

--ej 6
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n
    | n < 10 = True
    | n > 10 && mod n 10 /= mod (div n 10) 10 = False
    | otherwise = todosDigitosIguales (div n 10)

--ej 7 
iesimoDigito :: Int -> Int -> Int
iesimoDigito n i 
    | cantidadDigitos n == i = mod n 10
    | otherwise = iesimoDigito (div n 10) i

cantidadDigitos :: Int -> Int
cantidadDigitos n
    | n < 10 = 1
    | otherwise = 1 + cantidadDigitos (div n 10)

--ej 8
sumaDigitos :: Int -> Int
sumaDigitos n
    | n < 10 = n
    | otherwise = (mod n 10) + sumaDigitos (div n 10)

--ej 9
esCapicua :: Int -> Bool
esCapicua n
    | n < 10 = True
    | n > 10 && (mod n 10) /= (mod(reversaNumero n) 10) = False
    | otherwise = esCapicua (div (reversaNumero (div (reversaNumero n) 10)) 10) --hace esCapicua sin el primer y último dígito

esCapicuaSinRecursion :: Int -> Bool
esCapicuaSinRecursion n
    |n == reversaNumero n = True
    |otherwise = False
    
reversaNumero :: Int -> Int --no funciona si termina en 0. no importa tanto si voy a usarlo solo en la función esCapicua
reversaNumero n
    | n < 10 = n
    | otherwise = (mod n 10)*10^(cantidadDigitos n -1) + reversaNumero (div n 10)

--ej 10
f1 :: Int -> Int
f1 0 = 1
f1 n = 2^n + f1(n-1)

f2 :: Int -> Float -> Float
f2 1 q = q
f2 n q = q^n + f2 (n-1) q

f3 :: Int -> Float -> Float
f3 n q = f2 (n*2) q

f4 :: Int -> Float -> Float
f4 n q = f3 n q - f2 n q + q^n

--ej 11
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = 1/ fromIntegral(factorial n) + eAprox (n-1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n*factorial (n-1)

e::Float
e = eAprox 10

--ej 12
raizDe2Aprox :: Integer -> Float 
raizDe2Aprox n = aN n - 1

aN :: Integer -> Float
aN 1 = 2
aN n = 2 + 1/(aN (n-1))

--ej 13
f :: Int -> Int -> Int
f 1 m = f2F m 1
f n m = f2F m n + f (n-1) m

f2F :: Int -> Int -> Int
f2F 1 q = q
f2F n q = q^n + f2F (n-1) q 
--ej 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 m = sumaPotenciasM q 1 m
sumaPotencias q n m = sumaPotenciasM q n m + sumaPotencias q (n-1) m 

sumaPotenciasM :: Integer -> Integer -> Integer -> Integer
sumaPotenciasM q n 1 = q ^ (n+1)
sumaPotenciasM q n m = q ^ (n+m) + sumaPotenciasM q n (m-1)

-- ej 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumaRacionalesAux 1 m
sumaRacionales n m = sumaRacionalesAux n m + sumaRacionales (n-1) m

sumaRacionalesAux :: Integer -> Integer -> Float
sumaRacionalesAux n 1 = fromIntegral n
sumaRacionalesAux n m = (fromIntegral n / fromIntegral m) * sumaRacionalesAux n (m-1)

--ej 16
menorDivisor :: Int -> Int
menorDivisor n
    | n == 1 = 1
    | otherwise = menorDivisorDesde n 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde n d 
    | mod n d == 0 = d
    | otherwise = menorDivisorDesde n (d+1)

esPrimo :: Int -> Bool
esPrimo n
    | n == 1 = False
    | menorDivisor n == n = True
    | otherwise = False

sonCoprimos :: Int -> Int -> Bool
sonCoprimos n m 
    | mod n m == 0 || mod m n == 0 = False
    | menorDivisor n == menorDivisor m = False
    | otherwise = True --no funciona para el caso donde tienen divisores en comun pero no es el menor

nEsimoPrimo :: Int -> Int 
nEsimoPrimo n
    | n == 1 = 2
    | otherwise = siguientePrimo (nEsimoPrimo (n-1))

siguientePrimo :: Int -> Int
siguientePrimo n
    | esPrimo (n+1) == True = n+1
    | esPrimo (n+1) == False = siguientePrimo (n+1)

--ej 17
esFibonacci :: Int -> Bool
esFibonacci n = esFibonacciAux n 0

esFibonacciAux :: Int -> Int -> Bool
esFibonacciAux n i 
    | fibonacci i > n = False
    | fibonacci i == n = True
    | otherwise = esFibonacciAux n (i+1)

--ej 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n 
    | n < 10 && mod n 2 == 0 = n --si tiene un solo digito par, devuelve ese digito
    | n < 10 && mod n 2 /= 0 = -1 -- si tiene un solo digito impar, devuelve -1
    --si tiene más de un dígito:
    --ambos pares: se fija cuál es menor y hace mayorDigitoPar sobre el número con ese dígito extraido:
    | n >= 10 && mod (mod n 10) 2 == 0 && mod (mod (div n 10) 10) 2 == 0 && mod n 10 > (mod (div n 10) 10) = mayorDigitoPar(10*(div (div n 10) 10)+ mod n 10) 
    | n >= 10 && mod (mod n 10) 2 == 0 && mod (mod (div n 10) 10) 2 == 0 && mod n 10 <= (mod (div n 10) 10) = mayorDigitoPar(div n 10)
    --si uno es impar, lo saca y hace mayorDigitoPar con ese extraido:
    | n >= 10 && mod (mod n 10) 2 == 0 && mod (mod (div n 10) 10) 2 /= 0 = mayorDigitoPar (10*(div (div n 10) 10)+ mod n 10)
    | n >= 10 && mod (mod n 10) 2 /= 0 && mod (mod (div n 10) 10) 2 == 0 = mayorDigitoPar (div n 10)
    -- si ambos son impares, saca el último y hace mayorDigitoPar: (no saca los dos porque si eran los últimos dos llega a cero, que es par)
    | otherwise = mayorDigitoPar (div n 10)

--ej 19
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosAux n 1

esSumaInicialDePrimosAux :: Int -> Int -> Bool
esSumaInicialDePrimosAux n i
    | sumaPrimerosNPrimos i > n = False
    | sumaPrimerosNPrimos i == n = True
    | sumaPrimerosNPrimos i < n = esSumaInicialDePrimosAux n (i+1)

sumaPrimerosNPrimos :: Int -> Int 
sumaPrimerosNPrimos n
    | n == 1 = 2
    | otherwise = nEsimoPrimo n + sumaPrimerosNPrimos (n-1)

--ej 20 --??
--tomaValorMax :: Integer -> Integer -> Integer

--ej 21
-- pitagoras :: Integer -> Integer -> Integer -> Integer