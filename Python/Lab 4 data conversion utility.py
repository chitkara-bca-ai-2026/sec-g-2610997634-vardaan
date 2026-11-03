print("======================================================")
print("         DATA CONVERSION UTILITY  ")
print("======================================================")

product_name=input("Enter Product name :")
price=float(input("enter price :"))
quantity=int(input("enter quantity :"))

total_price=price*quantity
amount_str=str("total_pirce")

print("-----------------------------------------------------")
print("           TYPE CASTING SUMMARY ")
print("-----------------------------------------------------")
print(''' "variable"    "value"        "python type"''')
print("-----------------------------------------------------")


print("product_name",   product_name,   type(product_name))
print("price",          price,          type(price))
print("quantity",       quantity,       type(quantity))
print("total_price",    total_price,    type(total_price))
print("amount_str",     amount_str,     type(amount_str))
print("-----------------------------------------------------")

print("-----------------------------------------------------")
print("           TAX INVOICE ")
print("-----------------------------------------------------")

print("Product_name :",product_name)
print("Price : Rs",price)
print("Quantity :",quantity)
print("-----------------------------------------------------")
print("Invoice_total : Rs",amount_str)
print("======================================================")