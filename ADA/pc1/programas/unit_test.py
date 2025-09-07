import numeros_grandes
import strassen
import moda
import subsecuencia
import random
import numpy
class Unit_Test:
    def __init__(self) -> None:
        pass
    @staticmethod
    def test_moda() -> None:
        test_length = 10
        n_tests = 5
        list_tests = [[random.randint(1,5) for _ in range(test_length)] for _ in range(n_tests)]
        for i in range(n_tests):
            m = moda.Moda(list_tests[i])
            print(f"{list_tests[i]} | Moda: {m}")
    @staticmethod
    def test_numeros_grandes()->None:
        lim_inf = 130
        lim_sup = 140
        for i in range(lim_inf,lim_sup):
            for j in range(i,lim_sup):
                result = numeros_grandes.mul(str(i),str(j))
                print(f"{i} x {j} = {result} | Resultado real: {i*j}")
    @staticmethod
    def test_strassen()->None:
        n_test = 2
        n_matrix = 4
        for _ in range(n_test):
            A = strassen.matriz_aleatoria(n_matrix,n_matrix)
            B = strassen.matriz_aleatoria(n_matrix,n_matrix)
            A_2 = numpy.matrix(A)
            B_2 = numpy.matrix(B)
            strassen.imprimir_matriz(strassen.multiplicar_matrices(A,B))
            print(numpy.matmul(A_2,B_2))
    @staticmethod
    def test_subsecuencia():
        test_length = 10
        n_tests = 5
        list_tests = [[random.randint(-10,10) for _ in range(test_length)] for _ in range(n_tests)]
        for i in range(n_tests):
            m = subsecuencia.max_subsecuencia(list_tests[i])
            print(f"{list_tests[i]} | Suma máxima: {m}")
    @staticmethod
    def start_tests():
        print("Moda:")
        Unit_Test.test_moda()
        print("Numeros grandes:")
        Unit_Test.test_numeros_grandes()
        print("Strassen:")
        Unit_Test.test_strassen()
        print("Subsecuencia maxima:")
        Unit_Test.test_subsecuencia()

if __name__ == "__main__":
    Unit_Test.start_tests()

