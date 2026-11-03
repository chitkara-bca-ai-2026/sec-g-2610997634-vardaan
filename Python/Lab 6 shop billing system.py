print("==========================================================")
print("           CLOTHING STORE BILLING SYSTEM")
print("==========================================================")
name=input("Enter Customer Name:")
garment=input("Enter Garment Name:")
price=float(input("Enter Price Of One Garment:"))
quantity=int(input("Enter Number Of Garments:"))

Total_Amount=price*quantity

print("==========================================================")
print("                         BILL")
print("==========================================================")

print("Customer Name :",name)
print("Garment Name :",garment)
print("Price per Unit :",price)
print("Quantity :",quantity)
print("Total Amount :",Total_Amount)
print("==========================================================")