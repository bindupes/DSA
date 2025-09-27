'''Write a Python function that takes a list of numbers and returns the sum of all digits of all numbers in the list.

Example:

Input: [12, 34, 5]
Output: 1+2 + 3+4 + 5 = 15
'''

# there are two technique  1) string technique  2) modulo technique
# string technique

def sum_of_digits(nums):
    total =0
    for num in nums:
        for digit in str(num):
            total += int(digit)
    return total
    
print(sum_of_digits([12,34,5]))


# modulo technique
def sum_of_digits(nums):
    total =0
    for num in nums:
        while num>0:
            total += num%10
            num = num//10
    return total 
