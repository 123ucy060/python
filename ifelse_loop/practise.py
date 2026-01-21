"""🔥 TASK 1 – Smart Login System (Nested + Logical)
🧠 Scenario

A system checks username, password, OTP, and account status.

📥 Input
username = "admin"
password = "Admin@123"
otp = 4321
account_active = True

📌 Conditions

1️⃣ If username and password are correct
2️⃣ If account is active
3️⃣ If OTP is correct
4️⃣ Else show proper error message

✅ Expected Output
Login successful
"""

 

username = input("Enter username: ")
account_active = True

if username != "admin":
    print("Username incorrect")

else:
    password = input("Enter password: ")

    if password != "1234":
        print("Password incorrect")

    else:
        otp = int(input("Enter OTP: "))

        if otp != 4545:
            print("OTP incorrect")

        elif not account_active:
            print("Account inactive")

        else:
            print("Login successful")
