ams(str1,str2#Given two strings s1 and s2 consisting of lowercase characters.
#The task is to check whether two given strings are an anagram of each other or not. 
# An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
# For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

def anagrams(str1,str2):
    if len(str1) != len(str2):
        return False
        
    freq={}
    for char in str1:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
        
    for char in str2:
        if char not in freq:
            return False
        freq[char]-=1
        if freq[char]<0:
            return False
            
    return True


str1="listen"
str2="silent"
print(anagrams(str1,str2))


( OR ) 

str1="listen"
str2="silent"

str1=sorted(str1)
str2=sorted(str2)

if str1==str2:
    print("True")
else:
    print("False")
        
 
