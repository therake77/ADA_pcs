def max_subsecuencia(arr):
    def max_subsecuencia_cruzada(arr, left, mid, right):
        suma = 0
        izquierda_max = float('-inf')
        max_left = mid
        for i in range(mid, left-1, -1):
            suma += arr[i]
            if suma > izquierda_max:
                izquierda_max = suma
                max_left = i
        suma = 0
        derecha_max = float('-inf')
        max_right = mid+1
        for i in range(mid+1, right+1):
            suma += arr[i]
            if suma > derecha_max:
                derecha_max = suma
                max_right = i
        return izquierda_max + derecha_max, max_left, max_right

    def max_sub_sum(arr, left, right):
        if left == right:
            return arr[left], left, right
        mid = (left + right) // 2
        izquierda, izq_start, izq_end = max_sub_sum(arr, left, mid)
        derecha, der_start, der_end = max_sub_sum(arr, mid+1, right)
        cruzado, cruz_start, cruz_end = max_subsecuencia_cruzada(arr, left, mid, right)
        if izquierda >= derecha and izquierda >= cruzado:
            return izquierda, izq_start, izq_end
        elif derecha >= izquierda and derecha >= cruzado:
            return derecha, der_start, der_end
        else:
            return cruzado, cruz_start, cruz_end

    suma_max, inicio, fin = max_sub_sum(arr, 0, len(arr)-1)
    subsecuencia = arr[inicio:fin+1]
    return suma_max, subsecuencia

if __name__ == "__main__":
    entrada = input("Introduce la secuencia de números separados por espacio: ")
    arr = list(map(int, entrada.strip().split()))
    suma_max, subsecuencia = max_subsecuencia(arr)
    print("La suma máxima de una subsecuencia es:", suma_max)
    print("La subsecuencia de suma máxima es:", subsecuencia)
