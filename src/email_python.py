import yagmail         # importing yagamil
from newsCollector import NewsFeed   # newsCollector is a file and from that we are importing a class "NewsFeed"

import pandas as pd
import datetime
import time

today_date=str(datetime.date.today())             
yesterday=str(datetime.date.today()-datetime.timedelta(days=1))
print(today_date)

df=pd.read_csv("src\information.csv")

while(True):
    if(datetime.datetime.now().minute==30 and datetime.datetime.now().hour==6):  # This checks the time 6 Am and will execute 
        for index,row in df.iterrows():
            Newsfeed=NewsFeed(interest=row['interest'],from_date=yesterday,to_date=today_date,language="en")
            
            email=yagmail.SMTP(user="dailynewsbypython@gmail.com",password="furtfmruejfhkukc")  
            email.send(to=row['email'],
            subject=f" Hey {row['surname']} take a look at this ",
            contents=f""" Hey {row['name']} Good Morning!, your interest is {Newsfeed.get()} 
            
            Thanks and Regards,
            Pradeep
            """)
            print(f"\n mail sent to {row['name']} ")

        time.sleep(60)                                                      # The loop will wait for 60 seconds



  



