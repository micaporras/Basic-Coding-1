# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

# Function for showing the prices
def prices():
    print('The price of an apple is 20 pesos and orange is 25 pesos')

# Function for asking how many apples and oranges you want to buy
def get_apples():
    apple_count = int(input('How many apples you want to buy?: '))
    return apple_count

def get_oranges():
    oranges_count = int(input('How many oranges you want to buy?: '))
    return oranges_count

# Function for computing and displaying the total amount
def display_total(applesf, orangesf):
    total = (applesf*20) + (oranges*25)
    print(f'The total amount is {total}')


# Display the price of apple and orange
price = prices()
# Ask how many apples and oranges you want to buy
apples = get_apples()
oranges = get_oranges()
# Display the total amount
display_total(apples, oranges)