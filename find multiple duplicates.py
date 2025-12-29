//How do you find duplicate numbers in an array if it  contains multiple duplicates 
def find_duplicates(arr,target):
  duplicates=set()  //if there are more than two duplicates , then we use this to make sure only only the duplicate nubmer is added , it has duplicate numbers 
  seen=set()   //unique number firstly goes in here
  for num in arr:
    if num in seen:
      duplicates.add(num)
    seen.add(num)
  return duplicates
