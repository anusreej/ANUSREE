limit=int(input("Enter the limit"))
def multiple(n,i):
    if(i>limit):
        return
    print(i*n)
    return multiple(n,i+1)
n=3
i=1
multiple(n,i)
