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
Can you give me 5 problems to do with example, to help me learn variables and basic data types:
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




problem 2: FizzBuzz
Write a function called fizzbuzz(n) that prints the numbers from 1 to n. But for multiples of 3, 
print "Fizz" instead of the number. For multiples of 5, print "Buzz". For numbers which are multiples of both
 3 and 5, print "FizzBuzz".

problem 3: Write a function count_vowels(s) 
that takes a string and returns the number of vowels (a, e, i, o, u) in the string.

problem 4: Write a function find_largest(nums) 
that takes a list of numbers and returns the largest one without using max().

problme 5:Write a function reverse_list(lst) 
that takes a list and returns a new list thats reversed. Do not use [::-1] or .reverse().
"""









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

print("\nTesting Problem 2: Fuzz Ball")
number= int(input("How many numbers?"))
def Fuzz_Ball(x):
    for i in range(1, x + 1):
        hold= i
        print(str(hold))
        if i % 3==0 and i%5 != 0:
            print("Fizz")
            hold+=1
        if i % 5 == 0 and i %3 != 0:
            print("Buzz")
            hold+=1
        if i%3 ==0 and i%5==0:
            hold=+1
            print("FizzBall")
Fuzz_Ball(number)
print("\nTesting Problem 3: Count Vowels")
hold= 0
def count_Vowels(x):
    x.lower()
    for i in len(str(x)):
        if x[i]=="a" or "u" or "i" or "e" or "o":
            hold+=1
    return hold

print("\nTesting Problem 4:largest number")
number=[1,2,5,3,1,4,0]
hold= 0
def largest_Num(number):
    for i in len(number):
        if number[i]>hold:
            hold=number[i]
    return hold



print("\nTesting Problem 5: Reserves list")
list=[1,9,8,2,3]
new_List=[]
hold=0
def reverse_List(list):
    hold= len(list) 
    for i in len(list):
        new_List[i]= list[hold]
        hold=-1
    return new_List

