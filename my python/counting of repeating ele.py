a=int(input("Enter Any Number:"))
b={}

for i in str(a):
    if i not in b:
        b[i]=1
    else:
        b[i]=b[i]+1
b=[i[1] for i in b.items() if i[1]>1]
print(len(b))

