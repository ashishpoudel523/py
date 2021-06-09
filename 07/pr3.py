def mul_table(n, i=1):
    print (str(n) + " * " + str(i) + " = " + str(n*i))
    if i != 10:
        mul_table(n,i+1)
mul_table(6) 