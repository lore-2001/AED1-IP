--ej 1
f :: Int -> Int
f 1 = 8
f 4 = 131
f 16 = 16

fGuardas :: Int -> Int
fGuardas x
    | x == 1 = 8
    | x == 4 = 131 
    | x == 16 = 16

g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

gGuardas :: Int -> Int
gGuardas x
    | x == 8 = 16
    | x == 16 = 4
    | x == 131 = 1

h :: Int -> Int
h x = f (g x)

k :: Int -> Int
k x = g (f x)

--ej 2
absoluto :: Int -> Int
absoluto x
    | x >= 0 = x
    | otherwise = (-1)*x

maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y
    | absoluto(x) >= absoluto (y) = absoluto(x)
    | otherwise = absoluto(y)

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z
    |(x >= y) && (x >= z) = x
    |(y >= x) && (y >= z) = y
    |(z >= x) && (z >= y) = z

algunoEsCero :: Float -> Float -> Bool
algunoEsCero x y
    | x == 0 || y == 0 = True
    | otherwise = False

algunoEsCeroPM :: Float -> Float -> Bool 
algunoEsCeroPM 0 y = True
algunoEsCeroPM x 0 = True
algunoEsCeroPM _ _ = False

ambosSonCero :: Float -> Float -> Bool
ambosSonCero x y
    | x == 0 && y == 0 = True
    | otherwise = False

ambosSonCeroPM :: Float -> Float -> Bool
ambosSonCeroPM 0 0 = True
ambosSonCeroPM x y = False

enMismoIntervalo :: Float -> Float -> String --se pueden anidar las guardas?
enMismoIntervalo x y
    | x <= 3 && y <= 3 = "mismo intervalo"
    | x <= 3 && y > 3 = "distinto intervalo"
    | 7 >= x && x > 3 && 7 >= y && y > 3 = "mismo intervalo"
    | (7 >= x && x > 3) && (y>7 || y <=3) = "distinto intervalo"
    | x>7 && y>7 = "mismo intervalo"
    | x>7 && y<= 7 = "distinto intervalo"

sumaDistintos :: Int -> Int -> Int -> Int --idem
sumaDistintos x y z
    | x /= y && x /= z && y /= z = x+y+z
    | x /= y && y==z = x+y
    | x==y && y/=z = y+z
    | x==z && y/=z = x+y
    | x==y && x==z = x

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y
    | (mod x y) == 0 = True
    | otherwise = False

digitoUnidades :: Int -> Int
digitoUnidades x = (mod (absoluto x) 10)

digitoDecenas :: Int -> Int
digitoDecenas x = digitoUnidades(div (absoluto x) 10)

--ej 3
estanRelacionados :: Int -> Int -> Bool --qué hago con k??
estanRelacionados a b 
{--True si a*a + a*b*k == 0 para k entero distinto de 0
True si a*(a+b*k)==0
True si a == 0 o (a+b*k==0)
                (a+b*k == 0) si a=b*-k, es decir si mod a b == 0 --}
   | a == 0 = True
   | mod a b == 0 = True
   | otherwise = False

--ej 4
productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (a,b) (c,d) = a*c + b*d

esParMenor :: (Float, Float) -> (Float, Float) -> (Bool, Bool)
esParMenor (a,b) (c,d)
    | a < c && b < d = (True, True)
    | a < c && not(b< d) = (True, False)
    | not(a<c) && b < d = (False, True)
    | otherwise = (False, False)

distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (a,b) (c,d) = sqrt((a-c)^2 + (b-d)^2)

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (a,b,c) = a+b+c

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int --se puede hacer con una variable auxiliar para no plantear todos los casos??
sumarSoloMultiplos (a,b,c) d
    | mod a d == 0 && mod b d == 0 && mod c d == 0 = a+b+c
    | mod a d == 0 && mod b d == 0 && mod c d /= 0 = a+b
    | mod a d == 0 && mod b d /= 0 && mod c d == 0 = a+c
    | mod a d /= 0 && mod b d == 0 && mod c d == 0 = b+c
    | mod a d == 0 && mod b d /= 0 && mod c d /= 0 = a
    | mod a d /= 0 && mod b d == 0 && mod c d /= 0 = b
    | mod a d /= 0 && mod b d /= 0 && mod c d == 0 = c
    | otherwise = 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (a,b,c)
    |mod a 2 == 0 = 0
    |mod b 2 == 0 = 1
    |mod c 2 == 0 = 2
    |otherwise = 4

crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)

invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)

type Punto2D = (Float, Float)
productoInterno2 :: Punto2D -> Punto2D -> Float
productoInterno2 (a,b) (c,d) = a*c + b*d

esParMenor2 :: Punto2D -> Punto2D -> (Bool, Bool)
esParMenor2 (a,b) (c,d)
    | a < c && b < d = (True, True)
    | a < c && not(b< d) = (True, False)
    | not(a<c) && b < d = (False, True)
    | otherwise = (False, False)

distancia2 :: Punto2D -> Punto2D -> Float
distancia2 (a,b) (c,d) = sqrt((a-c)^2 + (b-d)^2)

--ej 5
funcg :: Int -> Int
funcg n 
    |mod n 2 == 0 = div n 2
    |otherwise = 3*n + 1

funcf :: Int -> Int
funcf n 
    | n <= 7 = n^2
    | n > 7 = 2*n - 1

todosMenores :: (Int, Int, Int) -> Bool
todosMenores (a,b,c)
    |(funcf a > funcg a) && (funcf b > funcg b) && (funcf c > funcg c) = True
    | otherwise = False

--ej 6
type Anio = Int
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto n
    | mod n 4 /= 0 || (mod n 100 == 0 && mod n 400 /= 0) = False
    | otherwise = True

--ej 7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a,b,c) (d,e,f) = (absolutoFloat(a-d))+(absolutoFloat(b-e))+(absolutoFloat(c-f))

absolutoFloat :: Float -> Float
absolutoFloat x
    | x >= 0 = x
    | x < 0 = (-1)*x

type Punto3D = (Float, Float, Float)

distanciaManhattan2 :: Punto3D -> Punto3D -> Float
distanciaManhattan2 (a,b,c) (d,e,f) = (absolutoFloat(a-d))+(absolutoFloat(b-e))+(absolutoFloat(c-f))

--ej 8
sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = (mod (absoluto x) 10) + (mod (div (absoluto x) 10) 10)

comparar :: Int -> Int -> Int
comparar a b
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0
