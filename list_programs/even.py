list1=[]
num=int(input("Enter the number of list elements:"))
for i in range(num):
    list1.append(int(input("Enter the list element:")))

newl=[]
for i in list1:
    if(i%2==0):
        newl.append(i)
newl.sort()
print("old list:",list1)
print("new list:",newl)
