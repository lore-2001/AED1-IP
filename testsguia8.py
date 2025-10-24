import unittest
from guia8 import *
from queue import Queue as Cola, LifoQueue as Pila

class test_generar_nros_al_azar(unittest.TestCase):
    def test_cantidadcero(self):
        cantidad = 0
        desde = 0
        hasta = 10
        pila = generar_nros_al_azar(cantidad,desde,hasta)
        self.assertTrue(pila.empty())
    def test_cantidad10(self):
        cantidad=10
        desde= 0
        hasta = 10
        pila = generar_nros_al_azar(cantidad,desde,hasta)
        self.assertEqual(pila.qsize(),cantidad)
    def test_elementosentre10y20(self):
        cantidad = 10
        desde = 10
        hasta = 20
        pila = generar_nros_al_azar(cantidad,desde,hasta)
        while not pila.empty():
            numero = pila.get()
            self.assertIn(numero, range(desde, hasta + 1))

class test_cantidad_elementos(unittest.TestCase):
    def test_vacia(self):
        p = Pila()
        self.assertEqual(cantidad_elementos(p),0)
    def test_cuatroelementos(self):
        p = Pila()
        p.put(1)
        p.put(2)
        p.put(1)
        p.put(2)
        self.assertEqual(cantidad_elementos(p),p.qsize())

class test_buscar_nota_maxima(unittest.TestCase):
    def test_unicoelemento(self):
        p = Pila()
        p.put(("a",10))
        self.assertEqual(buscar_nota_maxima(p),("a",10))
    def varioselementos(self):
        p = Pila()
        p.put(("b",5))
        p.put(("a",10))
        p.put(("c",3))
        self.assertEqual(buscar_nota_maxima(p),("a",10))

class test_buscar_el_maximo(unittest.TestCase):
    def test_unsoloelemento (self):
        p = Pila()
        p.put(1)
        maximo = 1
        self.assertEqual(buscar_el_maximo(p),maximo)
    def test_varioselementos (self):
        p = Pila()
        p.put(1)
        p.put(5)
        p.put(3)
        p.put(1)
        self.assertEqual(buscar_el_maximo(p),5)

class test_esta_bien_balanceada(unittest.TestCase):
    def test_bienbalanceada1(self):
        l = "1+(2*3-(20/5))"
        self.assertTrue(esta_bien_balanceada(l))
    def test_bienbalanceada2(self):
        l="10*(1+(2*(-1)))"
        self.assertTrue(esta_bien_balanceada(l))
    def test_malbalanceada(self):
        l="1+)2*3(()"
        self.assertFalse(esta_bien_balanceada(l))
    def test_sinparentesis(self):
        l="1+2+3"
        self.assertTrue(esta_bien_balanceada(l))

class test_evaluar_expresion(unittest.TestCase):
    def test_ejemplo(self):
        exp = "3 4 + 5 * 2 -"
        self.assertEqual(evaluar_expresion(exp),33)
    def test_conmasdeundigito(self):
        exp = "40 20 - 5 + 5 / 20 *"
        self.assertEqual(evaluar_expresion(exp),100)

class test_intercalar(unittest.TestCase):
    def test_random(self):
        p1 = Pila()
        p1.put(3)
        p1.put(2)
        p1.put(1)
        p2 = Pila()
        p2.put(6)
        p2.put(5)
        p2.put(4)
        l = [1,4,2,5,3,6]
        self.assertEqual(convertir_pila_a_lista(intercalar(p1,p2)),l)

class test_generar_nros_al_azarCola(unittest.TestCase):
    def test_cantidadcero(self):
        cantidad = 0
        desde = 0
        hasta = 10
        cola = generar_nros_al_azarCola(cantidad,desde,hasta)
        self.assertTrue(cola.empty())
    def test_cantidad10(self):
        cantidad=10
        desde= 0
        hasta = 10
        cola = generar_nros_al_azarCola(cantidad,desde,hasta)
        self.assertEqual(cola.qsize(),cantidad)
    def test_elementosentre10y20(self):
        cantidad = 10
        desde = 10
        hasta = 20
        cola = generar_nros_al_azarCola(cantidad,desde,hasta)
        while not cola.empty():
            numero = cola.get()
            self.assertIn(numero, range(desde, hasta + 1))

class test_cantidad_elementosCOla(unittest.TestCase):
    def test_vacia(self):
        p = Cola()
        self.assertEqual(cantidad_elementosCola(p),0)
    def test_cuatroelementos(self):
        p = Cola()
        p.put(1)
        p.put(2)
        p.put(1)
        p.put(2)
        self.assertEqual(cantidad_elementosCola(p),p.qsize())

class test_buscar_el_maximoCola(unittest.TestCase):
    def test_unsoloelemento (self):
        p = Cola()
        p.put(1)
        maximo = 1
        self.assertEqual(buscar_el_maximoCola(p),maximo)
    def test_varioselementos (self):
        p = Cola()
        p.put(1)
        p.put(5)
        p.put(3)
        p.put(1)
        self.assertEqual(buscar_el_maximoCola(p),5)

class test_buscar_nota_minima(unittest.TestCase):
    def test_unicoelemento(self):
        p = Cola()
        p.put(("a",10))
        self.assertEqual(buscar_nota_minima(p),("a",10))
    def varioselementos(self):
        p = Cola()
        p.put(("b",5))
        p.put(("a",10))
        p.put(("c",3))
        self.assertEqual(buscar_nota_minima(p),("c",3))

class test_intercalarCola(unittest.TestCase):
    def test_random(self):
        p1 = Cola()
        p1.put(1)
        p1.put(3)
        p1.put(5)
        p2 = Cola()
        p2.put(2)
        p2.put(4)
        p2.put(6)
        l = [1,2,3,4,5,6]
        self.assertEqual(convertir_cola_a_lista(intercalarCola(p1,p2)),l)

class test_bingo (unittest.TestCase):
    def test_ganaen12(self):
        bolillero = Cola()
        carton = []
        for i in range (0,12,1):
            bolillero.put(i)
            carton.append(i)
        self.assertEqual(jugar_carton_de_bingo(carton,bolillero),12)
    def test_ganaen50(self):
        bolillero = Cola()
        carton = []
        for i in range (49,-1,-1):
            bolillero.put(i)
        for i in range (0,12,1):
            carton.append(i)
        self.assertEqual(jugar_carton_de_bingo(carton,bolillero),50)

class test_pacientes_urgentes(unittest.TestCase):
    def test_sinpacientesurgentes(self):
        c = Cola()
        c.put((10,"a","b"))
        c.put((7,"v","d"))
        self.assertEqual(pacientes_urgentes(c),0)
    def test_2pacientesurgentes(self):
        c = Cola()
        c.put((10,"a","b"))
        c.put((7,"v","d"))
        c.put((2,"a","s"))
        c.put((3,"k","d"))
        self.assertEqual(pacientes_urgentes(c),2)
    def test_todosurgentes(self):
        c = Cola()
        c.put((2,"a","s"))
        c.put((3,"k","d"))
        self.assertEqual(pacientes_urgentes(c),2)

class test_atencion_a_clientes(unittest.TestCase):
    def test_sin_prioridad(self):
        c = Cola()
        c.put(("a",1,False,False))
        c.put(("b",1,False,False))
        l = [("a",1,False,False),("b",1,False,False)]
        self.assertEqual(convertir_cola_a_lista(atencion_a_clientes(c)),l)
    def test_random(self):
        c = Cola()
        c.put(("a",1,False,False))
        c.put(("b",1,False,False))
        c.put(("c",1,False,True))
        c.put(("d",1,True,True))
        c.put(("e",1,False,False))
        c.put(("f",1,True,False))
        c.put(("g",1,False,True))
        l = [("c",1,False,True),("d",1,True,True),("g",1,False,True),("f",1,True,False),("a",1,False,False),("b",1,False,False),("e",1,False,False)]
        self.assertEqual(convertir_cola_a_lista(atencion_a_clientes(c)),l)

class test_promedio_diccionarios(unittest.TestCase):
    def test_vacio(self):
        l=[]
        d={}
    def test_unsoloestudiante(self):
        l = [("a",10),("a",8)]
        d = {"a":9}
        self.assertEqual(calcular_promedio_por_estudiante(l),d)
    def test_dosestudiantesyunasolanota(self):
        l=[("a",9),("b",5)]
        d= {"a":9,"b":5}
    def test_variosestudiantesmezclados(self):
        l = [("a",10),("b",10),("a",7),("c",6),("b",4),("a",10)]
        d = {"a":9,"b":7,"c":6}
        self.assertEqual(calcular_promedio_por_estudiante(l),d)

class test_visitar_sitio(unittest.TestCase):
    def test_agregounusuario(self):
        historial = {}
        visitar_sitio(historial,"pablo","google")
        historialdepablo=[]
        while historial["pablo"].empty()==False:
            historialdepablo.append(historial["pablo"].get())
        self.assertEqual(historialdepablo,["google"])
    def test_agregousuarioyvariositems(self):
        historial = {}
        visitar_sitio(historial,"pablo","google")
        visitar_sitio(historial,"pablo","facebook")
        visitar_sitio(historial,"pablo","google")
        historialdepablo=[]
        while historial["pablo"].empty()==False:
            historialdepablo.append(historial["pablo"].get())
        self.assertEqual(historialdepablo,["google","facebook","google"])
    def test_variosusuarios(self):
        piladejose= Pila()
        piladejose.put("facebook")
        historial = {"jose":piladejose}
        visitar_sitio(historial,"pablo","google")
        visitar_sitio(historial,"pablo","facebook")
        visitar_sitio(historial,"jose","tumblr")
        visitar_sitio(historial,"pablo","google")
        historialdepablo=[]
        while historial["pablo"].empty()==False:
            historialdepablo.append(historial["pablo"].get())
        historialdejose=[]
        while historial["jose"].empty()==False:
            historialdejose.append(historial["jose"].get())
        self.assertEqual(historialdepablo,["google","facebook","google"])
        self.assertEqual(historialdejose,["tumblr","facebook"])

class test_navegar_atras(unittest.TestCase):
    def test_random(self):
        piladejose= Pila()
        piladejose.put("facebook")
        historial = {"jose":piladejose}
        visitar_sitio(historial,"pablo","google")
        visitar_sitio(historial,"pablo","facebook")
        visitar_sitio(historial,"jose","tumblr")
        visitar_sitio(historial,"pablo","google")
        self.assertEqual(navegar_atras(historial,"jose"),"tumblr")
        self.assertEqual(navegar_atras(historial,"pablo"),"google")

class test_agregar_producto(unittest.TestCase):
    def test_random(self):
        inventario = {"remeras":{"precio":50,"cantidad":30}}
        agregar_producto(inventario,"pantalones",500,2)
        inventario_esperado={"remeras":{"precio":50,"cantidad":30},"pantalones":{"precio":500,"cantidad":2}}
        self.assertEqual(inventario,inventario_esperado)

class test_actualizar_stock(unittest.TestCase):
    def test_random(self):
        inventario = {"remeras":{"precio":50,"cantidad":30}}
        actualizar_stock(inventario,"remeras",2)
        resultado_esperado = {"remeras":{"precio":50,"cantidad":2}}
        self.assertEqual(inventario,resultado_esperado)

class test_actualizar_precio(unittest.TestCase):
    def test_random(self):
        inventario = {"remeras":{"precio":50,"cantidad":30}}
        actualizar_precio(inventario,"remeras",300)
        resultado_esperado = {"remeras":{"precio":300,"cantidad":30}}
        self.assertEqual(inventario,resultado_esperado)

class test_calcular_valor_inventario(unittest.TestCase):
    def test_random(self):
        inventario={"remeras":{"precio":50,"cantidad":30},"pantalones":{"precio":500,"cantidad":2}}
        self.assertEqual(calcular_valor_inventario(inventario),2500)

import os
class test_contar_lineas(unittest.TestCase):
    def test_vacio(self):
        ruta_archivo = os.path.join("archivos txt para test","contar_lineas_caso_vacio")
        archivo = open(ruta_archivo, "w")
        archivo.close()
        resultado = contar_lineas(ruta_archivo)
        os.remove(ruta_archivo)
        self.assertEqual(resultado, 0)       
    def test_caso3lineas(self):
        ruta_archivo =os.path.join("archivos txt para test","contar_lineas_3_lineas")
        archivo = open(ruta_archivo,"w")
        archivo.write("a\n hola \n hola")
        archivo.close()
        resultado = contar_lineas(ruta_archivo)
        os.remove(ruta_archivo)
        self.assertEqual(resultado,3)

class test_existe_palabra (unittest.TestCase):
    def test_vacio(self):
        ruta_archivo = os.path.join("archivos txt para test","existe_palabra_vacio")
        archivo = open(ruta_archivo,"w")
        archivo.close()
        resultado = existe_palabra(ruta_archivo,"palabra")
        os.remove(ruta_archivo)
        self.assertFalse(resultado)
    def test_lapalabranoesta(self):
        ruta_archivo = os.path.join("archivos txt para test","existe_palabra_holamundo")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola mundo")
        archivo.close()
        resultado= existe_palabra(ruta_archivo,"abc")
        os.remove(ruta_archivo)
        self.assertFalse(resultado)
    def test_lapalabraesta(self):
        ruta_archivo = os.path.join("archivos txt para test","existe_palabra_holamundo")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola mundo")
        archivo.close()
        resultado= existe_palabra(ruta_archivo,"mundo")
        os.remove(ruta_archivo)
        self.assertTrue(resultado)

class test_contar_apariciones(unittest.TestCase):
    def test_vacio(self):
        ruta_archivo = os.path.join("archivos txt para test","contar_apariciones_vacio")
        archivo = open(ruta_archivo,"w")
        archivo.close()
        resultado = cantidad_de_apariciones(ruta_archivo,"a")
        os.remove(ruta_archivo)
        self.assertEqual(resultado,0)
    def test_noaparece(self):
        ruta_archivo = os.path.join("archivos txt para test","contar_apariciones_texto")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola a todos \n hola como estan \n")
        archivo.close()
        resultado = cantidad_de_apariciones(ruta_archivo,"personas")
        os.remove(ruta_archivo)
        self.assertEqual(resultado,0)
    def test_apareceunavezporlinea(self):
        ruta_archivo = os.path.join("archivos txt para test","contar_apariciones_vacio")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola a todos \n hola como estan \n")
        archivo.close()
        resultado = cantidad_de_apariciones(ruta_archivo,"hola")
        os.remove(ruta_archivo)
        self.assertEqual(resultado,2)
    def test_aparecevariasveces(self):
        ruta_archivo = os.path.join("archivos txt para test","contar_apariciones_texto")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola a todos \n hola como estan \n hola hola hola \n")
        archivo.close()
        resultado = cantidad_de_apariciones(ruta_archivo,"hola")
        os.remove(ruta_archivo)
        self.assertEqual(resultado,5)
    def test_quepasaconlasletras(self):
        ruta_archivo = os.path.join("archivos txt para test","contar_apariciones_texto")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola a todos \n hola como estan \n")
        archivo.close()
        resultado = cantidad_de_apariciones(ruta_archivo,"a")
        os.remove(ruta_archivo)
        self.assertEqual(resultado,1)
        
class test_agrupar_por_longitud(unittest.TestCase):
    def test_vacio(self):
        ruta_archivo = os.path.join("archivos txt para test","agrupar_por_longitud_vacio")
        archivo = open(ruta_archivo,"w")
        archivo.close()
        resultado = agrupar_por_longitud(ruta_archivo)
        os.remove(ruta_archivo)
        self.assertEqual(resultado,{})
    def test_unasolalinea(self):
        ruta_archivo = os.path.join("archivos txt para test","agrupar_por_longitud_1")
        archivo = open(ruta_archivo,"w")
        archivo.write("123 12 1234")
        archivo.close()
        resultado = agrupar_por_longitud(ruta_archivo)
        os.remove(ruta_archivo)
        resultado_esperado = {2:1,3:1,4:1}
        self.assertEqual(resultado,resultado_esperado)
    def test_random(self):
        ruta_archivo = os.path.join("archivos txt para test","agrupar_por_longitud_random")
        archivo = open(ruta_archivo,"w")
        archivo.write("123 12 1234\n 1234 12345 123456789 12\n 12 123") 
        archivo.close()
        resultado = agrupar_por_longitud(ruta_archivo)
        os.remove(ruta_archivo)
        resultado_esperado = {2:3,3:2,4:2,5:1,9:1}
        self.assertEqual(resultado,resultado_esperado)

class test_la_palabra_mas_frecuente(unittest.TestCase):
    def test_unasolapalabra(self):
        ruta_archivo= os.path.join("archivos txt para test","la_palabra_mas_frecuente_1")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola")
        archivo.close()
        resultado = la_palabra_mas_frecuente(ruta_archivo)
        os.remove(ruta_archivo)
        self.assertEqual(resultado,"hola")
    def test_variaspalabras(self):
        ruta_archivo= os.path.join("archivos txt para test","la_palabra_mas_frecuente_varios")
        archivo = open(ruta_archivo,"w")
        archivo.write("hola a todos hola como estan")
        archivo.close()
        resultado = la_palabra_mas_frecuente(ruta_archivo)
        os.remove(ruta_archivo)
        self.assertEqual(resultado,"hola")
    def test_alfinaldelalinea(self):
        ruta_archivo= os.path.join("archivos txt para test","la_palabra_mas_frecuente_final")
        archivo = open(ruta_archivo,"w")
        archivo.write("a hola todos hola\n como estan")
        archivo.close()
        resultado = la_palabra_mas_frecuente(ruta_archivo)
        os.remove(ruta_archivo)
        self.assertEqual(resultado,"hola")

class test_clonar_sin_comentarios(unittest.TestCase):
    def test_vacio(self):
        ruta_archivo=os.path.join("archivos txt para test","clonar_sin_comentarios_vacio")
        archivo = open(ruta_archivo,"w")
        archivo.close()
        resultado = clonar_sin_comentarios(ruta_archivo,ruta_vacio)
        os.remove(ruta_archivo)
        ruta_vacio=os.path.join("archivos txt para test","clonar_sin_comentarios_vacio2")
        archivo_vacio = open(ruta_vacio,"w")
        archivo_vacio.close()
        vacio = archivo_vacio.readlines()
        os.remove(ruta_archivo)
        self.assertEqual(resultado,vacio)


if __name__ == '__main__':
    unittest.main(verbosity=2)
