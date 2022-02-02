import os
f=open('first.txt')
content=f.read()
size=os.path.getsize('first.txt')
print(size)
# colist=content.split("\n")
# count=0
# c=0
# for line in colist:
#     if line:
#         count+=1
#     for character in line:
#         c+=1
# print(count)
# print(c)
