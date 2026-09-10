# User gives a year we need to tell if its a leap year or not

year = int(input("Whats the year you want to check \n"))

if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 == 0:
            print(True)
        print(False)
    print(True)
else:
    print(False)
