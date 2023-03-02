# Task 
# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.

# Input Format
# Read y, the year that needs to be checked.

# Constraints
# 1900 <= y <= 10**5

# Output Format
# Output is taken care of by the template. Your function must return a boolean value (True/False)

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap
year = int(input())
print(is_leap(year))
