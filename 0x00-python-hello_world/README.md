Directory: 0x00-python-hello_world
This directory contains the solutions for the tasks and challenges related to the introductory topic of Python programming in the ALX Higher Level Programming curriculum.

Description
The tasks in this directory focus on the basics of Python, including writing and executing Python scripts, using the Python interpreter, and understanding Python bytecode.

Files
10-check_cycle.c, lists.h: C functions to check if a linked list has a cycle.
100-write.py: A Python script that prints a specific string to stderr and exits with status code 1.
101-compile: A script that compiles a Python script file. The Python file name is stored in the environment variable $PYFILE and the output filename is $PYFILEc.
102-magic_calculation.py: A Python function that performs a specific bytecode operation.


Usage
Each file is a standalone script or module and can be used or run separately. For example, you can run a Python script as follows:
python3 script_name.py

For C files, you can compile and run them as follows:
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 c_file_name.c -o output_name
./output_name