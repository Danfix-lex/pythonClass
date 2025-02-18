import string
from operator import is_not

name = "ayo"
print(name)
print(id(name))
name += "mide"
print(name)
print(id(name))
name = "tunde"
print(name)
print(id(name))
my_name = "tunde"
print(my_name.capitalize())
help(my_name.capitalize())
print(my_name[::-1])
print(id(my_name))
my_own_name = "danfix"
print(my_own_name.swapcase())
letters = "A"
word = "A"
print(is_not(letters, word))
titles = ["dan", "tunde", "malik", "jayjay"]
print(", ".join(titles))
print(", ".join(string.ascii_letters))
print(string.ascii_letters.split(", "))
print(string.ascii_letters.join(", "))
username = input("Enter your name")
if username.isspace():
    username = input("Enter your name")
    if username.isdigit():
        username = input("Enter your name")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
