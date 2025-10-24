import unittest
from guia7 import *

class test_pertenece1(unittest.TestCase):
    def test_vacio(self):
        l = []
        self.assertFalse(pertenece1(l,1))
    def test_unicoelementoypertenece(self):
        l=[1]
        self.assertTrue(pertenece1(l,1))
    def test_unicoelementoynopertenece(self):
        l=[1]
        self.assertFalse(pertenece1(l,2))
    def test_varioselementosyeselprimero(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece1(l,1))
    def test_varioselementosyeselultimo(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece1(l,4))
    def test_varioselementosypertenece(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece1(l,3))
    def test_varioselementosynopertenece(self):
        l=[1,2,3,4]
        self.assertFalse(pertenece1(l,5))
    def test_varioselementosyperteneceyhayrepetidos(self):
        l=[1,2,3,4,2]
        self.assertTrue(pertenece1(l,2))

class test_pertenece2(unittest.TestCase):
    def test_vacio(self):
        l = []
        self.assertFalse(pertenece2(l,1))
    def test_unicoelementoypertenece(self):
        l=[1]
        self.assertTrue(pertenece2(l,1))
    def test_unicoelementoynopertenece(self):
        l=[1]
        self.assertFalse(pertenece2(l,2))
    def test_varioselementosyeselprimero(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece2(l,1))
    def test_varioselementosyeselultimo(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece2(l,4))
    def test_varioselementosypertenece(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece2(l,3))
    def test_varioselementosynopertenece(self):
        l=[1,2,3,4]
        self.assertFalse(pertenece2(l,5))
    def test_varioselementosyperteneceyhayrepetidos(self):
        l=[1,2,3,4,2]
        self.assertTrue(pertenece2(l,2))

class test_pertenece3(unittest.TestCase):
    def test_vacio(self):
        l = []
        self.assertFalse(pertenece3(l,1))
    def test_unicoelementoypertenece(self):
        l=[1]
        self.assertTrue(pertenece3(l,1))
    def test_unicoelementoynopertenece(self):
        l=[1]
        self.assertFalse(pertenece3(l,2))
    def test_varioselementosyeselprimero(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece3(l,1))
    def test_varioselementosyeselultimo(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece3(l,4))
    def test_varioselementosypertenece(self):
        l=[1,2,3,4]
        self.assertTrue(pertenece3(l,3))
    def test_varioselementosynopertenece(self):
        l=[1,2,3,4]
        self.assertFalse(pertenece3(l,5))
    def test_varioselementosyperteneceyhayrepetidos(self):
        l=[1,2,3,4,2]
        self.assertTrue(pertenece3(l,2))

class test_divide_a_todos(unittest.TestCase):
    def test_vacio (self):
        l = []
        self.assertTrue(divide_a_todos(l,1))
    def test_divide (self):
        l = [4,6,8]
        self.assertTrue(divide_a_todos(l,2))
    def test_nodivide(self):
        l = [1,2,3]
        self.assertFalse(divide_a_todos(l,2))

class test_suma_total(unittest.TestCase):
    def test_casovacio(self):
        s = []
        self.assertEqual(suma_total(s),0)
    def test_unelemento(self):
        s= [1]
        self.assertEqual (suma_total(s),1)
    def test_varioselementos(self):
        s=[1,2,3,4]
        self.assertEqual(suma_total(s),10)
    def test_algunosnegativos(self):
        s=[1,-1,2,-1]
        self.assertEqual(suma_total(s),1)
    def test_todosnegativos(self):
        s=[-1,-2,-3,-4]
        self.assertEqual(suma_total(s),-10)

class test_maximo(unittest.TestCase):
    def test_unelemento(self):
        l = [1]
        self.assertEqual(maximo(l),1)
    def test_varioselementosymaximoprimero(self):
        l=[4,3,2,1]
        self.assertEqual(maximo(l),4)
    def test_varioselementosymaximoultimo(self):
        l=[1,2,3,4]
        self.assertEqual(maximo(l),4)
    def test_varioselementosymaximoenelmedio(self):
        l=[-1,0,1,-2]
        self.assertEqual(maximo(l),1)

class test_minimo(unittest.TestCase):
    def test_unelemento(self):
        l = [1]
        self.assertEqual(minimo(l),1)
    def test_varioselementosyminimoprimero(self):
        l=[1,2,3,4]
        self.assertEqual(minimo(l),1)
    def test_varioselementosyminimoultimo(self):
        l=[4,3,2,1]
        self.assertEqual(minimo(l),1)
    def test_varioselementosyminimoenelmedio(self):
        l=[-1,0,1,-2]
        self.assertEqual(minimo(l),-2)

class test_ordenados(unittest.TestCase):
    def test_vacio(self):
        self.assertTrue(ordenados([]))
    def test_unelemento(self):
        l=[1]
        self.assertTrue(ordenados(l))
    def test_variosordenados(self):
        l=[1,3,5,6]
        self.assertTrue(ordenados(l))
    def test_variosdesordenados(self):
        l=[1,2,3,2]
        self.assertFalse(ordenados(l))

class test_pos_maximo(unittest.TestCase):
    def test_vacio(self):
        l=[]
        self.assertEqual(pos_maximo(l),-1)
    def test_unelemento(self):
        l=[1]
        self.assertEqual(pos_maximo(l),0)
    def test_varioselementossinrepetir(self):
        l=[1,2,3,2]
        self.assertEqual(pos_maximo(l),2)
    def test_varioselementosconmaxrepetido(self):
        l=[1,2,3,2,3,3]
        self.assertEqual(pos_maximo(l),2)

class test_pos_minimo(unittest.TestCase):
    def test_vacio(self):
        l=[]
        self.assertEqual(pos_minimo(l),-1)
    def test_unelemento(self):
        l=[1]
        self.assertEqual(pos_minimo(l),0)
    def test_varioselementossinrepetir(self):
        l=[1,2,3,0,2]
        self.assertEqual(pos_minimo(l),3)
    def test_varioselementosconminrepetido(self):
        l=[1,2,3,0,2,3,0,3]
        self.assertEqual(pos_minimo(l),6)

class test_long_mayorASiete(unittest.TestCase):
    def test_vacio(self):
        l=[]
        self.assertFalse(long_mayorASiete(l))
    def test_unosolomenora7 (self):
        l=["aca"]
        self.assertFalse(long_mayorASiete(l))
    def test_unosolomayora7(self):
        l=["abcdefghij"]
        self.assertTrue(long_mayorASiete(l))
    def test_variosningunomayora7(self):
        l=["termo", "gato", "tener", "jirafas"]
        self.assertFalse(long_mayorASiete(l))
    def test_variosyalgunomayora7(self):
        l=["termo", "gatosssss", "tener", "jirafas"]
        self.assertTrue(long_mayorASiete(l))

class test_es_palindroma(unittest.TestCase):
    def test_casovacio(self):
        self.assertTrue(es_palindroma(""))
    def test_unasolaletra(self):
        s = "a"
        self.assertTrue(es_palindroma(s))
    def test_palindromapar(self):
        s="abccba"
        self.assertTrue(es_palindroma(s))
    def test_palindromaimpar(self):
        s="abcba"
        self.assertTrue(es_palindroma(s))
    def test_nopalindroma(self):
        s="abcd"
        self.assertFalse(es_palindroma(s))

class test_iguales_consecutivos(unittest.TestCase):
    def test_casovacio(self):
        self.assertFalse(iguales_consecutivos([]))
    def test_casouno(self):
        self.assertFalse(iguales_consecutivos([1]))
    def test_casodos(self):
        self.assertFalse(iguales_consecutivos([1,1]))
    def test_casotresdistintos(self):
        self.assertFalse(iguales_consecutivos([1,2,3]))
    def test_casotresiguales(self):
        self.assertTrue(iguales_consecutivos([1,1,1]))
    def test_casovariossin3consecutivos(self):
        self.assertFalse(iguales_consecutivos([1,2,3,3,4,3,5,6,6]))
    def test_casovariosy3ultimosiguales(self):
        self.assertTrue(iguales_consecutivos([0,1,2,3,3,3]))
    def test_casovariosy3iguales(self):
        self.assertTrue(iguales_consecutivos([0,1,2,3,3,3,4]))

class test_vocales_distintas (unittest.TestCase):
    def test_menosdetres(self):
        self.assertFalse(vocales_distintas("abaco"))
    def test_tresomas(self):
        self.assertTrue(vocales_distintas("aereo"))

class test_pos_secuencia_ordenada_mas_larga(unittest.TestCase):
    def test_unsoloelemento(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([1]),0)
    def test_todalalistaordenada(self):
        l=[1,2,3,4]
        self.assertEqual(pos_secuencia_ordenada_mas_larga(l),0)
    def test_dosordenadasylamaslargaeslaprimera(self):
        l=[1,2,3,1,2]
        self.assertEqual(pos_secuencia_ordenada_mas_larga(l),0)
    def test_dosordenadaasylamaslargaeslasegundaporuno(self):
        l=[1,2,1,2,3]
        self.assertEqual(pos_secuencia_ordenada_mas_larga(l),2)
    def test_dosordenadaasylamaslargaeslasegundapormas(self):
        l=[1,2,1,2,3,4,5]
        self.assertEqual(pos_secuencia_ordenada_mas_larga(l),2)
    def test_dosdeigualtamañoyotraqueno(self):
        l=[3,1,2,3,1,2,3]
        self.assertEqual(pos_secuencia_ordenada_mas_larga(l),1)

class test_cantidad_digitos_impares(unittest.TestCase):
    def test_vacio(self):
        l=[]
        self.assertEqual(cantidad_digitos_impares(l),0)
    def test_sinnumerosimpares(self):
        l=[2,4,6]
        self.assertEqual(cantidad_digitos_impares(l),0)
    def test_algunosimparesdeundigito(self):
        l=[1,2,3,4,5,6,7]
        self.assertEqual(cantidad_digitos_impares(l),4)
    def test_numeros(self):
        l=[57, 2383, 812, 246]
        self.assertEqual(cantidad_digitos_impares(l),5)

class test_CerosEnPosicionesPares(unittest.TestCase):
    def test_vacia(self):
        l=[]
        CerosEnPosicionesPares(l) #IMPORTANTE!!! COMO NO DEVUELVE NADA SOLO PODEMOS COMPARAR S@PRE Y S@POST
        self.assertEqual((l),l)
    def test_unelemento(self):
        l=[1]
        CerosEnPosicionesPares(l)
        self.assertEqual((l),[0])
    def test_doselementos(self):
        l=[1,2]
        CerosEnPosicionesPares(l)
        self.assertEqual((l),[0,2])
    def test_muchoselementos(self):
        l=[1,2,3,4,5]
        CerosEnPosicionesPares(l)
        self.assertEqual((l),[0,2,0,4,0])
    def test_ceros(self):
        l=[0,0,0,0]
        CerosEnPosicionesPares(l)
        self.assertEqual((l),[0,0,0,0])

class test_CerosEnPosicionesPares2(unittest.TestCase):
    def test_vacia(self):
        l=[]
        self.assertEqual(CerosEnPosicionesPares2(l),l)
    def test_unelemento(self):
        l=[1]
        self.assertEqual(CerosEnPosicionesPares2(l),[0])
    def test_doselementos(self):
        l=[1,2]
        self.assertEqual(CerosEnPosicionesPares2(l),[0,2])
    def test_muchoselementos(self):
        l=[1,2,3,4,5]
        self.assertEqual(CerosEnPosicionesPares2(l),[0,2,0,4,0])
    def test_ceros(self):
        l=[0,0,0,0]
        self.assertEqual(CerosEnPosicionesPares2(l),l)

class test_sin_vocales(unittest.TestCase):
    def test_sinvocales(self):
        s = "bdr"
        self.assertEqual(sin_vocales(s),"bdr")
    def test_convocales(self):
        s = "abaco"
        self.assertEqual(sin_vocales(s),"bc")
    def test_solovocales(self):
        s = "aaa"
        self.assertEqual(sin_vocales(s),"")

class test_reemplaza_vocales(unittest.TestCase):
    def test_sinvocales(self):
        s = "bcbcb"
        self.assertEqual(reemplaza_vocales(s),s)
    def test_convocales(self):
        s="abaco"
        self.assertEqual(reemplaza_vocales(s),"_b_c_")
    def test_solovocales(self):
        s = "aaa"
        self.assertEqual(reemplaza_vocales(s),"___")

class test_dar_vuelta_str(unittest.TestCase):
    def test_vacia(self):
        l=""
        self.assertEqual(da_vuelta_str(l),l)
    def test_unelemento(self):
        l="a"
        self.assertEqual(da_vuelta_str(l),l)
    def test_varioselementosimpar(self):
        l="abc"
        self.assertEqual(da_vuelta_str(l),"cba")
    def test_varioselementospar(self):
        l="abcd"
        self.assertEqual(da_vuelta_str(l),"dcba")

class test_eliminar_repetidos(unittest.TestCase):
    def test_sinrepetidos(self):
        l = "abc"
        self.assertEqual(eliminar_repetidos(l),l)
    def test_conrepetidos(self):
        l = "abcabcdaf"
        self.assertEqual(eliminar_repetidos(l),"abcdf")

class test_resultadoMateria(unittest.TestCase):
    def test_promediomenora4(self):
        l = [3,3,2,1]
        self.assertEqual(resultadoMateria(l),3)
    def test_unelementomenora4(self):
        l=[10,3,10,10]
        self.assertEqual(resultadoMateria(l),3)
    def test_promediofinal(self):
        l=[5,5,5,5]
        self.assertEqual(resultadoMateria(l),2)
    def test_promediopromocion(self):
        l=[9,9,9,8]
        self.assertEqual(resultadoMateria(l),1)

class test_saldoActual(unittest.TestCase):
    def test_soloingresos(self):
        l=[("I",1000),("I",2000),("I",3000)]
        self.assertEqual(saldoActual(l),6000)
    def test_soloegresos(self):
        l=[("R",1000),("R",2000),("R",3000)]
        self.assertEqual(saldoActual(l),-6000)
    def test_prueba(self):
        l=[("I",2000),("R",20),("R",1000),("I",300)]
        self.assertEqual(saldoActual(l),1280)

class test_pertenecematriz(unittest.TestCase):
    def test_random(self):
        matriz = [[1,2,3],[4,5,6],[7,8,9]]
        resultado = [False,True,False]
        self.assertEqual(pertenece_a_cada_uno(matriz,4),resultado)

class test_es_matriz(unittest.TestCase):
    def test_vacio(self):
        l=[]
        self.assertFalse(es_matriz(l))
    def test_matrizdevacio(self):
        l=[[]]
        self.assertFalse(es_matriz(l))
    def test_uno(self):
        l=[[1]]
        self.assertTrue(es_matriz(l))
    def test_noes(self):
        l = [[1,2,3],[1,2,3],[1,2]]
        self.assertFalse(es_matriz(l))
    def test_sies(self):
        l = [[1,2],[1,2],[1,2]]
        self.assertTrue(es_matriz(l))

class test_filas_ordenadas(unittest.TestCase):
    def test_random(self):
        l = [[1,2,2],[1,2,3],[4,6,5]]
        res = [False,True,False]
        self.assertEqual(filas_ordenadas(l),res)

class test_columna(unittest.TestCase):
    def test_unacolumna(self):
        l=[[1],[2],[3]]
        res=[1,2,3]
        self.assertEqual(columna(l,0),res)
    def test_random(self):
        l=[[1,2,3],[4,5,6],[7,8,9]]
        res1 = [2,5,8]
        self.assertEqual(columna(l,1),res1)

class test_columnas_ordenadas(unittest.TestCase):
    def test_una_solafila(self):
        l=[[1,2,3]]
        self.assertEqual(columnas_ordenadas(l),[True,True,True])
    def test_unasolacolumnaordenada(self):
        l=[[1],[2],[3]]
        self.assertEqual(columnas_ordenadas(l),[True])
    def test_unasolacolumnadesordenada(self):
        l=[[2],[1],[3]]
        self.assertEqual(columnas_ordenadas(l),[False])
    def test_random(self):
        l=[[1,2,3],[4,1,3],[6,0,3]]
        res = [[True],[False],[False]]

class test_transpuesta(unittest.TestCase):
    def test_unelemento(self):
        l = [[1]]
        self.assertEqual(transponer(l),l)
    def test_filaacolumna(self):
        l = [[1,2,3]]
        lt = [[1],[2],[3]]
        self.assertEqual(transponer(l),lt)
    def test_columnaafila(self):
        lt = [[1,2,3]]
        l = [[1],[2],[3]]
        self.assertEqual(transponer(l),lt)
    def test_random(self):
        l = [[1,2,3],[4,5,6],[7,8,9]]
        lt = [[1,4,7],[2,5,8],[3,6,9]]
        self.assertEqual(transponer(l),lt)

class test_tateti(unittest.TestCase):
    def test_nadiegana(self):
        l = [["o","x","o"],["o","x","o"],["x","o","x"]]
        self.assertEqual(quien_gana_tateti(l),2)
    def test_ganaxvertical(self):
        l = [["x"," "," "],["x"," "," "],["x"," "," "]]
        self.assertEqual(quien_gana_tateti(l),1)
    def test_ganaovertical(self):
        l = [[" ","o"," "],["x","o"," "],["x","o"," "]]
        self.assertEqual(quien_gana_tateti(l),0)
    def test_ganaxhorizontal(self):
        l = [["x","x","x"],["x"," "," "],["x"," "," "]]
        self.assertEqual(quien_gana_tateti(l),1)
    def test_ganaohorizontal(self):
        l = [["x"," "," "],["o","o","o"],["x"," "," "]]
        self.assertEqual(quien_gana_tateti(l),0)
    def test_ganaxdiagonal1(self):
        l = [["x"," "," "],["x","x"," "],[" "," ","x"]]
        self.assertEqual(quien_gana_tateti(l),1)
    def test_ganaodiagonal2(self):
        l = [["x"," ","o"],["x","o"," "],["o"," "," "]]
        self.assertEqual(quien_gana_tateti(l),0)

if __name__ == '__main__':
    unittest.main(verbosity=2)