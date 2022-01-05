#sum of n natural nums using recursion

def add(n):
    if n!=0:
        return add(n-1) + n
    else:
        return n

num = int(input("Enter a number \n:"))
print(add(num))