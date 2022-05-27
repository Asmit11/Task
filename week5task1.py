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

# print("Third largest num: ",list2[-3])





    












