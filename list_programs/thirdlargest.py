list1=[]
n=int(input("Enter the number of list elements:"))
for i in range(n):
    list1.append(int(input("Enter the list element:")))

co=0
ma=max(list1)
while(ma in list1):
    list1.remove(ma)
    if ma not in list1 and co<1:
        ma=max(list1)
        co+=1

print("Third largest element is : ",list1[-1])
