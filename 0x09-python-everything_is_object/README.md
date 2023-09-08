#This is a project on Python-Everything is object

#TASK0
What function would you use to get the type of an object?
Write the name of the function in the file, without ().
#TASK1
How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ().
#TASK2
n the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 100
#TASK3
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 89
#TASK4
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a
#TASK5
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a + 1
#TASK6
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
#TASK7
What do these 3 lines print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
#TASK8
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
#TASK9
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
#TASK10
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
#TASK11
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
#TASK12
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
#TASK13
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
#TASK14
What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
#TASK15
What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
#TASK16
What does this script print?
def increment(n):
    n += 1
a = 1
increment(a)
print(a)
#TASK17
What does this script print?
def increment(n):
    n.append(4)
l = [1, 2, 3]
increment(l)
print(l)
#TASK18
What does this script print?
def assign_value(n, v):
    n = v
l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
#TASK19
Write a function def copy_list(l): that returns a copy of a list.
The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module
#TASK20
a = ()
Is a a tuple? Answer with Yes or No
#TASK21
a = (1, 2)
Is a a tuple? Answer with Yes or No.
#TASK22
a = (1)
Is a a tuple? Answer with Yes or No.
#TASK23
a = (1, )
Is a a tuple? Answer with Yes or No.
#TASK24
What does this script print?
a = (1)
b = (1)
a is b
#TASK25
What does this script print?
a = (1, 2)
b = (1, 2)
a is b
#TASK26
What does this script print?
a = ()
b = ()
a is b
#TASK27
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
#TASK28
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
#TASK29
Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):
Format: see example
Your file should be maximum 4-line long (no documentation needed)
You are not allowed to import any module
#TASK30
Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, 
except if the new instance attribute is called first_name.
You are not allowed to import any module
#TASK31
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:
How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)
#TASK32
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (104-line1.txt)
How many int objects are created by the execution of the second line of the script (104-line2.txt)
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
How many int objects are created by the execution of the last line of the script (104-line5.txt)
#TASK33
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
Why? (optional blog post :))
Hint: NSMALLPOSINTS, NSMALLNEGINTS
#TASK34
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

How many string objects are created by the execution of the first line of the script? (106-line1.txt)
How many string objects are created by the execution of the second line of the script (106-line2.txt)
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
How many string objects are created by the execution of the last line of the script (106-line5.txt)
