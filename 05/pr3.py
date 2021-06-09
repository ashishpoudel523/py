com = input("Enter the comment \n")


if("make a lot of money"  in com):
    spam = True
elif("buy now" in com):
    spam = True
elif("subscribe his" in com):
    spam =  True
elif("click this" in com):
    spam = True
else:
    spam = False

if(spam):
    print("This is spam")
else:
    print("This is not spam")
