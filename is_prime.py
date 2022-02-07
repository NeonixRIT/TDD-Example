'''
Assignment prompt:
Use TDD to create a function that returns true if a number is prime and false if it isn't.
This function should take a number as an integer.

Write a main function that prompts a user for a number and prints whether it is prime or not.
It should continue to prompt for a number until the user enters 0 or a negative number.
Don't forget to comment your code!

NOTE:
Comments are more indepth for example/expanatory purposes
'''

# "number: int" and "-> bool" is called typing in python.
# This is strictly for readability but basically says:
#   number parameter is expected to be an int and
#   the function "is_prime" is expected to return a boolean
def is_prime(number: int) -> bool:
    '''
    Checks if a number is prime.
    Return True if the number is Prime.
    Return False if the number is not Prime.
    '''
    if number <= 1: # 0 and 1 are not prime numbers
        return False

    # Check if given number is evenly divisibale by numbers from 2 upto the square
    # root of itself plus 1. Casts the square root too an int and adds one because
    # range doesn't handle floats.
    for i in range(2, int(number ** (1/2)) + 1):
        if number % i == 0:
            return False
    return True


def main():
    '''
    Prompt the user for a number and print whether it is prime or not.
    Continue to prompt until the user inputs a number less than 1.
    '''
    number = 100 # initial value for number
                 # This just makes sure we enter the loop
                 # The initial value will be replaced at the top of the loop.
    while number > 0: # If number is less than 1 then break out of the loop.
        number = int(input('Enter a natural number: ')) # prompts for a positive number
        if is_prime(number): # Check if the number is prime
            print(number, 'is a prime number.') # if it is, print that it is
        else:
            print(number, 'is not a prime number.') # if it's not, print that it's not
        print() # print to make output more readable


# This stops main from running whenever this file is imported.
if __name__ == '__main__':
    main()
