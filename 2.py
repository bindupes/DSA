#You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
class Solution:
 def pushZerosToEnd(self,arr):
        non_zero = 0 #pointer
        for i in range(len(arr)):
    	    if arr[i] != 0:
                arr[non_zero],arr[i]=arr[i],arr[non_zero]
                non_zero +=1
        return arr
solution = Solution()
print(solution.pushZerosToEnd([1,0,2,0,4,0,0]))