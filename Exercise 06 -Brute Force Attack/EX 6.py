#Define the correct password
correct_password="comp1234"

#Set the number of allowed attempts
attempts=5

#Use a while loop to keep asking for the password
while attempts>0:
    entered_password=input("Enter password:")

#Check if the entered password is correct
    if entered_password==correct_password:
        print("Access granted")
        attempts=0

    else:
       attempts -=1

#Provide feedback on remaining attempts 
    if attempts>0:
        print(f"Incorrect. You have {attempts} attempts left.")

#Alert when maximum attempts are reached
    if attempts==0:
         print(" Access denied , Authorities have been alerted")

