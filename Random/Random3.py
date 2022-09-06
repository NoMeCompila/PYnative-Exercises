"""
Generate 6 digit random secure OTP
"""

import secrets


generator = secrets.SystemRandom()

otp = generator.randrange(10000, 99999)

print(otp)