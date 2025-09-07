def removeZeros(num:str):
    k = 0
    for i in num:
        if(i == '0'):
            k+=1
        else:
            break
    if k == len(num):
        return "0"
    else:   
        return num[k:]

def shl(num:str,n:int)->str:
    for i in range(0,n):
        num+="0"
    return num

def split(num:str, m)->tuple:
    if(m>=len(num)):
        return ("0",num)
    else:
        index = len(num)-m
        return (num[0:index],num[index:])

def positiveSum(num1:str,num2:str)->str:
    if(len(num2) > len(num1)):
        (num1,num2) = (num2,num1)
    carry:int = 0
    bias = len(num1) - len(num2)
    result = ""
    for i in range(len(num1)-1,-1,-1):
        if((i-bias)>=0):
            sum = int(num1[i]) + int(num2[i-bias]) + carry
        else:
            sum = int(num1[i]) + carry
        result = str(int(sum%10)) + result
        carry = int(sum/10)
    if(carry == 1):
        result = f"{carry}"+result
    return result

def positiveSub(num1:str,num2:str)->str:    
    if(len(num2) > len(num1)):
        (num1,num2) = (num2,num1)
    result = ""
    bias = len(num1) - len(num2)
    carry = 0
    for i in range(len(num1)-1,-1,-1):
        if((i-bias)>=0):
            sub = int(num1[i]) - int(num2[i-bias]) - carry
        else:
            sub = int(num1[i]) - carry
        
        if sub < 0:
            sub+=10
            carry=1
        else:
            carry = 0
        result=str(sub) + result

    return result
