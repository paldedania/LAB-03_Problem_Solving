#Check whether a number is an Armstrong number.
#An Armstrong number is a number where the sum of each digit raised to the power of the number of digits is equal to the original number.
num = int(input("Enter number:"))
digit_count = len(str(num))
sum_power=0
for digit in str(num):
    sum_power+= int(digit) ** digit_count
if sum_power==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")