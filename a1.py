# Assignment 1: AI-Generated Python Problems
# Name: [Nyleah Jones]

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
I am a highschool student who has taken AP CSA, but Ive dabbled a little bit in python. 
Can you give me 5 problems to do, to help me learn variables and basic data types:
 conditionals(if/elif/else), loops(for and while), functions, and basic list operations.

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Temperature Converter
Write a program that:

Asks the user to input a temperature in Celsius

Converts it to Fahrenheit using the formula: F = (C * 9/5) + 32

Prints the result in a formatted message

    Example:
        Enter temperature in Celsius: 25
        25°C is 77.0°F
ccccc

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""
number= int(input("Enter temperature in Celsius:"))
Fahr= (float(number) * 9/5 ) +32
print(str(number) +" Degrees Celsius is "+ str(Fahr)+ " Fahrenheit")








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
number= int(input("Enter temperature in Celsius:"))
Fahr= (float(number) * 9/5 ) +32
print(str(number) +" Degrees Celsius is "+ str(Fahr)+ " Fahrenheit")

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


