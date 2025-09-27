'''
Write a Python function that counts the frequency of each character in a string and returns the result as a dictionary.

Example:

Input: "programming"
Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
'''

def frequency(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
