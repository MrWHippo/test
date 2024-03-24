
entered_password = "password223"

admin_password = "password123"

if entered_password == admin_password:
    print("Password Correct \nLogging Admin In")
else:
    raise ValueError("Entered Password Does Not Match Admin Password")

print("Hello")