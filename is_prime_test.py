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


def test_is_prime_0():
    '''
    Test is_prime with number 0
    '''
    # setup
    number = 0 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_1():
    '''
    Test is_prime with number 1
    '''
    # setup
    number = 1 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


# Tests added as part of intermediary step regression testing.
def test_is_prime_non_prime_neg_10():
    '''
    Test is_prime with number prime number -10
    '''
    # setup
    number = -10 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_prime_neg_11():
    '''
    Test is_prime with number prime number -11
    '''
    # setup
    number = -11 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_2():
    '''
    Test is_prime with number 2
    '''
    # setup
    number = 2 # number to be passed as argument in invoke step
    expected = True # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_3():
    '''
    Test is_prime with number 3
    '''
    # setup
    number = 3 # number to be passed as argument in invoke step
    expected = True # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_10():
    '''
    Test is_prime with number 10
    '''
    # setup
    number = 10 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_23():
    '''
    Test is_prime with number 23
    '''
    # setup
    number = 23 # number to be passed as argument in invoke step
    expected = True # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_24():
    '''
    Test is_prime with number 24
    '''
    # setup
    number = 24 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected


def test_is_prime_100():
    '''
    Test is_prime with number 100
    '''
    # setup
    number = 100 # number to be passed as argument in invoke step
    expected = False # expected result
    # invoke
    actual = is_prime(number) # invoke function and get actaul result
    # analyse
    assert actual == expected
