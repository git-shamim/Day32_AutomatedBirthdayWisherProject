
# for multiple birthdays on same date

import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "study.practice.smtp@gmail.com"
MY_PASSWORD = "@Zoya051217"

now = dt.datetime.now()
today = (now.month, now.day)

df = pandas.read_csv("birthdays.csv")
birthdays_dict = df.to_dict(orient="records")

for birthday in birthdays_dict:
    month_day_birth = (birthday['month'], birthday['day'])
    birthday_name = birthday['name']
    birthday_email = birthday['email']
    birthday_year = birthday['year']
    birthday_date = (birthday_year, birthday['month'], birthday['day'])
    random_letter = random.randint(1, 3)
    letter_file = "letter_templates/letter_{}.txt".format(random_letter)
    if today == month_day_birth:
        with open(letter_file) as file:
            content = file.read()
            content = content.replace("[NAME]", birthday_name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_email,
                                msg="Subject: Happy Birthday\n\n{}".format(content))
