# ==========================================
# Practice Problem: The "Number Game" Score Calculator
# ==========================================
#
# Description:
# Write a Python program that takes a positive integer from the user and calculates a "Total Score" 
# by looping through a sequence of numbers and applying a specific set of mathematical rules.
#
# Instructions:
# 1. Ask the user to enter a positive integer `n`.
# 2. Create a variable named `total_score` starting at 0.
# 3. Use a `for` loop and `range()` to iterate through all numbers from 1 up to and including `n`.
# 4. For each number, apply these rules:
#    - Divisible by BOTH 2 and 3: add 15
#    - Divisible ONLY by 2: add 5
#    - Divisible ONLY by 3: subtract 2
#    - All other numbers: add 1
# 5. Display the final score using an f-string.
#
# ------------------------------------------
# Example 1:
# Input: n = 6
# Output: Final Score: 25
# Explanation: 
# 1 (+1)  -> 1
# 2 (+5)  -> 6
# 3 (-2)  -> 4
# 4 (+5)  -> 9
# 5 (+1)  -> 10
# 6 (+15) -> 25
#
# Example 2:
# Input: n = 3
# Output: Final Score: 4
# Explanation: 
# 1 is not divisible by 2 or 3 (+1).
# 2 is divisible by 2 (+5).
# 3 is divisible by 3 (-2). 
# Total = 1 + 5 - 2 = 4.
#
# Example 3:
# Input: n = 10
# Output: Final Score: 34
# Explanation: 
# Score for 1 to 6 is 25. 
# 7 (+1) = 26
# 8 (+5) = 31
# 9 (-2) = 29
# 10 (+5) = 34
# ------------------------------------------
#
# Constraints & Rules:
# - You must use a `for` loop and `range()`.
# - Do not use a `while` loop or any lists.
# - Use only `if`, `elif`, `else`, logical operators (`and`), and modulus (`%`).
#
# Problem-Solving Hints (IPO Method):
# - Input: Use `int(input(...))` to convert the string input into an integer.
# - Loop: `range(start, stop)` excludes the stop value. Set your stop value to include `n`.
# - Logic: The strictest condition (divisible by both) MUST come first in your `if-elif-else` chain.
#
# ==========================================
# SOLUTION BELOW
# ==========================================

n = int(input("Enter a positive integer: "))

total_score = 0

for i in range(1, n + 1):
    
    if i % 2 == 0 and i % 3 == 0:
        total_score = total_score + 15
    elif i % 2 == 0:
        total_score = total_score + 5
    elif i % 3 == 0:
        total_score = total_score - 2
    else:
        total_score = total_score + 1

print(f"Final Score: {total_score}")