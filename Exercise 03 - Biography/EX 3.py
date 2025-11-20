#Step 1: Create a dictionary to store name , hometown and age
information={
    'Name':'Eman',
     'Hometown': 'New york',
     'Age': '20'}

#Step 2: Prompt the user to input their name , hometown and age.
Name=input("Enter your Name")
Hometown=input("Enter your hometown")
Age=input("Enter your age")

#Convert age input to integer
Age=int(Age)

#Print values from the dictionary.
print(information["Name"],information["Hometown"],information["Age"])

