#1Write a program to accept percentage and display the Category according to the  following criteria :

# Percentage	Category
# < 40	                     Failed
# >=40 & <55	Fair
# >=55 & <65	Good
# >=65	                     Excellent

# a=int(input("Enter your percentage:"))
# if a<40:
#     print("Failed")
# elif a>=40 and a<55:
#     print("Fair")
# elif a>=55 and a<65:
#     print("Good")
# elif a>=65:
#     print("Excellent")

#2Write a Python Program to Swap Two Variables.
# a=int(input("Enter the first number(a):"))
# b=int(input("Enter the second number(b):"))
# c=a
# a=b
# b=c

# print("a:", a)
# print("b:", b)

#3 Write a program to print multiplication table of a  number 10 using for loop.
# number=10
# for i in range(1,11):
#     print(number,"*",i, "=", number*i)

#4 Print list in reverse order using a loop. Hint: list1=[1,2,3,4]
# list1=[1,2,3,4]
# reversed_list=[]
# for i in reversed(list1):
#     reversed_list.append(i)
# print(reversed_list)

#5 Display numbers from -10 to -1 using for loop.
# for i in range (-11,0):
#     print(i, end=" ")

#6 Use else block to display a message “Done” after successful execution of for loop.
# for i in range (0,8):
#     print(i)
# print("DONE")

#7 Find the factorial of a number 5.

# #8 Use a loop to display elements from a given list present at odd index positions. Given: my_list=[10,20, 30, 40, 50, 60, 70, 80, 90, 100]
# my_list=[10,20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in (1, len(my_list),2):
#     print(my_list(i))

#9 Calculate the cube of all numbers from 1 to a given number. (1-6)
# example:
# Expected output:
# 1-1
# 2-8
# 3-27
# 4-64
# 5-125
# 6-216

# for i in range(1,7):
#     print(i, "-", i**3)

#10Print First 10 natural numbers using for loop.
# print("The first 10 natural numbers are:")
# for i in range(1,11):
#     print(i )
        
        
# LOOP 
# for i in range(5):   
#     for j in range(5):  
#         print("*",end="")
#     print("")           
    
# for i in range(5):   
#   for j in range(i):   
#     print("*",end="")
#   print("*")
  
# for i in range(5):    
#   for j in range(5-i):    
#     print("*",end="")
#   print()
  
# for i in range(5):   
#   for j in range(i):    
#     print("*",end="")
#   print("*")

# for i in range(5): 
#   for j in range(5-i):    
#     print("*",end="")
#   print()




# a=input("Please! enter an alphabet:")
# b=a.lower()
# list=["a","e","i","o","u"]
# while b in list:
#     print(f"{b} is a vowel letter.")
#     break
# else:
#     print(f"{b} is a consonant")




# i=0
# while True:
#       i+=1
#       print(i)
#       if(i==3):
#             continue
# print("Rest of the code")

from ast import Continue


i=1
while i<=10:
      if i==5:
            break
      print(i)
      i+=1
      



