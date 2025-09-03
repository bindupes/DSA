#You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
#Note: Positive number starts from 1. The array can have negative integers too.
#Examples:
#Input: arr[] = [2, -3, 4, 1, 1, 7]
#Output: 3
#Explanation: Smallest positive missing number is 3.

def missingNumber(arr):
        n= len(arr)
        m=[]
        for i in range(n):
            if arr[i]>0:
                m.append(arr[i])
        m=sorted(set(m))    
        minimum = 1
        for num in m:
             if num==minimum:
                  minimum += 1
        
        return minimum
print(missingNumber([1,2,3,4,5]))
             
            


