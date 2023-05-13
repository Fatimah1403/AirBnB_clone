AirBnB clone project!
We create a Python package, a command interpreter in Python using the cmd module, and other files that work together to make this command-driven web app that imitates Airbnb service.
We carry out Unit testing in this project
We serialize and deserialize Classes- write and read JSON files.
We manage datetime
We use UUID
We use *args and **kwargs and in the project
We handle named arguments in a function

We carry out the management of objects including:
- Creating a new object (ex: a new User or a new Place)
- Retrieving an object from a file, a database etc…
- Doing operations on objects (count, compute stats, etc…)
- Updating attributes of an object
- Destroying an object


Requirements given for the project
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge case



Description of the command interpreter:
We use the built in python cmd to make the console.py that is used to manage this clone application.

How to start it
Run ./console.py

How to use it
Use the following defined function names to create and manage classes.

update_dict:
	Helper method for update() with a dictionary. Takes three arguments (self, classname, uid, s_dict)
quit:
	Exits the program.
create:
	Creates an instance. Takes one argument (self, line)
show:
	Prints the string representation of an instance. Takes one argument (self, line)
destroy
	Deletes an instance based on the class name and id. Takes one argument (self, line)
all:
	Prints string representation of all instances.- Takes one argument (self, line)
count:
	Counts the instances of a class. Takes one argument (self, line)
update:
	Updates an instance by adding or updating an attribute. Takes one argument (self, line)


examples
create user
