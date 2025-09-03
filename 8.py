# Given an integer array arr[]. You need to find the maximum sum of a subarray.
# make sure its continous numbers sum should be maximum 

def max_subarray_sum(arr):
    n=len(arr)
    current_sum=arr[0]
    max_sum=arr[0]

    for i in range(1,n):
        current_sum = max(arr[i],current_sum+arr[i]) # if the current number is greater or current_sum+arr[i] is greater 
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray_sum([1,2,3,-2,5]))


    
