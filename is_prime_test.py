'''
Tests for the is_prime function
'''

from is_prime import is_prime

def test_is_prime_prime():
    '''
    Test is_prime with prime number case
    '''
    # setup
    number = 11 # number to be passed as argument in invoke step
    expected = True # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_non_prime():
    '''
    Test is_prime with non-prime number case
    '''
    # setup
    number = 20 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected