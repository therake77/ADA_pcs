import random

def leer_matriz_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        matriz = [list(map(int, linea.strip().split())) for linea in f if linea.strip()]
    return matriz

def ingresar_matriz_manual(filas, columnas):
    matriz = []
    print(f"Ingresa la matriz de tamaño {filas}x{columnas}:")
    for i in range(filas):
        fila = list(map(int, input(f"Fila {i+1}: ").split()))
        matriz.append(fila)
    return matriz

def matriz_aleatoria(filas, columnas, min_val=0, max_val=10):
    return [[random.randint(min_val, max_val) for _ in range(columnas)] for _ in range(filas)]

def pad_matriz(matriz, filas_obj, columnas_obj):
    filas = len(matriz)
    columnas = len(matriz[0])
    nueva = [[0]*columnas_obj for _ in range(filas_obj)]
    for i in range(filas):
        for j in range(columnas):
            nueva[i][j] = matriz[i][j]
    return nueva

def siguiente_potencia_2(n):
    potencia = 1
    while potencia < n:
        potencia *= 2
    return potencia

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        mid = n // 2

        A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
        A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
        A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
        A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
        B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
        B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
        B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
        B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

        M1 = strassen(suma(A11, A22), suma(B11, B22))
        M2 = strassen(suma(A21, A22), B11)
        M3 = strassen(A11, resta(B12, B22))
        M4 = strassen(A22, resta(B21, B11))
        M5 = strassen(suma(A11, A12), B22)
        M6 = strassen(resta(A11, A21), suma(B11, B12))
        M7 = strassen(resta(A12, A22), suma(B21, B22))

        C11 = suma(resta(suma(M1, M4), M5), M7)
        C12 = suma(M3, M5)
        C21 = suma(M2, M4)
        C22 = resta(resta(suma(M1, M3), M2), M6)

        nueva = [[0]*n for _ in range(n)]
        for i in range(mid):
            for j in range(mid):
                nueva[i][j] = C11[i][j]
                nueva[i][j+mid] = C12[i][j]
                nueva[i+mid][j] = C21[i][j]
                nueva[i+mid][j+mid] = C22[i][j]
        return nueva

def suma(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def resta(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    filas_A, columnas_A = len(A), len(A[0])
    filas_B, columnas_B = len(B), len(B[0])
    if columnas_A != filas_B:
        raise ValueError("Las matrices no son compatibles para multiplicación.")

    n = max(filas_A, columnas_A, filas_B, columnas_B)
    n2 = siguiente_potencia_2(n)
    A_pad = pad_matriz(A, n2, n2)
    B_pad = pad_matriz(B, n2, n2)
    C_pad = strassen(A_pad, B_pad)

    C = [fila[:columnas_B] for fila in C_pad[:filas_A]]
    return C

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

def main():
    print("Opciones de ingreso de matrices:")
    print("1. Manual")
    print("2. Aleatorio")
    print("3. Desde archivo .txt")
    opcion = input("Selecciona una opción (1/2/3): ")
    if opcion == '1':
        filas_A = int(input("Filas de la matriz A: "))
        columnas_A = int(input("Columnas de la matriz A: "))
        filas_B = columnas_A
        columnas_B = int(input("Columnas de la matriz B: "))
        A = ingresar_matriz_manual(filas_A, columnas_A)
        B = ingresar_matriz_manual(filas_B, columnas_B)
    elif opcion == '2':
        filas_A = int(input("Filas de la matriz A: "))
        columnas_A = int(input("Columnas de la matriz A: "))
        filas_B = columnas_A
        columnas_B = int(input("Columnas de la matriz B: "))
        A = matriz_aleatoria(filas_A, columnas_A)
        B = matriz_aleatoria(filas_B, columnas_B)
        print("Matriz A:")
        imprimir_matriz(A)
        print("Matriz B:")
        imprimir_matriz(B)
    elif opcion == '3':
        archivo_A = input("Nombre del archivo de la matriz A: ")
        archivo_B = input("Nombre del archivo de la matriz B: ")
        A = leer_matriz_archivo(archivo_A)
        B = leer_matriz_archivo(archivo_B)
        filas_A, columnas_A = len(A), len(A[0])
        filas_B, columnas_B = len(B), len(B[0])
        if columnas_A != filas_B:
            print("Las matrices no son compatibles para multiplicación.")
            return
    else:
        print("Opción inválida.")
        return
    print("Resultado de la multiplicación Strassen:")
    C = multiplicar_matrices(A, B)
    imprimir_matriz(C)

if __name__ == "__main__":
    main()

