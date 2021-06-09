marks = int(input("Enter your marks: \n"))
if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B" 
elif marks>=60:
    grade = "C"
else:
    grade = "Fail"

print(grade)