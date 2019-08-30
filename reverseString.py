list_str=[]
def reversing(str1):
    list_str=str1.split(" ")
    n=len(list_str)
    print("Reversed string : ")
    while(n>0):
        print(list_str[n-1],end=" ")
        n=n-1
    #reversing the letters in the words
    print(" ")
    print("reversing the letters in the words :")   
    for i in list_str:
        print(i[::-1])

str1=input("Enter the string : ")
reversing(str1)
print(" ")
print("reversing the original string")
print(str1[::-1])

#welcome to bmsce
#em
