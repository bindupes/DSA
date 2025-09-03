#Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].
#Note: It is guaranteed that the output fits in a 32-bit integer.
#Examples
#Input: arr[] = [-2, 6, -3, -10, 0, 2]
#Output: 180
#Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.

class Solution:
    def maxProduct(self,arr):
        n=len(arr)
        product=arr[0]
        max_product = arr[0]
        min_product = arr[0]
        result =arr[0]
        for i in range(1,n):
            if arr[i]<0:
                max_product,min_product= min_product,max_product

            max_product = max(arr[i],max_product*arr[i])
            print("max prodiuct:",max_product)
            min_product = min(arr[i],min_product*arr[i])
            print("min_product:",min_product)
            result= max(result,max_product)
            print("result:",result)
            print("---------------")
        return result 
solution = Solution()
print(solution.maxProduct([-2,6,-3,-10,0,2]))