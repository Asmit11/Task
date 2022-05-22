#1.  Write a Python function to multiply all the numbers in a list.
#Sample list = [8,2,3,-1,7]
# def multiplication():
#     sample_list=[8,2,3,-1,7]
#     multiply=1
#     for i in sample_list:
#         multiply=multiply*i
#         i+=1
#     print(multiply)
# multiplication()

#2. Write a Python function to sum all the numbers in a list.
# Sample list : [8, 2, 3, 0, 7]
# def addition():
#     sample_list=[8,2,3,0,7]
#     sum=0
#     print("The sum of each characters of the list:")
#     for i in sample_list:
#         sum=sum+i
#         i+=1
#     print(sum)
# addition()

# 3.  Write a python function to find min of three numbers.(no parameter and no return type)
# def logic():
#     num1=int(input("Enter your first number:"))
#     num2=int(input("Enter your second number:"))
#     num3=int(input("Enter your third number:"))
#     if num1<num2 and num2>num3:
#         print(f"{num1} is the minimum of all three number")
#     elif num2<num3 and num1<num3:
#         print(f"{num2} is the minimum of all three number")
#     else:
#         print(f"{num3} is the minimum of all three")
# logic()

#4. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.
# def fizz_buzz():
#     num=int(input("Enter your number:"))
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(f"{num}")
# fizz_buzz()

#5. Create a function that can accept two arguments name and age and print its value.
# def logic(Name, Age):
#     print(f"Name={Name}\nAge={Age}")
# logic('Ashish', 30)

#6. Write a program function to find max of three numbers.(no parameter and no return type)
# def logic():
#     num1=int(input("Enter the first num:"))
#     num2=int(input("Enter the second num:"))
#     num3=int(input("Enter the third num:"))
#     if num1>num2 and num1<num3:
#         print(f"{num1} is the maximum of all three numbers")
#     elif num2>num3 and num2>num1:
#         print(f"{num2} is the maximun of all three numbers")
#     else:
#         print(f"{num3} is the maximum of all three numbers")
# logic()

#7. Write a Python function to print the even numbers from a given list. 
# sample: [1,2,3,4,5,6]
# def even():
#     sample=[1,2,3,4,5,6]
#     print(f"Even number from {sample} list are:")
#     for i in sample:
#         if i%2==0:
#             print(i, end=" ")
# even()

#8. Write a Python function to print the odd numbers from a given list. 
# sample: [1,2,3,4,5,6]
# def odd():
#     sample=[1,2,3,4,5,6]
#     print(f"Odd numbers from {sample} are:")
#     for i in sample:
#         if i%3==0:
#             print(i, end=" ")
# odd()
            
#9. Write a Python function that takes a number as a parameter and check the number is prime or not.
# def num():
#     num=int(input("enter the number:"))    
#     if num>1:
#         for i in range(2, num):
#             if (num%i==0):
#                 print(f"{num} is a prime number")
# num()   

#10  Write a function to reverse a string.

# def rev():
#     x="MarvelCinematicUniverse"
#     for j in range(9,-1,-1):
#         print(x[j],end="")
# rev()

## # 12. Write a program to create function func1()
# #  to accept a variable length of arguments and print their value.

# def func1(*arguements):
#     print(*arguements)
    
# func1('hello', 'hi', 23, '2383')

# # 13  Write a program to create function calculation() such that it can accept 
# # two variables and calculate addition and subtraction.Also, it must return 
# # both addition and subtraction in a single return call

# def calculation(c,d):
#     print(c+d)
#     print(c-d)
#     return c,d
# calculation(6,3)

# # 14. Write a program to create a function show_employee() using the following conditions.
# # It should accept the employee’s name and salary and display both.
# # If the salary is missing in the function call then assign default value 9000 to salary

# def func(Employee, salary=15000):
#     print('Employee: ', Employee )
#     print('Salary: ', salary)

# func('Marc Spktr', 30000)
# func('Khonshu')

# # 15. Find the largest item from a given list. 
# # sample: [4, 6, 8, 24, 12, 2]

# sample=[4,6,8,24,12,2]
# print(max(sample))

# # 16. Find the smalles item from a given list. 
# # sample: [4, 6, 8, 24, 12, 2]

# samples=[4,6,8,24,12,2]
# print(min(samples))

# # 17. Define a function that accepts roll number and returns
# #  whether the student is present or absent.

# def logic(rollno):
#     x=[23,43,22,56]
#     if rollno in x:
#         print(f'roll number {rollno}, is present.')
#     else:
#         print(f'roll number {rollno}, is absent')
# rollno=int(input('enter a roll number'))
# logic(rollno)

# # 18. Define a function that accepts a number and returns whether the number is even or odd.

# def func(x):
#     if x%2==0:
#         print(f"{x}, is even")
#     else:
#         print(f"{x}, is odd")
# x=int(input('enter your number: '))
# func(x)

# # 19. Define a function which counts vowels and consonant in a word.

# def count(val):
#     vov=0
#     cons=0
#     for i in range(len(val)):
#         if val[i] in ["a",'e','i','o','u']:
#             vov=vov+1
#         else:
#             cons=cons+1
#     print("count of vowels is", vov)
#     print("count of consonant is", cons)
# x=input("enter sth; ")
# count(x)

# # 20. Define a function that returns Factorial of a number.

# def factorial(num):
#     fact=1
#     while(num!=0):
#         fact*=num
#         num=num-1
#     print("Factorial is", fact)
# num=int(input('enter a number'))
# factorial(num)

# # 21. Define a function that accepts lowercase words
# #  and returns uppercase words.

# def respone(text):
#     z=text.upper()
#     print(z)
# text=input('Enter a string.')
# response(text)

# # 22. Define a function that accepts radius and returns the area of a circle.

# def area(radius):
#     area=3.14*radius**2
#     return area
# radius=int(input('enter radii; '))
# print(area(radius))


    




