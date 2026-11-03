print("==========================================================================")
print("                  SCHOOL RESULT PROCESSING")
print("==========================================================================")
name=input("Enter Student Name :")
roll_no=int(input("Enter Roll Number :"))
marks=[]
failed=False

print("----Enter Marks For 5 Subjects (0-100)----")
for i in range(1,6):
    mark=float(input("Enter marks for Subject {i} (0-100):"))

    if mark<0 or mark>100:
        print("Error")
        exit()
    marks.append(mark)
    if mark<40:
        failed=True



total_marks=sum(marks)
percentage=(total_marks/500)*100

if failed:
    result="FAIL"
    grade="F"
    remark="Failed in one or more subjects"
else:
    result="PASS"
    
    if percentage>=90:
        grade="A+"
        remark="Outstanding"
    elif percentage>=80:
        grade="A"
        remark="Excellent"
    elif percentage>=70:
        grade="B"
        remark="Very Good"
    elif percentage>=60:
        grade="C"
        remark="Good"
    elif percentage>=50:
        grade="D"
        remark="Satisfactory"
    else:
        grade="E"
        remark="Pass"

print("==========================================================================")
print("                      STUDENT REPORT CARD")
print("==========================================================================")
print("Student Name :",name)
print("Roll Number :",roll_no)
print("-------------------------------------")
print("Total Marks :",total_marks,"/500")
print("Percentage :",percentage,"%")
print("Result :",result)
print("Grade :",grade)
print("Remarks :",remark)
print("==========================================================================")