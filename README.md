# TDD-Example
Repo meant to be an example of Python Test Driven Development using pytest.

Going through the commit history will show TDD for an example function, `is_prime`, that returns True if a number is prime or False if a number isn't. It will expect to take a positive number as a parameter.

# What is TDD?
TDD, or Test Driven Development referse to a specific programming workflow.

### Step 1: Write a stubbed function.
Start with a base definition of some function. It will be stubbed, meaning it has no functionality, it does nothing, but has a name and parameters. In this case, I'm using `is_prime`

### Step 2: Write a failing test.
You should have an idea of what you want the function to do or what functionality you wish to add. With this idea you can write tests with some expected value results. These tests should fail as this functionality hasn't been added yet

These tests should fail as the functionality hasn't been implemented yet.

### Step 3: Passing Tests.
This is where you write code in your function to make your failing tests pass.


### Step 4: Repeat.
For more complicated functions, you may need to repeat step 2 and 3 until your function has all the functionality needed.

# Pytest
A quick summary of `pytest`. The python module we will be using for testing.

Each test function should start with the word test so that pytest recognises it as a test function, just like you file name guessing_test.py ends with test so that pytest knows its a file with tests in it.

Each test also should follow the same format. It should generally have 3 sections

### Section 1: setup
Setup should declare variables that we will need for the function we want to test, as well as what we expect the result of the function we are testing to be

### Section 2: invoke
This is where we call the function we are testing, passing some variables we declared in the setup as arguments, and store its result in a variable.

### Section 3: analyse
This is where we compare our expected value from setup with the actual value we got in invoke. This section will have our assert call(s)

Its also important to note that our test functions/cases should not have parameters (We do not learn about `pytest` fictures, or testing with them. That is what parameters are for, for pytest test functions)
