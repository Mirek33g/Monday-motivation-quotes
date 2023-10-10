import datetime as dt
import smtplib
import random


my_email ="first.steps.coding@gmail.com"
password = "rtai ojdb ienr waec"


now = dt.datetime.now()
today_is = now.weekday()

if today_is == 1:
    rand_quote = random.choice(list(open("quotes.txt")))

    connection= smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user= my_email,password= password)
    connection.sendmail(from_addr= my_email, to_addrs= my_email, msg=f"Subject: HELLO\n\n{rand_quote}")
    connection.close()
    






