import os 

old =  "E:/python/08/old.txt"
new = "E:/python/08/new.txt"

with open(old) as f:
    content = f.read()

with open(new , "w") as f:
    f.write(content)

os.remove(old)