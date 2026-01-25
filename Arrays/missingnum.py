#You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
#Note: Positive number starts from 1. The array can have negative integers too.
#Examples:
#Input: arr[] = [2, -3, 4, 1, 1, 7]
#Output: 3
#Explanation: Smallest positive missing number is 3.

def missingNumber(arr):
        positives=set()
        for num in arr:
                if num>0:
                        positives.add(num)
        i=1
        while True:
                if i not in positives:
                        return i
                i+=1
print(missingNumber([1,2,3,4,5]))
             
            



