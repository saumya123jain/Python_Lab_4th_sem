def is_prime(num):
    factor=0
    i=2
    while(i!=num):
        if (num%i==0):
            factor=1
        if(factor!=0):
            return "Composite"
        i+=1
    return "Prime"
print("Enter a number:")
num=int(input())
factor = is_prime(num)
print(factor)
