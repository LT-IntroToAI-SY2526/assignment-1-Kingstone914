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
[I'm a highschool student taking an intro to ai class. I'm starting to learn the basics of python and I'm completely new to programming. Generate 3-5 practice problems about difference lists, functions, writing a sentence, factorial and greetings.]

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
def factorial (n): # this creates an function and sets the inputs which is n
    result = 1  # this stores 1 into result which basically is to remember the value
    for i in range(1,n + 1): # this is creating a loop which starts at 1 and ends on n
        result *= i # this multiplys result and i and store it back into result
    return result # sends factorial value back so it can be printed in the next line
print(factorial(4)) # this is giving n an value which is 4 in this case.

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
Problem:4: Writing an function


Let’s think it through step-by-step:

Your function needs two inputs (two numbers).

If the second number is zero, return the string "Cannot divide by zero".

Otherwise, return the result of dividing the first number by the second.
"""
def number(a,b):  # this is setting the input (a,b) and creating an function
    if b == 0: # this and the line below makes it where if the number is divided by 0 then make the answer 0. It's like an if then statement in scratch but with words.
        return 0
    else:  #This and the line below makes it where if b is not 0 then divide a and b. The else is like the alternative outcome to the if statement.
        return a / b
print(number(10, 5)) # this is to give a and b a value.

""""
Problem 5:writing an setence
What do you want your function to do?
For example, should it take some words and put them together into a sentence?

What inputs should your function have?
Maybe a person’s name, an action, or a place?

What should the sentence look like?
For example: "Alice loves pizza." or "Bob is going to the park."
"""
def make_sentence(name, activity):  # this is to make a function and set the inputs
    return f"{name} is playing {activity}." # the return sends the value back to where the function was called. The f behind {name} is called an f string. You use an f string to set variables into {} inside the string. This makes it where {name} is name and {activity} is activity with "is playing" as text.
print(make_sentence("Joe", "basketball")) # This gives name = joe and activity = basketball to create an actual sentence.

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
print(factorial(3))
print(factorial(6))
print(factorial(8))

print("\nTesting Problem 2:")
print(difference(10,9))
print(difference(31,20))
print(difference(45,12))

print("\nTesting Problem 3:")
greet("Piero")
greet("Joe")
greet("Jonathan")

print("\nTesting Problem 4:")
print(number(20, 4))
print(number(1450, 50))
print(number(144, 12))

print("\nTesting Problem 5:")
print(make_sentence("Bo", "chess"))
print(make_sentence("Jonathan", "Fifa"))
print(make_sentence("Piero", "volleyball"))


""