class Solution():
    def inversion(self,arr):
        n=len(arr)
        count=0
        for i in range(0,n-2):
            for j in range(1,n-1):
                if arr[i]>arr[j]:
                    count +=1
                
                else:
                    return 0
        
        return count

solution = Solution()
print(solution.inversion([2,4,1,3,5]))

