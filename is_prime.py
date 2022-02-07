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
    Stubbed function that will eventually:
        Checks if a number is prime.
        Return True if the number is Prime.
        Return False if the number is not Prime.
    '''
    return


def main():
    '''
    Main
    '''
    # Manual testing is_prime (not needed, but sometimes can help)
    result = is_prime(5) # is_prime returns None as it is stubbed.
    print(result) # Prints None.


# This stops main from running whenever this file is imported.
if __name__ == '__main__':
    main()
