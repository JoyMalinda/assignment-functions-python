def temp_convert():
    unit = input("What is the unit of the tempreture you want to convert [C/F]?")
    temp = int(input("Enter the temperature value: "))

    if unit == "C":
       new_temp_F = (temp * 9/5) + 32
       print(f"{new_temp_F}F")
    elif unit == "F":
       new_temp_C = (temp - 32) * 5/9
       print(f"{new_temp_C}C")
    else:
       print("Error: Invalid input!")

temp_convert()