m=int(input())
n=int(input())

def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if (m%i)==0:
            fm.append(i)
    fn=[]
    print(fm)
    for j in range(1,n+1):
        if (n%j)==0:
            fn.append(j)

    fc=[]
    print(fn)
    for f in fm:
        if f in fn:
            fc.append(f)
    return(fc[-1])



print("Gcd is ",gcd(m,n))







