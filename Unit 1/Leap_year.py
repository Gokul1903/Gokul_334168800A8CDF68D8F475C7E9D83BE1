while(1):
    year=int(input("enter a year: ".title()))
    if(year % 4==0 and year % 100!=0)or(year % 400 ==0):
        print(f"{year} is a leap year.\n".title())
    else:
        print(f"{year} is not a leap year.\n".title())

