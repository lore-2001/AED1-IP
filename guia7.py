#ej 1.1
def pertenece1 (s: list[int],e:int) -> bool:
    res:bool = False
    for elemento in s:
        if e==elemento:
            res = True
    return res
        
def pertenece2 (s: list[int],e:int) -> bool:
    i:int = 0
    res:bool = False
    while i < len(s):
        if e==s[i]:
            res=True
        i += 1
    return res

def pertenece3 (s: list[int],e:int) -> bool:
    res:bool = False
    for i in range(0,len(s),1):
        if e == s[i]:
            res = True
    return res

#ej 1.2
def divide_a_todos (s:list[int], e:int) -> bool:
    res = True
    for i in range (0,len(s),1):
        if s[i] % e != 0:
            res = False
    return res

#ej 1.3
def suma_total (s:list[int]) -> int:
    suma:int = 0
    for elemento in s:
        suma += elemento
    return suma

#ej 1.4
def maximo (s:list[int]) -> int:
    maximo_hasta_ahora = s[0]
    for elemento in s:
        if elemento > maximo_hasta_ahora:
            maximo_hasta_ahora = elemento
    return maximo_hasta_ahora

#ej 1.5
def minimo (s:list[int]) -> int:
    minimo_hasta_ahora = s[0]
    for elemento in s:
        if elemento < minimo_hasta_ahora:
            minimo_hasta_ahora = elemento
    return minimo_hasta_ahora

#ej 1.6
def ordenados (s:list[int]) -> bool:
    res = True
    for i in range (0,len(s)-1,1):
        if not s[i] <s[i+1]:
            res = False
    return res

#ej 1.7
def pos_maximo (s:list[int]) -> int:
    if len(s)==0:
        res=-1
    else:
        res = primera_aparicion(s,maximo(s))
    return res

def primera_aparicion (s:list[int],numero:int) -> int: #asume que sí aparece
    for i in range (0,len(s),1):
        if numero == s[i]:
            return i

#ej 1.8
def pos_minimo (s:list[int]) -> int:
    if len(s) == 0:
        res = -1
    else:
        res = ultima_aparicion(s,minimo(s))
    return res

def ultima_aparicion(s:list[int],numero:int) -> int: #tmb asume que sí aparece
    ultima_aparicion_hasta_ahora = primera_aparicion (s,numero)
    for i in range (0,len(s),1):
        if numero == s [i]:
            ultima_aparicion_hasta_ahora = i
    return ultima_aparicion_hasta_ahora
    #otra posible implementación sería hacer primera_aparicion con la lista dada vuelta

#ej 1.9
def long_mayorASiete (s:list[str]) -> bool:
    res = False
    for i in range (0,len(s),1):
        if len(s[i]) > 7:
            res = True
    return res
        
#ej 1.10
def es_palindroma(s:str) -> bool:
    if s == da_vuelta_str(s):
        return True
    else:
        return False

#ej 1.11
def iguales_consecutivos (s:list[int]) -> bool:
    res = False
    for i in range (0,len(s)-2):
        if s[i]==s[i+1]==s[i+2]:
            res=True
    return res

#ej 1.12
def vocales_distintas (s:str) -> bool:
    if len(vocales_usadas(s))>=3:
        return True
    else:
        return False

def vocales_usadas (s:str) -> set[chr]:
    vocales = set()
    if "a" in s:
        vocales.add("a")
    if "e" in s:
        vocales.add("e")
    if "i" in s:
        vocales.add("i")
    if "o" in s:
        vocales.add("o")
    if "u" in s:
        vocales.add("u")
    return vocales

def lista_vocales_usadas (s:str) -> list[chr]: #opción sin usar conjuntos (no los vimos)
    vocales = []
    if "a" in s and "a" not in vocales:
        vocales.append("a")
    if "e" in s and "e" not in vocales:
        vocales.append("e")
    if "i" in s and "i" not in vocales:
        vocales.append("i")
    if "o" in s and "o" not in vocales:
        vocales.append("o")
    if "u" in s and "u" not in vocales:
        vocales.append("u")
    return vocales

#ej 1.13
def pos_secuencia_ordenada_mas_larga (s:list[int]) -> int:
    largo_mas_larga = 1
    largo_provisorio = 1
    res = 0
    for i in range (0,len(s)-1,1):
        if s[i]<=s[i+1]:
            largo_provisorio+=1
            if largo_provisorio > largo_mas_larga:
                largo_mas_larga = largo_provisorio
                res=i+2-largo_provisorio
        else:
            largo_provisorio = 1
    return res

#ej 1.14
def cantidad_digitos_impares (s:list[int]) -> int:
    listaDeImparesPresentes = []
    for elemento in s:
        for impar in obtenerelementosimpares(elemento):
            listaDeImparesPresentes.append(impar)
    return len(listaDeImparesPresentes)

def obtenerelementosimpares (numero:int) -> list[str]:
    digitosImpares:list[str] = ["1","3","5","7","9"]
    ImparesEnNumero = []
    strdelnumero: str = str(numero)
    for elemento in strdelnumero:
        if elemento in digitosImpares:
            ImparesEnNumero.append(elemento)
    return ImparesEnNumero

#ej 2.1

def CerosEnPosicionesPares (s:list[int]):
    for i in range (0,len(s),2):
        s[i]=0

#ej 2.2
def CerosEnPosicionesPares2 (s:list[int]) -> list[int]:
    lista=s #otra forma es crear una lista vacía y hacer append(0) en los lugares pares y append(s[i]) en los lugares impares
    for i in range (0,len(lista),2):
        lista[i]=0
    return lista

#ej 2.3 
def sin_vocales (s:str)->str:
    palabraSinVocales:str = ""
    vocales=["a","e","i","o","u"]
    for letra in s:
        if letra not in vocales:
            palabraSinVocales += letra
    return palabraSinVocales

#ej 2.4
def reemplaza_vocales (s:str) -> str:
    vocales=["a","e","i","o","u"]
    palabranueva=""
    for letra in s:
        if letra in vocales:
            palabranueva += "_"
        else:
            palabranueva += letra
    return palabranueva

#ej 2.5 
def da_vuelta_str (s:str) -> str:
    res:str = ""
    for i in range (len(s)-1,-1,-1):
        res = res + s[i]
    return res

#ej 2.6
def eliminar_repetidos (s:str) -> str:
    palabranueva: str = ""
    for letra in s:
        if letra not in palabranueva:
            palabranueva += letra
    return palabranueva

#ej 3
def resultadoMateria (notas:list[int]) -> int:
    if promedio(notas) < 4:
        res = 3
    if promedio(notas) >= 4 and promedio(notas) < 7:
        res = 2
        for elemento in notas:
            if elemento < 4:
                res = 3
    if promedio(notas) >= 7:
        res = 1
        for elemento in notas:
            if elemento < 4:
                res = 3
    return res

def promedio (notas:list[int]) -> int:
    return (suma_total(notas)/len(notas))

#ej 4
def saldoActual (movimientos:list[(str,int)]) -> int:
    saldo:int = 0
    for elemento in movimientos:
        if elemento[0]=="I":
            saldo += elemento[1]
        if elemento[0]=="R":
            saldo -= elemento[1]
    return saldo

#ej 5
def pertenece_a_cada_uno (s:list[list[int]],e:int) -> list[bool]:
    res:list[bool] = []
    for fila in s:
        if pertenece1 (fila,e):
            res.append(True)
        else:
            res.append(False)
    return res

#ej 6.1
def es_matriz (s:list[list[int]]) -> bool: 
    if s == []:
        res = False
    else:
        largoprimerafila : int = len(s[0])
        if largoprimerafila == 0:
            res= False
        else:
            res = True
    for fila in s:
        if len(fila) != largoprimerafila:
            res = False
    return res

#ej 6.2
def filas_ordenadas(m:list[list[int]]) -> list[bool]:
    res : list[bool] = []
    for fila in m:
        if ordenados (fila):
            res.append(True)
        else:
            res.append(False)
    return res

#ej 6.3
def columna (m:list[list[int]],c:int) -> list[int]:
    res : list [int] = []
    for fila in m:
        res.append(fila[c])
    return res

#ej 6.4
def columnas_ordenadas (m:list[list[int]]) -> list[bool]:
    res : list[bool] = []
    matriz_ordenada_por_columnas : list[list[int]] = []
    for i in range(0,len(m[0]),1):
        matriz_ordenada_por_columnas.append(columna(m,i))
    for column in matriz_ordenada_por_columnas:
        if ordenados (column):
            res.append(True)
        else:
            res.append(False)
    return res

#ej. 6.5
def transponer (m:list[list[int]]) -> list[list[int]]:
    matriz_ordenada_por_columnas : list[list[int]] = []
    for i in range(0,len(m[0]),1):
        matriz_ordenada_por_columnas.append(columna(m,i))
    return matriz_ordenada_por_columnas

#ej 6.6
def quien_gana_tateti (m:list[list[chr]]) -> int:
    res = 2
    for fila in m:
        if fila == ["x","x","x"]:
            res = 1
        if fila == ["o","o","o"]:
            res = 0
    for column in transponer(m):
        if column == ["x","x","x"]:
            res = 1
        if column == ["o","o","o"]:
            res = 0
    if m[0][0] == "x" and m[1][1] == "x" and m[2][2] == "x":
        res = 1
    if m[0][2] == "x" and m[1][1] == "x" and m[2][0] == "x":
        res = 1
    if m[0][0] == "o" and m[1][1] == "o" and m[2][2] == "o":
        res = 0
    if m[0][2] == "o" and m[1][1] == "o" and m[2][0] == "o":
        res = 0
    return res

#ej 7.1 PREGUNTAR COMO TESTEAR FUNCIONES CON INPUT!!
def nombres_estudiantes () -> list[str]:
    listadenombres : list[str] = []
    nombres : str = input("ingrese un nombre. para finalizar, ingrese 'listo' o presione ENTER ")
    while nombres != "listo" and nombres != "":
        listadenombres.append(nombres)
        nombres = input("ingrese un nombre. para finalizar, ingrese 'listo' o presione ENTER ")
    return listadenombres

#ej 7.2
def historial_monedero () -> list[(str,int)]:
    historial : list[(str,int)] = []
    opciones: str = input("ingrese 'C' para cargar créditos, 'D' para descontar créditos o 'X' para finalizar ")
    while opciones != "X":
        cargar_o_descontar: str = opciones
        monto:int = input("ingrese el monto ")
        historial.append((cargar_o_descontar,monto))
        opciones: str = input("ingrese 'C' para cargar créditos, 'D' para descontar créditos o 'X' para finalizar ")
    return historial

#ej 7.3 CONSULTAR SI SE PUEDE HACER SIN BREAK
import random
def siete_y_medio ():
    cartas_posibles : list[int] = [1,2,3,4,5,6,7,10,11,12]
    suma_hasta_ahora :int = 0
    carta = random.choice(cartas_posibles)
    historial = [carta]
    if carta == 10 or carta == 11 or carta == 12:
        suma_hasta_ahora += 0.5*carta
    else:
        suma_hasta_ahora += carta
    print ("su carta es " + str(carta) + ". su suma hasta ahora es " + str(suma_hasta_ahora))
    if suma_hasta_ahora >= 7.5:
        print ("perdió el juego. su carta fue " + str(historial))
    else:
        eleccion: str = input("ponga 'S' si quiere sacar otra carta y 'N' si no ")
        while eleccion == "S":
                carta = random.choice(cartas_posibles)
                historial.append(carta)
                if carta == 10 or carta == 11 or carta == 12:
                    suma_hasta_ahora += 0.5*carta
                else:
                    suma_hasta_ahora += carta
                print ("su carta es " + str(carta) + ". su suma hasta ahora es " + str(suma_hasta_ahora))
                if suma_hasta_ahora >= 7.5:
                    print ("perdió el juego. sus cartas fueron " + str(historial))
                    break
                else:
                    eleccion: str = input("ponga 'S' si quiere sacar otra carta y 'N' si no ")
        if eleccion == "N":
            print ("eligió terminar. su puntaje es " + str(suma_hasta_ahora) + ". sus cartas fueron " + str(historial))

#ej 7.4 ¿está bien que no haya parámetro de entrada?
def fortaleza_contraseña () -> str:
    contraseña: str = input("ingrese su contraseña ")
    if len(contraseña) < 5:
        res = "ROJA"
    elif len(contraseña) > 8:
        if tienemayus(contraseña) and tieneminus(contraseña) and tienedigito(contraseña):
            res = "VERDE"
        else:
            res = "AMARILLA"
    else: 
        res = "AMARILLA"
    return res

def tienemayus(palabra:str) -> bool:
    res = False
    mayus = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
    for letra in palabra:
        if letra in mayus:
            return True
    return res

def tieneminus(palabra:str) -> bool:
    res = False
    minus = "abcdefghijklmnopqrstuvwxyz"
    for letra in palabra:
        if letra in minus:
            return True
    return res

def tienedigito(palabra:str) -> bool:
    res = False
    digitos = "0123456789"
    for letra in palabra:
        if letra in digitos:
            return True
    return res
