def swap(a,b):
    print("Numbers before swapping are a =",a,"b =",b)
    a=a+b
    b=a-b
    a=a-b
    print("Numbers after swapping a =",a,"b =",b)
print("Enter two numbers:")
a=int(input())
b=int(input())
swap(a,b)