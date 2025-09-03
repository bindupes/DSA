# Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

#Examples:
#Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
#Output: 22
#Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.

def circularSubarraySum(arr):
    n = len(arr)
    maxsum = arr[0]
    minsum = arr[0]
    result = arr[0]

    for i in range(1, n):
        maxsum = max(arr[i], maxsum + arr[i])
        minsum = min(arr[i], minsum + arr[i])
        result = max(result, maxsum)

    total_sum = sum(arr)
    
    # Handle the case where all elements are negative
    if total_sum == minsum:
        return maxsum

    circular_sum = total_sum - minsum
    return max(maxsum, circular_sum)

# Test cases
print(circularSubarraySum([8, -8, 9, -9, 10, -11, 12]))  # Output: 22
print(circularSubarraySum([-3, -2, -1]))  # Output: -1
