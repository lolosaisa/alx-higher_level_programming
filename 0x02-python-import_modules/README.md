This directory contains python practices for the "import modules" from
the ALX Software Engineering Program

a module is a python file containing some type code. In python any file
can be a module

there are two types of modeles
:user defined
:built in

why use of module
increases code reusability
saves time
it's easy to maintain a program that uses modules
increases code readability

to use the things in the in build module you have to use the name of the module then call whatever function you want
example:
import math
print(math.e)// math s the name of our module and e is the value we want to access

""""""""""""""""""""""""""""""PRACTICE QUESTIONS"""""""""""""""""""""""""""""""""""""""""""""""""""
TASK 0
0. Import a simple function from a simple file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

You have to use print function with string format to display integers
You have to assign:
the value 1 to a variable called a
the value 2 to a variable called b
and use those two variables as arguments when calling the functions add and print
a and b must be defined in 2 different lines: a = 1 and another b = 2
Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
You can only use the word add_0 once in your code
You are not allowed to use * for importing or __import__
Your code should not be executed when imported - by using __import__, like the example below
guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$ 
