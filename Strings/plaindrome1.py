class Three(object):
    def longest_palindrome(self,s):
        max_length=0
        start_index=0
        for i in range(1,len(s)-1):
            left= i-1
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                
            length = right-left-1
            if length >max_length:
                max_length =length
                start_index = left+1
                
        return s[start_index:left+1-right]
        
        
                
sol = Three()
print(sol.longest_palindrome("cbba"))
