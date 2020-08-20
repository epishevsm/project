def division_user_number(num_1, num_2):
    division = num_1 / num_2
    return division
try:
    num_2 = 0
    print(division_user_number(int(input("Enter first number: ")), int(input("Enter second number: "))))
except ZeroDivisionError:
    print("Wrong number")