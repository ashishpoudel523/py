maths =  int(input("Enter your marks in Maths: \n"))
science = int(input("Enter your marks in Science: \n"))
gk  = int(input("Enter your marks in GK: \n"))  

if(maths<33 or science<33 or gk<33):
    print("Fail")

elif(maths+science+gk)/3 <40:
    print("fail")
else:
    print("Passed")
