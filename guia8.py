from queue import Queue as Cola, LifoQueue as Pila
import random

#ej 1.1
def generar_nros_al_azar (cantidad:int, desde:int, hasta:int) -> Pila[int]:
    res : Pila[int] = Pila()
    for i in range (0,cantidad,1):
        res.put(random.randint(desde,hasta))
    return res

#ej 1.2
def cantidad_elementos (p:Pila) -> int:
    pila_auxiliar: Pila = Pila()
    contador = 0
    while p.empty() == False:
        pila_auxiliar.put(p.get())
        contador +=1
    while pila_auxiliar.empty() == False:
        p.put(pila_auxiliar.get())
    return contador

#ej 1.3
def buscar_el_maximo (p:Pila[int]) -> int:
    pilaaux : Pila[int] = Pila()
    primer_elemento = p.get()
    pilaaux.put(primer_elemento)
    maximo = primer_elemento
    while p.empty() == False:
        siguiente_elemento = p.get()
        pilaaux.put(siguiente_elemento)
        if siguiente_elemento > maximo:
            maximo = siguiente_elemento
    while pilaaux.empty() == False:
        p.put(pilaaux.get())
    return maximo

#ej 1.4    
def buscar_nota_maxima (p:Pila[(str,int)]) -> (str,int):
    pilaaux : Pila[(str,int)] = Pila ()
    primer_elemento = p.get()
    pilaaux.put(primer_elemento)
    maximo_hasta_ahora = primer_elemento
    while p.empty() == False:
        siguiente_elemento = p.get()
        pilaaux.put(siguiente_elemento)
        if siguiente_elemento[1] > maximo_hasta_ahora[1]:
            maximo_hasta_ahora = siguiente_elemento
    while pilaaux.empty() == False:
        p.put(pilaaux.get())
    return maximo_hasta_ahora

#ej 1.5
def esta_bien_balanceada (s:str) -> bool:
    piladeparentesis: Pila[chr] = Pila()
    for elemento in s:
        if elemento == "(" or elemento == ")":
            piladeparentesis.put(elemento)
    contador_apertura: int = 0
    contador_cierre: int = 0
    pilaaux: Pila[chr] = Pila()
    for i in range(cantidad_elementos(piladeparentesis)):
        ultimo_elemento = piladeparentesis.get()
        if ultimo_elemento == "(":
            contador_apertura += 1
        if ultimo_elemento == ")":
            contador_cierre += 1
        pilaaux.put(ultimo_elemento)
    if contador_apertura != contador_cierre:
        res = False
    else:
        apertura_sin_pareja: int = 0
        for i in range (cantidad_elementos(pilaaux)):
            primer_elemento = pilaaux.get()
            if primer_elemento == "(":
                apertura_sin_pareja +=1
            if primer_elemento == ")":
                apertura_sin_pareja -=1
            if apertura_sin_pareja <0:
                return False
        if apertura_sin_pareja == 0:
            res= True
    return res
                
#ej 1.6
def evaluar_expresion (s:str) -> float:
    expresion_dividida: list[str] = dividir_en_tokens(s)
    operadores: list[str] = ["+","-","*","/"]
    pila_de_operandos: Pila(str) = Pila()
    for token in expresion_dividida:
        if token not in operadores:
            pila_de_operandos.put(token)
        else:
            primer_elemento = pila_de_operandos.get()
            segundo_elemento = pila_de_operandos.get()
            print(primer_elemento,segundo_elemento)
            resultado = 0
            if token == "+":
                resultado = float(primer_elemento) + float(segundo_elemento)
            if token == "*":
                resultado = float(primer_elemento) * float(segundo_elemento)
            if token == "-":
                resultado = float(segundo_elemento) - float(primer_elemento)
            if token == "/":
                resultado = float(segundo_elemento) / float(primer_elemento)
            pila_de_operandos.put(resultado)
    res = pila_de_operandos.get()
    return res

def dividir_en_tokens (s:str) -> list[str]:
    con_espacio_al_final: str = s + " "
    lista_dividida = []
    numero = ""
    for elemento in con_espacio_al_final:
        if elemento != " ":
            numero += elemento
        else:
            lista_dividida.append(numero)
            numero = ""
    return lista_dividida

#ej 1.7
def intercalar(p1:Pila,p2:Pila) -> Pila:
    res_al_reves: Pila = Pila()
    while p2.empty() == False:
        res_al_reves.put(p1.get())
        res_al_reves.put(p2.get())
    res : Pila = Pila()
    while res_al_reves.empty() == False:
        res.put(res_al_reves.get())
    return res

def convertir_pila_a_lista(p:Pila) -> list:
    lista = []
    while p.empty() == False:
        lista.append(p.get())
    return lista

#ej 2.8
def generar_nros_al_azarCola (cantidad:int, desde: int, hasta: int) -> Cola[int]:
    cola : Cola[int] = Cola()
    for i in range(cantidad):
        cola.put(random.randint(desde,hasta))
    return cola

#ej 2.9
def cantidad_elementosCola(c:Cola) -> int:
    contador:int = 0
    colaaux: Cola = Cola()
    while c.empty() == False:
        colaaux.put(c.get())
        contador +=1
    while colaaux.empty()==False:
        c.put(colaaux.get())
    return contador

#ej 2.10
def buscar_el_maximoCola (c:Cola[int]) -> int:
    maximo = c.get()
    c.put(maximo)
    for i in range (cantidad_elementos(c)):
        elemento = c.get()
        if elemento > maximo:
            maximo = elemento
        c.put(elemento)
    return maximo

#ej 2.11
def buscar_nota_minima(c:Cola[tuple[str,int]]) -> tuple[str,int]:
    minimo: (str,int) = c.get()
    c.put(minimo)
    for i in range(cantidad_elementosCola(c)-1):
        elemento = c.get()
        if elemento[1] < minimo[1]:
            minimo = elemento
        c.put(elemento)
    return minimo

#ej 2.12
def intercalarCola(c1:Cola,c2:Cola) -> Cola:
    res: Cola = Cola()
    for i in range (cantidad_elementosCola(c1)):
        elementodec1=c1.get()
        elementodec2=c2.get()
        res.put(elementodec1)
        res.put(elementodec2)
        c1.put(elementodec1)
        c2.put(elementodec2)
    return res

def convertir_cola_a_lista(c:Cola) -> list:
    res = []
    while c.empty()==False:
        res.append(c.get())
    return res

#ej 2.13.1
def armar_secuencia_de_bingo() -> Cola[int]:
    secuencia = Cola()
    for i in range (0,100,1):
        secuencia.put(i)
    secuencia = random.shuffle(secuencia)
    return secuencia

#ej 2.13.2
def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int]) -> int:
    carton_tachado: list[int] = []
    contador: int = 0
    while mismocarton(carton_tachado,carton) == False:
        bolilla = bolillero.get()
        contador +=1
        if bolilla in carton:
            carton_tachado.append(bolilla)
    return contador

def mismocarton (carton1: list[int],carton2:list[int]) -> bool:
    res = True
    if len(carton1) != len(carton2):
        res = False
    else:
        for numero in carton1:
            if numero not in carton2:
                res = False
        for numero in carton2:
            if numero not in carton1:
                res = False
    return res

#ej 2.14
def pacientes_urgentes(c:Cola[tuple[int,str,str]]) -> int:
    contador: int = 0
    for i in range (cantidad_elementosCola(c)):
        elemento= c.get()
        if elemento[0] <4:
            contador += 1
        c.put(elemento)
    return contador

#ej 2.15
def atencion_a_clientes(c:Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    orden_de_atencion = Cola()
    for i in range(cantidad_elementosCola(c)):
        elemento=c.get()
        if elemento[3]==True:
            orden_de_atencion.put(elemento)
            c.put(elemento)
        else:
            c.put(elemento)
    for i in range(cantidad_elementosCola(c)):
        elemento=c.get()
        if elemento[3] == False and elemento[2]==True:
            orden_de_atencion.put(elemento)
            c.put(elemento)
        else:
            c.put(elemento)
    for i in range(cantidad_elementosCola(c)):
        elemento=c.get()
        if elemento[3]==False and elemento[2]==False:
            orden_de_atencion.put(elemento)
            c.put(elemento)
        else:
            c.put(elemento)
    return orden_de_atencion

#ej 3.16
def calcular_promedio_por_estudiante (notas:list[tuple[str,float]]) -> dict[str,float]:
    diccionario_de_notas : dict [str,float]= {}
    diccionario_de_cant_materias: dict [str,float] = {}
    diccionario_de_promedios: dict[str,float] = {}
    for tupla in notas:
        if tupla[0] in diccionario_de_notas.keys():
            diccionario_de_notas[tupla[0]] += tupla[1]
            diccionario_de_cant_materias[tupla[0]] += 1
        else:
            diccionario_de_notas[tupla[0]] = tupla[1]
            diccionario_de_cant_materias[tupla[0]] = 1
    for alumno in diccionario_de_notas.keys():
        diccionario_de_promedios[alumno] = diccionario_de_notas[alumno] / diccionario_de_cant_materias[alumno]
    return diccionario_de_promedios

#ej 3.17
historiales: dict[str,Pila[str]] = {}
def visitar_sitio(historiales:dict[str,Pila(str)],usuario:str,sitio:str):
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        pila_de_sitios: Pila(str) = Pila()
        pila_de_sitios.put(sitio)
        historiales[usuario] = pila_de_sitios

def navegar_atras(historiales:dict[str,Pila(str)],usuario:str) -> str:
    ultimo_elemento=historiales[usuario].get()
    return ultimo_elemento 

#ej 3.18
def agregar_producto(inventario:dict[str,dict[str,int|float]],nombre:str,precio:float,cantidad:int):
    diccionario_del_producto: dict[str,int|float] = {}
    diccionario_del_producto["precio"] = precio
    diccionario_del_producto["cantidad"] = cantidad
    inventario[nombre]=diccionario_del_producto

def actualizar_stock(inventario:dict[str,dict[str,int|float]],nombre:str,cantidad:float):
    inventario[nombre]["cantidad"] = cantidad

def actualizar_precio(inventario:dict[str,dict[str,int|float]],nombre:str,precio:float):
    inventario[nombre]["precio"] = precio

def calcular_valor_inventario(inventario:dict[str,dict[str,int|float]]) -> float:
    total : int = 0
    for prenda in inventario.keys():
        total_prenda:int = inventario[prenda]["precio"] * inventario[prenda]["cantidad"]
        total += total_prenda
    return total

#ej 3.19
from typing import TextIO

def contar_lineas(nombre_archivo:str) -> int:
    archivo: TextIO = open(nombre_archivo,"r")
    lineas: list[str] = archivo.readlines()
    contador: int = len(lineas)
    archivo.close()
    return contador

def existe_palabra(nombre_archivo:str,palabra:str) -> bool:
    res = False
    archivo: TextIO = open(nombre_archivo, "r")
    linea = archivo.readline()
    while linea != "":
        if palabra in linea:
            archivo.close()
            return True
        linea: str = archivo.readline()
    archivo.close()
    return res

def cantidad_de_apariciones (nombre_archivo:str,palabra:str) -> int:
    archivo: TextIO = open(nombre_archivo,"r")
    contador: int = 0
    linea = archivo.readline()
    while linea != "":
        contador += contar_apariciones_por_linea(linea,palabra)
        linea = archivo.readline()
    archivo.close()
    return contador

def eliminar_salto_de_linea(linea: list[str]) -> list[str]:
    lista_sin_salto: list[str] = []
    ultima_palabra=linea[len(linea)-1]
    if ultima_palabra == "\n":
        for i in range(0,len(linea)-1,1):
            lista_sin_salto.append(linea[i])
    elif ultima_palabra[len(ultima_palabra)-1] == "\n":
        palabra_final = ""
        for i in range(len(ultima_palabra)-1):
                palabra_final += ultima_palabra[i]
        for i in range(0,len(linea)-1,1):
            lista_sin_salto.append(linea[i])
        lista_sin_salto.append(palabra_final)
    else:
        lista_sin_salto = linea
    return lista_sin_salto

def contar_apariciones_por_linea(linea:str,palabra:str) -> int:
    linea_separada_en_palabras:list[str] = separar_string_en_palabras(linea)
    linea_sin_cortes:list[str] = eliminar_salto_de_linea(linea_separada_en_palabras)
    contador:int = 0
    if palabra in linea_sin_cortes:
        contador += 1
    saco_la_palabra = eliminar_primera_aparicion(linea_sin_cortes,palabra)
    while palabra in saco_la_palabra:
        contador +=1
        saco_la_palabra = eliminar_primera_aparicion(saco_la_palabra,palabra)
    else:
        return contador

def separar_string_en_palabras(frase:str) -> list[str]:
    palabra_actual:str = ""
    lista_separada:list[str]=[]
    frase += " "
    for letra in frase:
        if letra != " ":
            palabra_actual += letra
        else:
            lista_separada.append(palabra_actual)
            palabra_actual=""          
    return lista_separada

def eliminar_primera_aparicion (lista: list[str],palabra:str) -> list[str]:
    lista_sin_palabra = []
    ya_vi_la_palabra = False
    for elemento in lista:
        if ya_vi_la_palabra:
            lista_sin_palabra.append(elemento)
        else:
            if elemento != palabra:
                lista_sin_palabra.append(elemento)
            else:
                ya_vi_la_palabra = True
    return lista_sin_palabra

#ej 3.20
def agrupar_por_longitud(nombre_archivo:str) -> dict[int,int]:
    archivo:TextIO = open(nombre_archivo,"r")
    lineas:list[str] = archivo.readlines()
    diccionario_de_longitudes: dict[int,int] = {}
    for linea in lineas:
        linea_separada_y_sin_cortes= eliminar_salto_de_linea(separar_string_en_palabras(linea))
        for elemento in linea_separada_y_sin_cortes:
            if len(elemento) in diccionario_de_longitudes.keys():
                diccionario_de_longitudes[len(elemento)] += 1
            elif len(elemento) not in diccionario_de_longitudes.keys() and len(elemento) != 0:
                diccionario_de_longitudes[len(elemento)] = 1
        linea = archivo.readline()
    archivo.close()
    return diccionario_de_longitudes

#ej 3.21
def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    diccionario_de_palabras: dict[str,int] = {}
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        linea_separada_y_sin_cortes = eliminar_salto_de_linea(separar_string_en_palabras(linea))
        for palabra in linea_separada_y_sin_cortes:
            if palabra in diccionario_de_palabras.keys():
                diccionario_de_palabras[palabra] += 1
            else:
                diccionario_de_palabras[palabra] = 1
    maximo = 0
    palabra_maxima = ""
    for palabra in diccionario_de_palabras.keys():
        if diccionario_de_palabras[palabra] >= maximo:
            maximo = diccionario_de_palabras[palabra]
            palabra_maxima = palabra
    return palabra_maxima #devuelve solo una, pero podría devolver todas si la especificacion fuera distinta

#ej 3.22
def clonar_sin_comentarios(nombre_archivo_entrada:str,nombre_archivo_salida:str):
    archivoentrada: TextIO = open(nombre_archivo_entrada,"r")
    clon: TextIO = open(nombre_archivo_salida,"w")
    lineas: list[str] = archivoentrada.readlines()
    for linea in lineas:
        linea_sin_espacios_iniciales = eliminar_espacios_iniciales(linea)
        if linea_sin_espacios_iniciales[0]!="#":
            clon.write(linea)
    archivoentrada.close()
               
def eliminar_espacios_iniciales(frase:str)->str:
    frase_sin_espacios: str = ""
    ya_vi_algun_caracter: bool = False
    for i in range(len(frase)):
        if ya_vi_algun_caracter:
            frase_sin_espacios += frase[i]
        else: 
            if frase[i] != " ":
                ya_vi_algun_caracter = True
                frase_sin_espacios += frase[i]
    return frase_sin_espacios

def eliminar_espacios_iniciales_recursion (frase:str) -> str:
    frase_sin_espacios=""
    if frase[0] == " ":
        for i in range (1,len(frase)):
            frase_sin_espacios += frase[i]
        return eliminar_espacios_iniciales_recursion(frase_sin_espacios)
    else:
        return frase

#ej 23
def invertir_lineas (nombre_archivo_entrada:str,nombre_archivo_salida:str):
    archivo:TextIO = open(nombre_archivo_entrada,"r")
    lineas_original:list[str] = archivo.readlines()
    archivo.close()
    nuevo_archivo:TextIO = open(nombre_archivo_salida,"w")
    for i in range(len(lineas_original)-1,-1,-1):
        nuevo_archivo.writelines(lineas_original[i])
    nuevo_archivo.close()

#ej 24
def agregar_frase_al_final(nombre_archivo:str,frase:str):
    archivo:TextIO = open(nombre_archivo,"r")
    lineas:list[str] = archivo.readlines()
    archivo.close()
    lineas.append(frase)
    archivo:TextIO = open(nombre_archivo,"w")
    for i in range(len(lineas)):
        archivo.writelines(lineas[i])
    archivo.close()

#ej 25
def agregar_frase_al_principio(nombre_archivo:str,frase:str):
    frase += "\n"
    nuevas_lineas:list[str]=[frase]
    archivo:TextIO=open(nombre_archivo,"r")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    for i in range(len(lineas)):
        nuevas_lineas.append(lineas[i])
    archivo:TextIO=open(nombre_archivo,"w")
    for i in range(len(nuevas_lineas)):
        archivo.writelines(nuevas_lineas[i])
    archivo.close()

#faltan 26 y 27