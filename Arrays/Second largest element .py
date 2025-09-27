# Find the second largest number in the array

def second_largest(arr):
    first = second = float('-int')
    for nums in nums:
        if num > first:
            second = first
            first = num
        elif num >second and num!=first:
            second = num
    return second 

    
        
        
OR 

def second_largest(arr):
    arr.sort()
    largest=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i]!=largest:
            return arr[i]
    return None
