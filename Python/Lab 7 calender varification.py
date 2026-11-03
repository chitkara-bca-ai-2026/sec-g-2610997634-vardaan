print("============================================")
print("     calender verification system")
print("============================================")
year = int(input("enter year :"))
leap=("leap year:")
if year >=0:
    print("error: year must be positive integer")
else:
 if year%100==0:
       if year%400==0:
          leap=True
          reason="century year divisible by 400"
       else:
           leap=False
           reason="century year not divisible by 400"
 elif year % 4==0:
      leap=True
      reason="divisible by 4 and not a century year"
 else:
    leap= False
reason="divisible by 4"
print("============================================")
print("year:",year) 

if leap:
    print("status:LEAP YEAR")
    print("Days in year:366 days")
    print("days in faburary:29 days")     
else:
    print("status: COMMON YEAR")
    print("days in year:365 days")
    print("days in faburary:28 days")


print("reason:",reason)
print("============================================")