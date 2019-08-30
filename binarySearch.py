pos=-1
def binarysearch(A,n,key):
    high=n-1
    low=0
    while(low<=high):
        mid=int((high+low)/2)
        if(A[mid]==key):
            return True
        else:
            if(key<A[mid]):
                high=mid-1
            else:
                low=mid+1
    return False
a=[];
n=int(input("enter the number of elements"))
print("enter the sorted array")
for i in range(0,n):
    x=int(input(" "))
    a.append(x)

key=int(input("enter the key element to be searched"))
result=binarysearch(a,n,key)
print(result)        
    
            
