# for pattern
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print("\n")






# for pattern 
# *****
# ****
# ***
# **
# *
for k in range(5, 0, -1):
    for l in range(1, k+1):
        print("*", end=" ")
    print("\n")




# for pattern
#     *
#    **
#   ***
#  ****
# *****
for a in range(1, 6):
    for b in range(1, 6-a):
        print(" ", end="")
    for c in range(1, a+1):
        print("*", end="")
    print("\n")


# for pattern
# *****
#  ****
#   ***
#    **
#     *

for d in range(5, 0, -1):
    for e in range(1, 6-d):
        print(" ", end="")
    for f in range(1, d+1):
        print("*", end="")
    print("\n")


# for pattern 
#     *
#    ***
#   *****
#  *******
# *********


for f in range(1,6):
    for g in range(1, 6-f):
        print(" ", end="")
    for h in range(1, (2*f-1)+1):
        print("*", end="")
    print("\n")



for f in range(5, 0, -1):
    for g in range(1, 6-f):
        print(" ", end="")
    for h in range(1, (2*f-1)+1):
        print("*", end="")
    print("\n")



# Python Program to Print Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()