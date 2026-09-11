# User gives a year we need to tell if its a leap year or not

# year = int(input("Whats the year you want to check \n"))

# if year % 4 ==0:
#     if year % 100 ==0:
#         if year % 400 == 0:
#             print(True)
#         print(False)
#     print(True)
# else:
#     print(False)

    #i think this code is not right for all case
    #if we give intput 2000
    #the output comes out 
    #True 
    #False
    #True
    # what's the meaning of this type of output ?



# the right method is simple 
# if year%4==0 than print true , else false 

# year = int(input("Whats the year you want to check \n"))

# if year%4==0:
#     print(f"{year} is a leap year ")

# True but the conditions are not true here as 100 is not a leap year but in this code it will give leap year so correct ans will be 
year = int(input("Whats the year you want to check: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
