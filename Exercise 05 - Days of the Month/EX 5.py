#Create a dictionary mapping months to number of days
months={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31}

#Ask the user to input a month number
month_number=int(input("Enter a month number(1-12):"))

#Check if the input is valid and handle February seperately
if month_number in months: 
    if month_number==2:
        leap=input("Is it a leap year (yes/no):")
        if leap=="yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days")
    else: 
        print(f"The month has {months[month_number]} days.")
else: 
    print("Invalid month number! Please enter a number between 1 and 12")

    