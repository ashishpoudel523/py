#multiplication in reverse order

inp = int(input("Enter a number :\n"))

for i in range(10, 0, -1):
    print(f"{inp} X {i} = {inp*i}")