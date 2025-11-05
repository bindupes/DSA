count =0
num=2

while count<15:
  is_prime=True
  for i in range(2,num):
    if num%i==0:
      is_prime=False
      break
  if is_prime:
    print(num,end=" ")
    count +=1
  num+=1
      
