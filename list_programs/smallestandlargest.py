list1=[]
num=int(input("Enter the number of list elements:"))
for i in range(num):
    list1.append(int(input("Enter the list element:")))
print(list1)
lar=max(list1)
sma=min(list1)
print("Largest number is:",lar)
print("Smallest number is:",sma)
