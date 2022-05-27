# 1. Write a Python program to get the smallest number from a list
# list=[1,2,3,4,5]
# print(min(list))

#2. Write a Python function to check a list is empty or not.
# def check():
#     list=[]
#     if len(list)==0:
#         print("The list is empty")
#     else:
#         print("The list is not empty")
# check()

#3. Write a Python program to select an item randomly from a list. 
# import random
# my_list=[1,2,3,4,5,6]
# print(random.choice(my_list))

#4. Write a Python program to copy a list.
# list1=[1,2,3,4,5,"Ram",2.30]
# list2=list1.copy()
# print("list1:", list1)
# print("list2:", list2)

#5. Write a Python program to find the 2nd largest number in a list.
# list1=[1,5,6,7,8]
# list2=list(set(list1))
# list2.sort()

# print(f"The second largest number in the list:{list1} is", list2[-2])

#6. Write a Python program to print a specified list after removing the 3rd elements.
# list=[1,2,3,4,5,6,]
# del list[2]
# print(list)

#7. Write a Python program to count the number of even and odd numbers from a series of numbers.
# num=(1,2,3,4,5,6,7,8,9,10)
# #Declaring tuple
# even=0
# odd=0
# for x in num:
#     if x%2==0:
#         even+=1
#     else:
#         odd+=1
# print("The number of even numbers from the series of numbers:", even)
# print("The numbers of odd numbers from the series of numbers:", odd)

#8. Write a Python program to add an item in a tuple.
# Tuple1=("ASMIT","ARYAN",12)
# print("original tuple",Tuple1)
# List1=list(Tuple1)
# List1.insert(3,"KRI")
# Tuple2=tuple(List1)
# print("New Tuple:", Tuple2)

#9. Write a Python program to convert tuple to list.
# tuple=(1,2,"Lucy","Noya")
# print("Tuple:", tuple)
# print("---CONVERTING TUPLE INTO LIST---")
# list1=list(tuple) #conversion of tuple into list
# print("List:", list1)

#10. Write a Python program to convert a tuple to a string.
# def convertingtuple(tuple):
#     string=""
#     for i in tuple:
#         string=string+i
#     return string    

# tuple1=("L",'U','C','Y')
# print("TUPLE:", tuple1)
# print("****CONVERTING TUPLE INTO STRING****")
# string=convertingtuple(tuple1)
# print("STRING:", string)

#11. Write a Python program to convert a list to a tuple.
# list=[1,2,3,4]
# print("LIST:", list)
# print("**CONVERTING LIST INTO TUPLE")
# tuple1=tuple(list)
# print("TUPLE:", tuple1)

#12. Write a Python Program to Convert List of Tuple into Dictionary
# list=[("Ram", 1),("Shyam",2),("Kri",3)]
# print("LIST:", list)
# print("**CONVERTING LIST OF TUPLE INTO DICTIONARY**")
# di=dict(list)
# print("DICTIONARY:", di)

#13. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# sample_dictionary={0:10, 1:20}
# print("Dictionary:", sample_dictionary)
# #updating the above dictionary using update 
# sample_dictionary.update({2:30}) 
# print("Updated Dictionary:", sample_dictionary)

#14. 14. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in (dic1,dic2,dic3):
#     dic4.update(i)
# print(dic4)

##15.  Write a Python script to check if a given key already exists in a dictionary.

# data={"name":"Asmit",'age':18}
# data1=data.get('name')

# print(data1)



##16.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)



##17. Write a Python script to merge two Python dictionaries.

# dict1={"name":"Asmit","age":18}
# dict2={"address":"baneshwor","weight":60}

# dict1.update(dict2)
# print(dict1)



#18. Write a Python program to find the 3nd largest number in a list.
# list1=[22,64,11,345,23,535,444,64,43]

# list2=list(set(list1))
# list2.sort()

# print("Third largest num is ",list2[-3])

# # 19. Write a Python program to print the odd numbers from a given list. 
# list  = [1,2,3,4,5,6,7,8,9]
# a = len(list)
# for i in range(a):
#     c = list[i]
#     if c % 2!= 0:
#         print(c, end=" ")
#     else:
#         pass


# # 20. Write a program to accept percentage and display the Category according to the  following criteria :
# # Percentage	Category
# # < 41	                     Failed
# # >=41 & <55	Fair
# # >=55 & <65	Good
# # >=65	                     Excellent
# num= int(input("Enter your percentage :"))
# if num < 0:
#     print("Enter a valid marks.")
# elif num < 41:
#     print("Failed")
# elif num >= 41 and a < 55:
#     print("Fair")
# elif num >= 55 and a <65:
#     print("good")
# elif num >= 65:
#     print("Excellent")

# # 19. Write a Python program to create a set.
# s= set()
# print(type(s))


# # 21. Write a Python program to add member(s) in a set.
# s = {1}
# s.add(24)
# print(s)


# # 22. Write a Python program to remove item(s) from set
# s = {21,1}
# s.remove(21)
# print(s)


# # 23. Write a Python program to remove an item from a set if it is present in the set.
# a = {1,2,3,4,"Kri"}
# print(a)
# print("----Removing Kri--")
# if "Kri" in a:
#     a.remove("Kri")
# else:
#     pass
# print(a)


# # 24. Write a Python program to create an intersection of sets. 
# a = {1,2,3}
# b = {4,5,6}
# c = a | b
# print(c)


# # 25. Write a Python script to check if a given key exists in a dictionary.
# a = int(input("What do you want to check :"))
# c = {1:2,3:4,5:6}
# if a in c:
#     print(True)
# else:
#     print(False)


# # 26. Write a Python script to check if a given values exists in a dictionary.
# a = int(input("What do you want to check :"))
# c = {1:2,3:4,5:6}
# if a in c.values():
#     print(True)
# else:
#     print(False)





    












