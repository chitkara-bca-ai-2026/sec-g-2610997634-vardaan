print("========================================================")
print("          ENGINEERING CALCULATION TOOL")
print("========================================================")
value=float(input("Enter a numerical value :"))
exponent=float(input("Enter a exponent :"))
measurement=float(input("Enter a decimal measurement :"))

print("----Result----")
import math
import math as f
Power=(f.pow(value,exponent))
Square_Root=(f.sqrt(value))
Ceil_value=(f.ceil(measurement))
Floor_value=(f.floor(measurement))


print("Value :",value)
print("Exponent :",exponent)
print("Power :",Power)
print("Square_Root :",Square_Root)
print("Decimal_Value",measurement)
print("Ceil_value",Ceil_value)
print("Floor_Value",Floor_value)

print("========================================================")