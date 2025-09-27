''' write the code to find the prime numbers in array and give a new list"
def prime(nums):
    arr=[]
    for num in nums:
        if num>1:
            for j in range(2,num):
                if num%j==0:
                    break
            else:
                arr.append(num)
    return arr
    
print(prime([2,3,4,5,6,7,8]))
