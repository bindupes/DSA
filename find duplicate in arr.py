def duplicate(arr):
  seen=set()
  for num in arr:
    if num in seen:
      return num
    seen.add(num)
    
