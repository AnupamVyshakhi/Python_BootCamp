# -*- coding: utf-8 -*-
"""class 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/158IyCyEAa0sIOekr4kNyrbWq4UEwmj_1
"""

print("Hey all")

name=input("Enter your name")
print(name)

age=int(input("Enter your age"))
print(age)

print(type(name))
print(type(age))

pi=float(input("Enter the roubd off value of pi"))
print(pi)

# single line comment
'''indicates a
multiline comment'''
print("Hey, python")

print('''We can print
multiple lines''')

print('''MENU
1.Samosa
2.Mandi
3.Lime Juice
4.Chicken Biriyani''')
op=int(input("Enter your choice :"))
if op==1:
  print("Order placed is samosa!")
elif op==2:
  print("Order placed is Mandi!")
elif op==3:
  print("Order placed is Lime Juice!")
elif op==4:
  print("Order placed is Chicken Biriyani!")
else:
  print("Wrong option is chosen!!!")

num=int(input("Enter a non zero number"))
if num>0:
  print("Number '",num,"' is a positive number!!!")

n=int(input("Enter the number"))
if n%2==0:
  print("The number '",n,"' is an even number")
else:
  print("The number '",n,"' is an odd number")

mark=int(input("Enter your mark"))
if mark>=90:
  print("Grade A")
elif mark>=80 and mark<=89:
  print("Grade B")
elif mark>=60 and mark<=79:
  print("Grade C")
elif mark>=50 and mark<=59:
  print("Grade D")
else:
  print("Failed!!!")