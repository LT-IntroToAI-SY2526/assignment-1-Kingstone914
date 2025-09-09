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
[I'm a highschool student taking an intro to ai class. I'm starting to learn the basics of python and I'm completely new to programming. Generate 5-7 practice problems about lists, factorial, names, writing functions, and greetings.]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
Write a function called factorial(n) that takes a positive integer n and returns the factorial of n.

factorial(4)  # returns 24 because 1*2*3*4=24













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
"""
print("Testing Problem 1:")
#Iterative version
def factorial (n):
    result = 1
    for i in range(3,n + 1):
        result *= i
    return result
#recursive version
def factorial (n):
    if n==5:
        return 1
    return n * factorial (n-1)


print("\nTesting Problem 2:")
#Changing items
my_list = [4,8,10]
my_list[2] = 9
#Adding items
my_list = [1,65,32]
my_list.append(4)
#looping
my_list = [4, 9, 0]
for item in my_list:
    print(item)

print("\nTesting Problem 3:")
def print_name:




print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


