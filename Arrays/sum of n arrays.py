class AnyArray(object):
  def sum_arrays(self,*arrays):
    max=max(len(arr) for arr in arrays)
    padded = [arr + 0* (max_len- len(arr) for arr in arrays)
    result =[]
    for i in range(max_len):
        s=0
        for arr in padded:
          s+=arr[i]
    result.append(s)   
sol = AnyArray()
print(sol.sum_arrays([1,2,3],[4,5,6]))
    
    
