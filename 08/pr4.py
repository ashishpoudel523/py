with open("E:/python/08/ap1hd.txt") as f:
    content = f.read()

content = content.replace("donkey", "*****")

with open("E:/python/08/ap1hd.txt", "w") as f:
    f.write(content)