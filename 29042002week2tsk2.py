#1 What is the output of ‘banana’ > ‘BANANA’?
# a="BANANA"
# b="banana"
# print(a.lower())
# print(b.upper())

#2 Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
# A=[1,2,3,4,5]
# B=5
# print(B in A)

#3  Given three integers, print the smallest one. (Three integers should be user input)
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter your third number:"))
# if a<b and a<c:
#     print(f"{a} is the smallest integer")
# elif b<a and b<c:
#     print(f"{b} is the smallest integer")
# else:
#     print(f"{c} is the smallest integer")
    
#4  Given a three-digit number. Find the sum of its digits.
# number=int(input("enter your number:"))
# s=number//100 + (number%100)//10 + number % 10
# print(f"the sum is: {s}")

# 5Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where 
#  1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display an error message if the user enters a number
#  that is outside the range of 1 to 12.

# a=int(input("Enter your month number:"))
# if a==1:
#     print("January")
# elif a==2:
#     print("February")
# elif a==3:
#     print("March")
# elif a==4:
#     print("April")
# elif a==5:
#     print("May")
# elif a==6:
#     print("June")
# elif a==7:
#     print("July")
# elif a==8:
#     print("August")
# elif a==9:
#     print("September")
# elif a==10:
#     print("October")
# elif a==11:
#     print("November")
# elif a==12:
#     print("December")
# else:
#     print("Error! The number should be in range of 1 to 12.")

#6 Given x = 5, what will be the value of x after we run x+=3?
# x=5
# x+=3 # this mean adding 3 to the value that is assigned to the variable x
# print(x)

#7  Write a Python Program to Check Prime Number.
# x=(int(input("Enter your number:")))
# if x%x==0:
#     print(f"{x} is a prime number")
# else:
#     print(f"{x} is not a prime number")

#8  A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
# marks=int(input("enter your marks:"))
# if marks>80:
#     print("Grade A")
# elif marks>60 and marks<=80:
#     print("Grade B")
# elif marks>50 and marks<=60:
#     print("Grade C")
# elif marks>45 and marks<=50:
#     print("Grade D")
# elif marks>25 and marks<=45:
#     print("Grade E")
# else:
#     print("Grade F")

#9 Take input of age of 3 people by user and determine oldest and youngest among them
# a=int(input("Enter the first person's age"))
# b=int(input("Enter the second person's  age"))
# c=int(input("Enter the third person's age:"))
# if a<b and a<c:
#     print(f"{a} is the youngest")
# elif b<c and b<c:
#     print(f"{b} is the youngest")
# else:
#     print(f"{c} is the youngest")
# if a>b and a>c:
#     print(f"{a} is the eldest")
# elif b>c and b>a:
#     print(f"{b} is the eldest")
# else:
#     print(f"{c} is the eldest")

#10 Write a program to check whether a person is eligible for voting or not. (accept age from user)
# a=int(input("enter the age:"))
# if a>=18:
#     print("you're eligible to vote")
# else:
#     print("you're not eligible to vote")

#11Write a program to check whether a number entered by user is even or odd
# a=int(input("Enter the number:"))
# if a%2==0:
#     print(f"{a} is a even number")
# else:
#     print(f"{a} is an odd number")

#12  Write a program to check whether a number is divisible by 7 or not.
# a=int(input("enter your number:"))
# if a%7==0:
#     print(f"{a} is divisible by 7")
# else:
#     print(f"{a} is not divisible by 7")

#13  Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
# a=int(input("Enter the number:"))
# if a%5==0:
#     print("Hello")
# else:
#     print("Bye")

#14  Write a program to accept percentage from the user and display the grade according to the following criteria:

        #  Marks                                    Grade
        #  > 90                                         A
        #  > 80 and <= 90                    B
        #  >= 60 and <= 80                  C
        #  below 60                                 D

# percentage=int(input("Enter your percentage:"))
# if percentage>90:
#     print("GRADE A")
# elif percentage>80 and percentage<=90:
#     print("GRADE B")
# elif percentage>=60 and percentage<=80:
#     print("GRADE C")
# else:
#     print("GRADE D")

#15 Accept any city from the user and display monument of that city.
                #   City                                 Monument
                #   Delhi                               Red Fort
                #   Agra                                Taj Mahal
                #   Jaipur                              Jal Mahal

# City1="Delhi"
# City2="Agra"
# City3="Jaipur"
# print("CHOOSE (DELHI , AGRA , JAIPUR)")
# a=input("Enter the city's name:")
# if a==City1:
#     print("RED FORT")
# elif a==City2:
#     print("TAJ MAHAL")
# elif a==City3:
#     print("JAL MAHAL")

#16 Write the output of the following if a = 9
        
    # if (a > 5 and a <=10):    
    #      print("Hello")    
    # else:    
    #     print("Bye")

# a=9
# if (a>5 and a<=10):
#     print("Hello")
# else:
#     print("Bye")
# # the output for the above code is Hello.

#17 Write a program to whether a number (accepted from user) is divisible by 2 and 3 both
# a=int(input("enter the number:"))
# if a%2==0 and a%3==0:
#     print(f"Yes {a} is divisible by both 2 and 3")
# else:
#     print(f"Not {a} is not divisible by both 2 and 3")

#18 Write a program to check a character is vowel or not.
# a=input("enter the letter:")
# if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
#     print(f"{a} is a vowel letter")
# else:
#     print(f"{a} is a consonent letter")

#19 Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16

# firstNumber=int(input("enter the first number:"))
# secondNumber=int(input("enter the second number:"))
# operator=input("please choose your operator: +, -, *, /:")

# if operator=='+':
#     print(firstNumber+secondNumber)
# elif operator=='-':
#     print(firstNumber-secondNumber)
# elif operator=='*':
#     print(firstNumber*secondNumber)
# elif operator=='/':
#     print(firstNumber/secondNumber)
# else:
#     print("error")
    









    

 

