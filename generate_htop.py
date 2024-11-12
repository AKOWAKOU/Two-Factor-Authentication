import pyotp

# Create a secret key (keep it secret!)̥
secret_key = pyotp.random_base32()

otp = pyotp.TOTP(secret_key, interval=60,digits=10)
# Generate an OTP using TOTP after every 30 seconds
print("Your TOTP is: ", otp.now())

user_otp = input("Enter the OTP: ")
if (otp.verify(user_otp)):
    print("Access granted!")
else:
    print("Incorrect OTP")
