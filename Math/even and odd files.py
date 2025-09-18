'''
i have a files , now i need to carrange all even files and old files seperately in folders '''

import os

for f in os.listdir("files"):
  num = int(''.join(filter(str.isdigit,f)))
  if num % 2==0:
    os.rename("files/"+f,"files/even/"+f)
    else:
    os.rename("files/"+f,"files/odd/+f)
 
