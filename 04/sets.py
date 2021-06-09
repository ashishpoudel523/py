b = {4, 6, 3, 7, 9}
print(type(b))
print(b)

a = {} #this makes empty dictionary
print(type(a))

# an empty set can be made using below syntax:
c = set()
print(type(c))

#adding into empty sets
c.add(5)
c.add(7)
c.add(9)
c.add(6) #no repitition

print(len(c))

c.remove(5)

c.pop()  #deletes any one items in sets
c.clear() #deletes all items

# c.remove(15) #throws error
# c.add([3, 5, 7])
# cannot add list or dictionary to  sets
# c.add({3:5})  
print(c)

d = set(("apple", "ball", "cat"))
print(d)

