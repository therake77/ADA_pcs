import mylib
def mul(A:str,B:str)->str:
    A = mylib.removeZeros(A)
    B = mylib.removeZeros(B)

    if(len(A)<=1 and len(B)<=1):
        return str(int(A) * int (B))
    
    n = int(max(len(A),len(B)))
    m = int(n/2)
    
    a,b = mylib.split(A,m)
    c,d = mylib.split(B,m)
    
    p1 = mul(a,c)
    p2 = mul(b,d)
    p3 = mul(mylib.positiveSum(a,b),mylib.positiveSum(c,d))
    
    p3= mylib.positiveSub(mylib.positiveSub(p3,p1),p2)

    return mylib.removeZeros(mylib.positiveSum(mylib.positiveSum(mylib.shl(p1,2*m),mylib.shl(p3,m)),p2))


