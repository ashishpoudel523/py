use1  =  int(input("Enter number 1: \n"))
use2  =  int(input("Enter number 2: \n"))
use3  =  int(input("Enter number 3: \n"))
use4  =  int(input("Enter number 4: \n"))

if(use1>use4):
    f1 = use1
else:
    f1 = use4

if(use2>use3):
    f2 = use2
else:
    f2 =  use3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")