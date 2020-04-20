print("Dice game v2.3 \n Made by JAYU")
def die(num):
    print("------------")
    if num==1:
        print("            ")
        print("            ")
        print("     0      ")
        print("            ")
        print("            ")
    if num==2:
        print("            ")
        print(" 0          ")
        print("            ")
        print("          0 ")
        print("            ")
    if num==3:
        print("            ")
        print("  0         ")
        print("      0     ")
        print("          0 ")
        print("            ")
    if num==4:
        print("            ")
        print("  0      0  ")
        print("            ")
        print("  0     0   ")
        print("            ")
    if num==5:
        print("      0     ")
        print("  0     0   ")
        print("            ")
        print("  0      0  ")
        print("            ")
    if num==6:
        print(" 0      0   ")
        print("            ")
        print(" 0      0   ")
        print("            ")
        print(" 0      0   ")
print("-------------")
from random import randint as # REVIEW:
d1=r(1,6)
die(d1)
d2=r(1,6)
die(d2)
a=d1+d2
print("\n You Rolled",a,"\n")
d3=r(1,6)
die(d3)
import random
d4=r(1,6)
die(d4)
b=d3+d4
print("\n your opponent rolled",b,"\n")
    print("",a,"-",b)

if a==b:
    print("Draw!\n Try again.")
elif a>b:
     print("You won!\n wanna play again?")
elif a<b:
    print("Your opponent won.\n wanna play again")
