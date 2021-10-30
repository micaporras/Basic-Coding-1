# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

# Function for asking name
def get_name():
    name_func = input('What is your name?: ')
    return name_func

# Function for asking age
def get_age():
    age_func = input('How old are you?: ')
    return age_func

# Function for asking address
def get_address():
    address_func = input('Where do you live?: ')
    return address_func

# Function for displaying name, age, address
def display(namef, agef, addressf):
    print(f'Hi, my name is {namef}. I am {agef} years old and I live in {addressf} ')

# Variable for name
name = get_name()
# Variable for age
age = get_age()
# Variable for address
address = get_address()
# Displaying name, age, address
display(name, age, address)