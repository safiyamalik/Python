month=input("enter month name:").lower()
y=int(input("enter the year:"))
if month in ["january", "march", "may", "july","august","october","december"]:
       print("31 days")
elif month in ["april", "june", "september","november"]:
    print("30 days")
elif month=="february":
    if (y%4==0 and y %100!=0) or (y%400==0):
        print("29 days")
    else:
        print("28 days")
else:
    print("invalid month:")
