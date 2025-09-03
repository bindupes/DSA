#Given a string s , the objective is to convert it into integer format without utilizing any built-in functions . 
#Cases for atoi() conversation : 
#1) Skip any leading whitespaces.
#2) Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
#3) Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
#4) If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.


class solution :
    def myAtoi(self , s):
        s=s.strip()    # this will remove all the whitespacess
        if not s:       # if its not a string then return 0
            return 0
        
        sign =1   # by default sign is positive 
        if s[0] in ['-','+']:  # if sign is negative then sign is -1
            if s[0]=='-':
                sign =-1
        s=s[1:]   # extract the string leaving the signs to convert to digits

        result =0
        for char in s:
            if char.isdigit():
                result = result * int(char)
            else:
                break 

        result*=sign
        INT_MAX = 2**31 -1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result 

        