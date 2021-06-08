
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "study.practice.smtp@gmail.com"
MY_PASSWORD = "@Zoya051217"

now = dt.datetime.now()
today = (now.month, now.day)

df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}

if today in birthdays_dict:
    birthday_today = birthdays_dict[today]
    selected_letter = "letter_templates/letter_{0}.txt".format(random.randint(1, 3))

    with open(selected_letter) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_today["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_today["email"],
                            msg="Subject: Happy Birthday\n\n{}".format(contents))
