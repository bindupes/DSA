#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
class Solution:
 def getSecondLargest(self, arr):
        lar=second_lar=-1
        for num in arr:
            if num>lar:
                second_lar=lar
                lar=num
            elif num>second_lar and num<lar:
                second_lar = num
        return second_lar
solution=Solution()      
print(solution.getSecondLargest([20,10,30,40]))

#OR
''' def getSecondLargest(arr):
        lar=second_lar=-1
        for num in arr:
            if num>lar:
                second_lar=lar
                lar=num
            elif num>second_lar and num<lar:
                second_lar = num
        return second_lar
    print(getSecondLargest([20,10,30,40]))
 '''