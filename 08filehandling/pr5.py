words =["donkey", "mc", "bastard"]
with open("E:/python/08/words.txt") as f:
    a = f.read()

for word in words:
    a = a.replace(word, "*****")
    
    with open("E:/python/08/words.txt", "w") as f:
        f.write(a)