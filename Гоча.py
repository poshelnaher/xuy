#1
#a = int(input("Enter first number "))
#b = int(input("Enter second number "))
#c = int(input("Enter third number "))

#zet = input("What do ?")

#if zet == "+":
   # print ("summa = ", a+b+c)
#elif zet == "*":
  #  print ("proizv = ", a*b*c)
#elif zet == "sr":

    
 #   print (" srednee = ", (a+b+c)/3)
#else:
   # print ("error")

#2

#a = float(input("fist coordinata = "))
#b = float(input("second coordinata = "))
#if a > b:
#    z = a - b
#    print ("dlina = ", z )
#elif b > a:
 #   z = b - a
  #  print ("dlina = ", z )
#else:
   # print("dlina=0")

#3
#import random

#a =random.randint(100,1000)
#print (a)
#print (a//100, "сотен", a//10%10, "десятков", a%10,"единиц")

#4

#a = int(input("a = "))
#b = int (input("b = "))
#z = a
#c = b
#a = c
#b = z
#print (" b =", b, "a = ", a)

#5
#a = int(input("a = "))
#b = int(input("b = "))
#a = a+b
#b = a -b
#a = a -b
#print(a , b)

#6

#import random

#x =random.randint(2,17)
#print(x)
#b = ' '
#while x > 0:
#    b =str(x % 2) + b
#    x = x//2
#
#print (b)

#7
#import random

#x =random.randint(0,30)
#print("в десятичной", x)
#b = ' '
#while x > 0:
    #b =str(x % 2) + b
    #x = x//2

#print (" в двоичной ", b)
   
#8
#a = int(input("a = "))
#b = int(input("b = "))
#while b!=1:
  #  a = a*a
   # b = b - 1

#print (a)

#9

#a = int(input("number "))
#b = a*a
#c = b*b
#v = c*c
#a = b*v

#print (a)


#10

#a = int(input("кол студентов = "))
#import random
#b = random.randint(2, a)
#print (b)

#11
#import random
#a, b = map(int, input().split())
#print(*(randint(a,b+1) for l in range(5)))













