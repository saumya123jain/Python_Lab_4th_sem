def palindrome(num):
    j=-1
    mid=len(num)//2
    for i in range(0,mid+1):
        if(num[i]==num[j]):
            j-=1
        else:
            return -1
num="aabaa"
s=palindrome(num)
if(s==-1):
    print("Not a palindrome")
else:
    print("Palindrome")
