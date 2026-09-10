#Find the sum of Fibonacci numbers.
first_number = 0
second_number = 1
total_sum = 0
for i in range(10):
    print(first_number)
    total_sum += first_number

    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
print("Sum =", total_sum)