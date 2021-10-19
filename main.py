## Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is (4/3) πr^3
import math

def vol(rad):
    return (4/3) * math.pi * (rad ** 3)

print(vol(2))





## Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num >= low and num <= high:
        print("{} is in the range between {} and {}".format(num, low, high))
        return True
    else:
        print("{} is NOT in the range between {} and {}".format(num, low, high))
        return False

print(ran_check(5,2,7))
print(ran_check(13,1,10))





## Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!


def up_low(s):
    up = 0
    low = 0
    for letter in s:
        if letter.isupper():
            up += 1
        elif letter.islower():
            low += 1
        else:
            continue
    return "No. of upper case characters: {} \nNo. of Lower case characters: {}".format(up, low)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))





##Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1, 2, 3, -4]
#Expected Output : -24

def multiply (numbers):
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(multiply([1,2,3,-4]))




## Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

def palindrome(s):
    check = True
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            check = False
            break
    return check

print(palindrome('helleh'))
print(palindrome('hello'))





## Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string
def ispangram (str1, alphabet = string.ascii_lowercase):
    return set(alphabet) == set(str1.replace(" ", "").lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Hello World"))
