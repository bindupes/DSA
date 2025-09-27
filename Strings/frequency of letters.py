Write a Python function that counts the frequency of each character in a string and returns the result as a dictionary.

def char_frequency(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
