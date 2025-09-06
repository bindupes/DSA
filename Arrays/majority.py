#You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 
#Note: The answer should be returned in an increasing format.

class Solution:
    def findMajority(self,arr):
        n=len(arr)
        count_map={}    # we will store num:count in dictionary 

        for num in arr:
            if num in count_map:
                count_map[num]+=1
            else:
                count_map[num]=1
        
        result=[]
        for num,count in count_map.items():
            if count > n/3:
                result.append(num)
        result.sort()
        return result 
    
solution = Solution()
print(solution.findMajority([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))

