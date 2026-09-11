
# if year % 4 == 0 :
#     print(f"{year} is a leap year")
# else :
#     print(f"{year} is not a leap year")

#Now this code can hold all the edge cases.

# Bro see the code 100 is divisible by 4 so it will still give leap year
year = int(input("Whats the year you want to enter: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")

# now if you think there is something better lets talk dont commit pls
    
