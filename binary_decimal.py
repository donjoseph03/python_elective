binary_number=input("enter the binary number:")
length=len(binary)
num=0
for i in range(length):
    num+=int(binary_number[length-i-1])*int(2**i)
print(num)
