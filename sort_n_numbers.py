print("Python program to sort n numbers")
n=int(input("input number of elements :"))
numberlist=[]
for i in range(n):
    numberlist.append(int(input("enter element "+str(i+1)+" : ")))
numberlist.sort()
print("numbers after sorting are :")
for i in range(n):
    print(numberlist[i])
                
