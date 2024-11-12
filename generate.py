import time
import pyotp

# Create a secret key (keep it secret!)̥
secret_key = pyotp.random_base32()

otp = pyotp.TOTP(secret_key)
# Generate an OTP using TOTP after every 30 seconds
while True:
    print(f"Your Time-based OTP at {time.ctime()}:", otp.now())

    time.sleep(10)
