import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("Email")
email1= os.getenv("Email1")
passw = os.getenv("py_password")
test= smtplib.SMTP('smtp.gmail.com', 587)
test.ehlo()
test.starttls()

message = """ 
Subject: Application - Fresher- Hariprasath M

Dear Hiring Team,

I am excited to apply for the at Analyst PPM EBOM at Ford India Pvt. Ltd.

My name is Hariprasath, and I am a recent graduate in Electronics and Communication Engineering (B.E., 2025) from Karpaga Vinayaga Collage of Engineering and Technology.
With a strong academic foundation and hands-on experience in Python, SQL, Ms Office (Excel, Word, PowerPoint), Digital Electronics and Networking. And Good in Communication, Problem-Solving, Logical Thinking. I believe I would be strong fit for this role.

I have attached my resume for your review. I would be grateful for the opportunity to discuss how my background and enthusiasm can contribute to your team.
Thank you for your time and consideration. I look forward to the possibility of hearing from you.

Best regards,

Hariprasath M
Mobile: 9360073685
Email: hariprasathprem@gmail.com
"""

test.login(email,passw)
test.sendmail(email, email1,message)
test.quit()
print("Email Sent Sucessfully!")
