with open("E:/python/08/log.txt") as f:
    c = f.read()

if 'python' in c.lower():
    print("Exists")
else:
    print("Don't exist")