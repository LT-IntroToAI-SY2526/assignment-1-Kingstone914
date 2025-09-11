# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[I'm a highschool student taking an intro to ai class. I'm starting to learn the basics of python and I'm completely new to programming. Generate 5-7 practice problems about difference lists, factorial, names, writing functions, and greetings.]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Factorials
Write a function called factorial(n) that takes a positive integer n and returns the factorial of n.

factorial(4)  # returns 24 because 1*2*3*4=24
"""
def factorial (n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result
print(factorial(4))

""""
Problem 2: lists
Write a function called difference that:

Takes two numbers as parameters.

Returns the absolute difference between the two numbers (i.e., always a positive value).
Ex:difference(10, 4)  # returns 6
   difference(3, 7)   # also returns 4

"""
def difference(a,b):  # this makes a and b inputs which are the numbers that are getting carried out
    result = abs(a-b) #I used this function to maintain a postive difference because I dont want negatives for this
    return result  #This function is to output the difference
print(difference(76,54))  #this function is to finish off the code by printing the difference between the numbers 76 and 54

"""
Problem 3: Writing an function for greeting
For example, you might want it to say:

Hello, welcome!


Or maybe:

Hi, Sarah!

"""
def greet(name):  # this creates a function which is where the code is going under
    print("hello, " + name + "!") # this connects all the strings making a string concatention which basically means that it's joining hello, name, and ! together.
greet("Kingston") # this is to define my name as Kingston. It's like the greet(name) in the function but this time (name) is Kingston

"""
Problem:4
"""


# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")



print("\nTesting Problem 2:")


print("\nTesting Problem 3:")




print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


""