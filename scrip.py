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

test.login(email,passw)
test.sendmail(email, email1, "Subject: Test Email: \n This is Sample Email 2")
test.quit()
print("Email Sent Sucessfully!")