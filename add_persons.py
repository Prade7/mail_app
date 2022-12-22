import csv
    
name=input("Enter your Name - ")
surname=input("Enter your surname - ")
email=input("Enter your email - ")
interest=input("Tell me your interest in single word like tesla,stocks,meditation - ")

total=[name,surname,email,interest]
with open("src\information.csv","a") as data:         # editing the information.csv  as append 
    csvwriter=csv.writer(data)                      

    csvwriter.writerow(total)                    # writting a row in csv   


