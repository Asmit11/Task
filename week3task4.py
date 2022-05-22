#1  Write a python program to reverse a given list using while loop. 
# a=[1,2,3,4]
# a=[1,2,3,4]
# reversed_list=[]
# i=3
# list=len(a)-1
# while i>=0:
#     reversed_list.append(a[i])
#     i-=1
# print(reversed_list)


#2 Write a python program to reverse a string using while loop. 
# a="python"
# i=5
# while i>=0:
#     print(a[i], end="")
#     i-=1

# 3.Write a python program to print a multiplication table of any number using while loop. 
# a=int(input("Table of number:"))
# i=1
# while True:
#     print(f"{a}*{i}=", a*i)
#     i+=1
#     if i==11:
#         break

# 4.Write a python program to reverse a given list using while loop.
# list=[1,2,3,4]
# l=len(list)
# reversed_list=[]
# i=l-1
# while i>=0:
#     reversed_list.append(list[i])
#     i-=1
# print(reversed_list)

#5.Write a program to print the following using while loop
# a. first 10 even numbers
# b.first 10 odd numbers
# c.first 10 natural numbers

# a=0
# print("FIRST 10 EVEN NUMBERS:")
# while a<=19:
#     print(a, end=",")
#     a+=2

# b=0
# print("FIRST 10 ODD NUMBER:")
# while b<=20:
#     print(b, end=",")
#     b+=3

# c=1
# print("FIRST 10 NATURAL NUMBER:")
# while c<11:
#     print(c, end=",")
#     c+=1

#6Write for loop statement to print the following series:
# 10 20 30 --------300

# for i in range(10,301,10):
#     print(i, end=",")

#7. Write a while loop statement to print the following series:
# 105 98 -------7

# i=105
# while i>=7:
#     print(i , end=" ")
#     i-=7

#8 Write a program to print the factorial of a number accepted from user.

num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial can be of positive number only.")
elif num==0:
    print("Factorial of 1: ", factorial)
else:
    for i in range(1,num+1):        
        factorial=factorial*i
    print(factorial)





