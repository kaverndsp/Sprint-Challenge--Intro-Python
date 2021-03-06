# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")

# using the builtin python method startswith() to compare the 0 index with 'D' for each string
a = [human.name for human in humans if human.name.startswith('D')]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")

# same thing, instead using the endswith() method
b = [human.name for human in humans if human.name.endswith('e')]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")

# I used this resource for this problem https://stackoverflow.com/questions/20461847/str-startswith-with-a-list-of-strings-to-test-for
prefix = ['C', 'D', 'E', 'F', 'G']
c = [human.name for human in humans if human.name.startswith(tuple(prefix))]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")

# In the expression, just adding 10 to the ages
d = [human.age + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")

# in the expression, using a f format string to print out name-age
e = [f"{human.name}-{human.age}" for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")

# expression(create a tuple with human name and age) for loop (go through humans in list & set range between 27 & 33)
f = [tuple([human.name, human.age])
     for human in humans if human.age in range(27, 33)]

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")

# used this resource https://www.python.org/dev/peps/pep-0274/
g = [(Human(human.name.upper(), human.age + 5))for human in humans]

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")

# Using the sqrt method. Found it in this resource https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.
h = [math.sqrt(human.age) for human in humans]

print(h)
