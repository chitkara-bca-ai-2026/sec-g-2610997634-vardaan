username=input("Enter your username :")
password=input("Enter your password :")

print("======================================================")
print("         PASSWORD VALIDATION REPORT")
print("======================================================")
print("Username :",username)
print("Password :",len(password))

length_valid=len(password)>=8
digit_valid=any(chr.isdigit() for chr in password)
uppercase_valid=any(chr.isupper() for chr in password)

print("---Validation Rules---")

if length_valid:
    print(f"[PASS] Minimumn 8 characters({len(password)}characters)")
else:
    print(f"[FAIl] Minimum 8 characters")

if digit_valid:
    print(f"[PASS] At least one digit")
else:
    print(f"[FAIL] At least one digit")

if uppercase_valid:
    print(f"[PASS] At least one uppercase")
else:
    print(f"[FAIL] At least one uppercase")


print("---Result---")

if length_valid and digit_valid and uppercase_valid:
    print("Passwrd is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("======================================================")