//How are duplicates removed from a given array in  python?  

arr=[1,2,2,3,4,4,5]
seen=set()
unique=[]

for num in arr:
    if num not in seen:
        unique.append(num)
        seen.add(num)
