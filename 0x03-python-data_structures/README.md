#This is a project on PYTHON LISTS DATA STRUCTURES

#TASK 0
Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

#TASK 1
Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except

#TASK 2
Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify 
anything, and returns the original list
You are not allowed to import any module
You are not allowed to use try/except

#TASK 3
Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

#TASK 4
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except

#TASK 5
Write a function that removes all characters c and C from a string.
Prototype: def no_c(my_string):

#TASK 6
Write a function that prints a matrix of integers.
Prototype: def print_matrix_integer(matrix=[[]]):

#TASK 7
Write a function that adds 2 tuples.
Prototype: def add_tuple(tuple_a=(), tuple_b=()):
Returns a tuple with 2 integers:
The first element should be the addition of the first element of each argument
The second element should be the addition of the second element of each argument

#TASK 8
Write a function that returns a tuple with the length of a string and its first character.
Prototype: def multiple_returns(sentence):

#TASK 9
Write a function that finds the biggest integer of a list.
Prototype: def max_integer(my_list=[]):

#TASK 10
Write a function that finds all multiples of 2 in a list.
Prototype: def divisible_by_2(my_list=[]):

#TASK 11
Write a function that deletes the item at a specific position in a list.

#TASK 12
complete the source code in order to switch value of a and b

#TASK 13
Technical interview preparation:
You are not allowed to google anything
Whiteboard first
Write a function in C that checks if a singly linked list is a palindrome.
Prototype: int is_palindrome(listint_t **head);
Return: 0 if it is not a palindrome, 1 if it is a palindrome
An empty list is considered a palindrome

#TASK 14
Create a C function that prints some basic info about Python lists.

Prototype: void print_python_list_info(PyObject *p);
Format: see example
Python version: 3.4
Your shared library will be compiled with this command line: 
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: Ubuntu 14.04 LTS
Start by reading:
listobject.h
object.h
Common Object Structures
List Objects
