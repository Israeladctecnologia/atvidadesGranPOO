
def fator(n):
    if n == 0:
        return 1
    else:
        return n * fator  (n-1)
    
print(fator(6))    
    
