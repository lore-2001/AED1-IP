#ej 1.1
def imprimir_hola_mundo ():
    print ("¡hola mundo!")

#imprimir_hola_mundo ()

#ej 1.2
def imprimir_un_verso ():
    print ("You said a problem's not a problem till you call it by name \n Pilot's still a pilot till he crashes the plane \n I swear I have control just like a universe expanding \n try not to think about landing")

#imprimir_un_verso()

#ej 1.3
import math
def raizDe2() -> float:
    return (round((math.sqrt(2)),4))

#print(raizDe2())

#ej 1.4 
def factorial_de_dos()-> int:
    return(math.factorial(2))

#print(factorial_de_dos())

#ej 1.5 
def perimetro () -> float:
    return (2*math.pi)

#print(perimetro())

#ej 2.1
def imprimir_saludo (nombre: str):
    print ("hola " + nombre)

#imprimir_saludo("lore")

def imprimir_saludo_dos (nombre:str):
    print ("hola", nombre)

#imprimir_saludo_dos ("lore")

#ej 2.2
def raiz_cuadrada_de (numero:float) -> float:
    return (math.sqrt(numero))

#print(raiz_cuadrada_de (81))

#ej 2.3 
def fahrenheit_a_celsius (t: float) -> float:
    return ((t-32)*5)/9

#print(fahrenheit_a_celsius(100))

#ej 2.4 
def imprimir_dos_veces(estribillo: str):
    print(estribillo*2)

#imprimir_dos_veces("hola \n a todos \n")

#ej 2.5
def es_multiplo_de (n:int, m:int) -> bool:
    if m % n == 0:
        return True
    else:
        return False

#print (es_multiplo_de (10,30))
#print (es_multiplo_de(10,35))

#ej 2.6 
def es_par (numero:int) -> bool:
    if es_multiplo_de (2, numero):
        return True
    else:
        return False

#print (es_par(24))
#print (es_par(25))

#ej 2.7 
def cantidad_de_pizzas(comensales:int,min_cant_de_porciones:int)-> int:
    if (round((comensales*min_cant_de_porciones)/8)) < ((comensales*min_cant_de_porciones)/8):
        return (round((comensales*min_cant_de_porciones)/8)) + 1
    else:
        return (round((comensales*min_cant_de_porciones)/8))

#print (cantidad_de_pizzas (2,3))
#print (cantidad_de_pizzas (2,1))
#print (cantidad_de_pizzas (4,5))

def pizzasConCeil(comensales:int,min_cant_de_porciones:int)-> int:
    return math.ceil ((comensales*min_cant_de_porciones)/8)

#print(pizzasConCeil(2,3))
#print(pizzasConCeil(2,1))
#print(pizzasConCeil(4,5))

#ej 3.1
def alguno_es_0 (numero1: float, numero2: float) -> bool:
    return (numero1==0 or numero2==0)

#print (alguno_es_0(1,2))
#print (alguno_es_0(1,0))
#print (alguno_es_0(0,2))
#print (alguno_es_0(0,0))

#ej 3.2
def ambos_son_cero (numero1:float,numero2:float)-> bool:
    return (numero1==0 and numero2==0)

#print (ambos_son_cero(0,0))
#print (ambos_son_cero(0,1))

#ej 3.3
def es_nombre_largo (nombre:str) -> bool:
    return (len(nombre)>=3 and len(nombre)<=8)

#print(es_nombre_largo("lore"))
#print(es_nombre_largo("lo"))
#print(es_nombre_largo("lorelorelore"))

#ej 3.4
def es_bisiesto (año:int)->bool:
    return (año%400==0 or (año%4==0 and not año%100==0))

#print (es_bisiesto(2028))
#print (es_bisiesto(2025))

#ej 4
def peso_pino (altura:float) -> float:
    primeros_tres_metros=0
    siguientes_metros=0
    if altura <= 3:
        primeros_tres_metros = 300*altura
    else: 
        primeros_tres_metros = 900
        siguientes_metros = 200*(altura-3)
    return primeros_tres_metros + siguientes_metros

#print(peso_pino(2))
#print(peso_pino(5))

def es_peso_util (peso:float)->bool:
    return (peso>=400 and peso<=1000)

#print(es_peso_util(500))
#print(es_peso_util(1500))
#print(es_peso_util(200))

def sirve_pino (altura:float) -> bool:
    return (es_peso_util(peso_pino(altura)))

#print(sirve_pino(2))
#print(sirve_pino(5))

#ej 5.1
def devolver_el_doble_si_es_par (numero:int) -> int:
    if es_par (numero):
        return numero*2
    else:
        return numero
    
#print(devolver_el_doble_si_es_par(2))
#print(devolver_el_doble_si_es_par(3))

def devolver_valor_si_es_par_sino_el_que_sigue (numero:int) -> int:
    if es_par (numero):
        return numero
    else:
        return numero+1
    
#print (devolver_valor_si_es_par_sino_el_que_sigue(2))
#print (devolver_valor_si_es_par_sino_el_que_sigue(3))

#ej 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero:int) -> int:
    if numero % 3 == 0:
        return 2*numero
    if numero % 9 == 0 :
        return 3*numero
    else:
        return numero
    
#print (devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18)) #devuelve 36, si hacía las guardas al revés devolvía 3*18

#ej 5.4 
def lindo_nombre (nombre: str) -> str:
    if len(nombre) >= 5:
        return "tu nombre tiene muchas letras"
    else:
        return "tu nombre tiene menos de 5 caracteres"
    
#print (lindo_nombre("lore"))
#print (lindo_nombre("lorena"))

#ej 5.5
def elRango (numero:float):
    if numero < 5 :
        print ("menor a 5")
    elif numero >=10 and numero<=20:
        print("entre 10 y 20")
    elif numero > 20: 
        print("mayor a 20")

#elRango(3)
#elRango(12)
#elRango(25)
#elRango(7)

#ej 5.6
def vacaciones_o_trabajo (sexo:str,edad:int):
    if edad<18:
        print ("andá de vacaciones")
    elif edad >= 60 and sexo == "F":
        print ("andá de vacaciones")
    elif edad >= 65 and sexo == "M":
        print ("andá de vacaciones")
    else: 
        print("te toca trabajar")

#(vacaciones_o_trabajo ("F",5))
#(vacaciones_o_trabajo ("M",5))
#(vacaciones_o_trabajo ("F",35))
#(vacaciones_o_trabajo ("M",35))
#(vacaciones_o_trabajo ("F",60))
#(vacaciones_o_trabajo ("M",60))
#(vacaciones_o_trabajo ("F",65))
#(vacaciones_o_trabajo ("M",65))

#ej 6.1
def primerosDiez ():
    contador = 1
    while contador <= 10:
        print (contador)
        contador += 1

#primerosDiez ()

#ej 6.2
def paresEntre10y40 ():
    contador = 10
    while contador <= 40:
        print (contador)
        contador += 2

#paresEntre10y40()

#ej 6.3 
def eco ():
    contador = 0
    while contador < 10:
        print ("eco")
        contador += 1

#eco()

#ej 6.4
def cuentaRegresiva (inicio:int):
    contador = inicio
    while contador >= 1:
        print (contador)
        contador -= 1
    if contador == 0:
        print ("despegue")

#cuentaRegresiva (6)

#ej 6.5
def viajes_en_el_tiempo (inicio:int, llegada:int):
    contador = inicio -1
    while contador >= llegada:
        print ("viajó 1 año al pasado, estamos en el año "+ str(contador))
        contador -= 1

#viajes_en_el_tiempo (2020,2016)

#ej 6.6 
def viaje_a_aristoteles (inicio:int):
    contador = inicio - 20
    while contador >= -384:
        print ("viajaste 20 años al pasado, es el año " + str(contador))
        contador -= 20

#viaje_a_aristoteles (-200)

#ej 7.1
def forPrimerosDiez ():
    for num in range (1,11,1):
        print (num)

#forPrimerosDiez()

#ej 7.2
def forDel10al40 ():
    for num in range (10,41,2):
        print (num)

#forDel10al40()

#ej 7.3
def forEco ():
    for i in range (1,11,1):
        print ("eco")

#forEco()

#ej 7.4
def forCuentaRegresiva (numero:int):
    for i in range (numero, 0, -1):
        print (i)
    print ("despegue")

#forCuentaRegresiva(6)

#ej 7.5
def forViajesEnElTiempo (inicio:int, llegada:int):
    for i in range (inicio-1,llegada-1,-1):
        print ("viajó un año en el pasado, estamos en el año " + str(i))

#forViajesEnElTiempo (2020,2015)

#ej 7.6 
def forAristoteles (inicio:int):
    for i in range (inicio-20,-385,-20):
        print ("viajaste 20 años al pasado, estamos en el " + str (i))

#forAristoteles (-200)