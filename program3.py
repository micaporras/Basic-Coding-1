# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

# Function for asking the money you have and how much is an apple
def total_money():
    money_func = float(input('The money you have: '))
    return money_func
def apple_price():
    apple_price_func = float(input('How much is an apple? '))
    return apple_price_func

#  Function for computing the maximum apples you can buy
def maximum_apple(moneyf, applef):
    apples_func = int(moneyf//applef)
    return apples_func

# Function for computing your change
def change(moneyf, possible_applesf, applef):
    change_func = moneyf-(possible_applesf*applef)
    return change_func

#Function for displaying the maximum apples you can by and your change
def display_output(possible_applesf, remain_moneyf):
    print(f'You can buy {possible_applesf} apples and your change is {remain_moneyf} pesos.')

# Variable for your money and the price of an apple
money = total_money()
apple = apple_price()
# Variable for computed maximum apple
possible_apples = maximum_apple(money, apple)
# Variable for your remaining money
remain_money = change(money, possible_apples, apple)
# Display the apples you can buy and your remaining money
display_output(possible_apples, remain_money)