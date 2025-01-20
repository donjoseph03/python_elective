number=int(input("\nEnter a Number: "))
if number<2:
    print("\nSquare Root: ",number)
else:
    a=number
    b=(a+(number/a))/2
    while abs(b-a)>= 0.000001:
        a=b
        b=(a + (number/a))/2
    print("\nSquare Root: ",b)
