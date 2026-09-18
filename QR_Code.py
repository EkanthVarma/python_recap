import segno

# Developer Profile Details
profile = """
================================
        DEVELOPER PROFILE
================================

Name: Seera Ekanth Varma

Role: Python Full Stack

Skills:
Python
SQL
HTML
CSS
JavaScript
React

Email:
ekanthvarma2005@gmail.com

LinkedIn:
https://www.linkedin.com/in/ekanthvarmaseera/

GitHub:
https://github.com/EkanthVarma

================================
        THANK YOU!
================================
"""

# Create QR Code
qr = segno.make(profile)

# Save QR Code
qr.save("developer_profile.png", scale=10)

print("Developer Profile QR Code Created Successfully!")
