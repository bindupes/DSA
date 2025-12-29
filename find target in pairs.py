//How do you find all pairs of an integer array whose  sum is equal to a given number?  

def find_pairs(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    pairs=[]
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            pairs.append((arr[left],arr[right]))
            left+=1
            right-=1
        elif sum<target:
            left+=1
        else:
            right-=1
    return pairs
