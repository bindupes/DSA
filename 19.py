#You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.
#Note: The characters in the strings are in lowercase.
#Examples :
#Input: s1 = "abcd", s2 = "cdab"
#Output: true
#Explanation: After 2 right rotations, s1 will become equal to s2.
#Input: s1 = "aab", s2 = "aba"
#Output: true
#Explanation: After 1 left rotation, s1 will become equal to s2.

class Solution:
    def rotate(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        return s2 in s1+s1
    
solution =Solution()
print(solution.rotate('aab','aba'))