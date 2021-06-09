f = open('E:/python/08/poem.txt')
t = f.read()
if 'sabailai' in t:
    print("present")
else:
    print("Not present")
f.close()