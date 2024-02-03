import math

nextNumber = None

def isPalindrome(num):
    return num == num[::-1]

def convertNumber (number, radix):
    if number == 0:
        return '0'

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        remainder = number % radix
        result = digits[remainder] + result
        number //= radix

    return result

def nextPalindrome (number, radix, result):
    if number < 0 or radix < 2 or radix > 36:
        return 0
    while True:
        number += 1
        if number > 2**64 - 1:
            return 0
        convertedNumber = convertNumber(number, radix)
        if isPalindrome(convertedNumber):
            result[0] = number
            return 1
        
next = [0]
assert nextPalindrome(123, 10, next) == 1 and next[0] == 131
assert nextPalindrome(188, 10, next) == 1 and next[0] == 191
assert nextPalindrome(1441, 10, next) == 1 and next[0] == 1551
assert nextPalindrome(95, 15, next) == 1 and next[0] == 96
assert nextPalindrome(45395, 36, next) == 1 and next[0] == 45431
assert nextPalindrome(1027, 2, next) == 1 and next[0] == 1057
assert nextPalindrome(1000, 100, next) == 0 and next[0] == 1057
assert nextPalindrome(18446744073709551614, 2, next) == 1 and next[0] == 18446744073709551615
assert nextPalindrome(18446744073709551615, 2, next) == 0 and next[0] == 18446744073709551615

print("All assertions passed!")