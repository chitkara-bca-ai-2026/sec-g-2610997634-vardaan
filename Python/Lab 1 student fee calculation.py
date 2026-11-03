tution_fee=int(input("Enter Tution Fee: "))
lab_fee=int(input("Enter Lab Fee: "))
library_fee=int(input("Enter Library Fee: "))
exam_fee=int(input("Enter Exam Fee: "))


#discount

dis=2000

#calculate total fee before discount 

Total_Fee=tution_fee + library_fee + lab_fee + exam_fee

#total fee after discount 

Fee_after_Discount=Total_Fee-dis

#yearly amount

Annual_Fee=Fee_after_Discount*2

#monthly amount 

Monthly_Installment=Annual_Fee/12
print("Tution Fee :",tution_fee)
print("Lab Fee :",lab_fee)
print("Library Fee :",library_fee)
print("Exam Fee :",exam_fee)
print("Total Fee :",Total_Fee)
print("Discount :",dis)
print("Fee after Discount :",Fee_after_Discount)
print("Annual Fee :",Annual_Fee)
print("Monthly Installmentt",Monthly_Installment)