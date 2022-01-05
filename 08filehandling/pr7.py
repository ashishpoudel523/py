c =True
i = 1
with open("E:/python/08/log.txt") as f:
    while c:
        
        c = f.readline()
        if 'python' in c.lower():
            print(c)
            print(f"Exists on line {i}")
            print(i)
        
        i+=1