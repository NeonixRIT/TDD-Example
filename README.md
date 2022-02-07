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

# This Example
Given the prompt:

"Use TDD to create a function that returns true if a number is prime and false if it isn't.
This function should take a number as an integer.

Write a main function that prompts a user for a number and prints whether it is prime or not.
It should continue to prompt for a number until the user enters 0 or a negative number.
Don't forget to comment your code!"

I will go through and complete the assignment on this repo

### Step 1a: Write Stubbed Function
I created my main `is_prime.py` boilerplate file. I commented the file, created my stubbed function, commented it, created a main, commented it, and called it inside the `if __name__ == '__main__':` statement.

You can browse the code here: [8dcb1e3](https://github.com/Acher0ns/TDD-Example/blob/8dcb1e390285891308c1eabcf8a27994887645f8/is_prime.py) # This is an abbreviated commit hash. You will be viewing the code at this commit.

### Step 2a: Write Failing Tests
Here, I created my tests file `is_prime_test.py` containing my initial tests for my `is_prime` function. In this case, it is 2 cases, testing a prime number `11` (should return True) and a non-prime number `20` (should return False).

You can browse the code here: [af6e3a8](https://github.com/Acher0ns/TDD-Example/blob/af6e3a86d562d4af0d7b40a59d82c4e823a23f0f/is_prime_test.py)

### Step 3a: Make Tests Pass
Then, I implemented the `minimal` amount of code needed to make the tests pass and still work for most other cases HOWEVER, there are still problems with the code. These are what Step 4 is for.

You can browse the new code here: [b647038](https://github.com/Acher0ns/TDD-Example/blob/b6470387cabfbd8513682b4fc573b2538ba6be59/is_prime.py)

### Step 4a: Repeat
If you look at the function or even test `is_prime` manually in main, you would notice that our function doesn't work for 0 and 1, which are non-prime numbers, however, `is_prime` currently says that they are, because if 1 or 0 is passed as an argument, it attempts to loop through a range from 2 to 0 or 2 to 1. This loops 0 times and jumps to the bottom of the function and returns True.

### Step 2b: Write Failing Tests For New Cases
Here we write 2 failings tests for out new cases of if 0 and 1 with the expected value of False because we don't expect 0 and 1 to be prime numbers.

You can browse the new tests here: [fd27cfe](https://github.com/Acher0ns/TDD-Example/blob/fd27cfee90537484ee359e2740ae19b10b01e769/is_prime_test.py)

### Step 3b: Make New Tests Pass
Here, I wrote the minimal code needed to make the new tests pass for new test cases of 0 and 1. This can be done with a simple contitional at the beginning of the function checking if the number is at or below 1 and return False. Coincidentally this covers other cases as well, like if a negative number is input to the function. We will handle these test cases in the next step

You can browse the new code here: [68920b6](https://github.com/Acher0ns/TDD-Example/blob/68920b6ccf6051cdf670d60c8b50926eaf3fc8eb/is_prime.py)

### Intermediary Step: Regression Testing
Regression testing is writing tests for you code AFTER you write it. Usually we don't want to do this, however, sometimes it happens like in the step above we happened to handle negative numbers as well. So, lets now write `passing` tests for those cases as well. I will also add test cases for a few other prime/non-prime numbers to attempt to cover more bases. Again, these tests should all pass.

You can browse the new tests here: [613ade5](https://github.com/Acher0ns/TDD-Example/blob/613ade50384c22953a96e090959abde0f89b04ff/is_prime_test.py)

### Intermediary Step: Refactoring
Wait. Another step? I thought we were done! Wrong! Code can almost always be improved! What happens if we want to check if a REALLY large number is prime? If we want to test a number like 433494437 is prime we will have to check if every number from 2 to that number can evenly divide it to see if its prime. This will take too long. BUT there is a way we can simplify this. I won't go into the math but it turns out we only need to check numbers from 2 up to the square root of the number we are trying to check. So lets change out code to implement this improve ment.

You can browse the new code here: [9573564](https://github.com/Acher0ns/TDD-Example/blob/9573564845c61b5754615608c82231ceb4faee51/is_prime.py)

Notice: All the tests still pass!

### Final Step: Finish The Assignment
Now we have our `is_prime` function implemented, we can implement `main` to prompt a user for a number and print if that number is prime or not and should continue to prompt until the user inputs a number less than 1.

Normally we do not need to test `main` functions and in this case we can since it is taking input and we haven't learned how to test that.

You can browse the new code here: [9408cd5](https://github.com/Acher0ns/TDD-Example/blob/9408cd50e47ea84b909e4af91fba2936ebaf3fd7/is_prime.py)