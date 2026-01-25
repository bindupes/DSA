class Solution():
    def inversion(self,arr):
        n=len(arr)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if arr[j]>arr[i]:
                    count +=1
        
        return count

solution = Solution()
print(solution.inversion([2,4,1,3,5]))


