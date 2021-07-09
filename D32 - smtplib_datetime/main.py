import smtplib
import datetime as dt
import random

MY_EMAIL = "bjornbergchad@gmail.com"
MY_PASSWORD = "5hoKV2kwo6cw"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    # for below to work:
    # Google settings; phone sign-in=False, 2-step=False, less secure apps=True
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # a way of securing our connection to our email server
        # encrypts email until recipient receives email
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="bjornbergchad@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}.",
        )
