class Three(object):
    def sum_arrays(self,arr1,arr2,arr3):
        max_len = max(len(arr1),len(arr2),len(arr3))
        arr1 = arr1 + [0]*(max_len - len(arr1))
        arr2 = arr2 +[0]*(max_len - len(arr2))
        arr3 = arr3 +[0]*(max_len - len(arr3))
        result = [arr1[i]+arr2[i]+arr3[i] for i in range(max_len)]
        return result 
    
sol = Three()
print(sol.sum_arrays([1,3,5],[1,3,5],[1,3,5]))    
