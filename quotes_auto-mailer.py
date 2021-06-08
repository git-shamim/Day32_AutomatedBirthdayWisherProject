
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = "study.practice.smtp@gmail.com"
MY_PASSWORD = "@Zoya051217"


def send_quote():
    if weekday == 0:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="studypracticesmtp@yahoo.com",
                                msg="Subject: Monday Motivation\n\n{0}".format(quote))


send_quote()
