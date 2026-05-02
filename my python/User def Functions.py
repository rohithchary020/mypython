#step2
#defining the function
def a1():
    n1=10
    n2=20
    print(n1+n2)
def a2(a,b):
    print(a+b)
def a3():
    n1=50
    n2=60
    return n1+n2
def a4(a,b):
    return a+b

# step1
# calling a function
a1()
a2(30,40)
res=a3()
print(res)
res1=a4(70,80)
print(res1)





# second program

def Square():
    a=4
    x=input("area of square:",a*a)
    print(x)
    
def circle(a):
    x=input("radius of circle:",a*a*3.14)
    print(x)
    
def rectangle():
    x=10
    y=20
    return x*y
    

while(True):
    print("1.Square")
    print("2.circle")
    print("3.rectangle")
    print("4.exit")
    
    choice=input("enter your choice:")
    if choice==1:
        square()
    elif choice==2:
        circle(15)
    elif choice==3:
        result=rectangle()
        print(result)
    else: 
        break
        
    

    
