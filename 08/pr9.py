f1 = "E:/python/08/ap1hd.txt"
f2 = "E:/python/log_copy.txt"

with open(f1) as f:
     a = f.read()
with open(f2) as f:
     b = f.read()


if a == b:
    print("identical")
 
else:
    print("Different files")