#example looping program
# x=50
# for i in range(2,6):
#     x=x+i
#     print(x)
# for i in "x":
#     print(x)


# prime number code

# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # how many days lived
# from datetime import date
# a=date(2005,10,20)
# b=date(2026,4,28)
# print("No of days i lived:",(b-a))


# how many hours lived
# from datetime import date
# a=date(2005,10,20)
# b=date(2026,4,28)
# print("No of days i lived:",(b-a).total_seconds()/3600)




#year calendar
# import calendar
# year = int(input("Enter year: "))
# month=int(input("enter month"))
# print(calendar.month(month))





# random guess by the players
import random
p1=input("enter the player1")
p2=input("enter the player2")
s1=10
s2=10
d1=random.randint(1,10)
d2=random.randint(1,10)
print("player 1 turn")
g1=int(input("enter your guess"))
s1=s1-1
if g1==d1:
    break
print("player 2 turn")
g2=int(input("enter your guess"))
s2=s2-1
if g2==d2:
    break
print("summary")
print("{}:{}".format(p1,s1))
print("{}:{}".format(p2,s2))
print("result")
if s1>s2:
    print("winner is ",p1)
elif s2>s1:
    print("winnwr is ",p2)
else:
    print("TIE")


