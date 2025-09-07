#works because of pass-by-object-reference
def combinar(dictA:dict,dictB:dict)->None:
    for (u,v) in dictB.items():
            dictA[u] = dictA.get(u,0) + v

def frecuencias(A:list, start:int, stop:int)->dict:
    if(start<=stop):
        if(start == stop):
            return {A[start]:1}
        middle = int((start + stop)/2)
        left = frecuencias(A,start,middle)
        right = frecuencias(A,middle+1,stop)
        if(len(left) > len(right)):
            combinar(left,right)
            return left     
        else:
             combinar(right,left)
             return right 
    return {}

def Moda(A:list):
    freq_list = frecuencias(A,0,len(A)-1)
    fmax = max(freq_list.values())
    result = [k for k in freq_list.keys() if freq_list[k] == fmax]
    return result

lista = ['A','C','A','A','C','A','A','A','C','C','B','C','C','B','B']

print(Moda(lista))