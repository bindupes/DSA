#You are given an array of integers arr[]. Your task is to reverse the given array.
def reverseArray(arr):
    left = 0
    right = len(arr)-1
    while left < right :
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr

print(reverseArray([1,4,3,2,6,5]))
 