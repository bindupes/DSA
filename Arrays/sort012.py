#Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# without sort function
class Solution:
    def sort012(self,arr):
        sorted_arr=[]
        while arr:
            current = min(arr)
            sorted_arr.append(current)
            arr.remove(current)
        
            while current in arr:
             sorted_arr.append(current)
             arr.remove(current)
        return sorted_arr
        
solution=Solution()
print(solution.sort012([0,1,2,0,1,2]))


# dutch national flag 
class Solution:
    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1  # Step 1

        while mid <= high:  # Step 2
            if arr[mid] == 0:  # Step 3
                arr[low], arr[mid] = arr[mid], arr[low]  # Step 3a
                low += 1  # Step 3b
                mid += 1  # Step 3c
            elif arr[mid] == 1:  # Step 4
                mid += 1  # Step 4a
            else:  # arr[mid] == 2 (Step 5)
                arr[mid], arr[high] = arr[high], arr[mid]  # Step 5a
                high -= 1  # Step 5b

# Example usage
solution = Solution()
arr = [0, 1, 2, 0, 1, 2]
solution.sort012(arr)
print(*arr)









'''
#with sort function 
class Solution:
    def sort012(self,arr):
        a=arr.sort()
        return a
    
solution =Solution()
print(solution.sort012([0,2,1,0]))
'''