n=int(input("enter the number"))
flag=0
def divisor(n):
    print("divisors are ")
    for i in range(1,n):
        if(n%i==0):
            print(i)
    print(n)
divisor(n)

            
    
