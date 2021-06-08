
import smtplib

my_email = "study.practice.smtp@gmail.com"
password = "@Zoya051217"
to_email = "studypracticesmtp@yahoo.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg="Subject:Hello\n\nThis is a test mail")




