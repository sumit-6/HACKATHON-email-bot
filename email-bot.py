import smtplib
import pandas as pd
import numpy as np
flag = 1
t = input("enter your email:")
while(flag == 1):
    a = np.random.randint(100000,999999)
    c="OTP is "+str(a)
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('algorithmunlock495@gmail.com','rasusuma')
    server.sendmail('algorithmunlock@gmail.com',t,c)
    b = int(input("enter your OTP that you have recieved on your E-mail ID:"))
    if (b == a):
        print("OTP verfied.\nYour attendance is marked!")
        flag = 0
    else:
        print("Wrong OTP please try again")
        print("We have resent the new OTP")
        
