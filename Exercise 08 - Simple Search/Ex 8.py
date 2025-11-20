#Intialize the list of names.
names=["Jake","Zac","Ian","Ron","Sam","Dave"]
search_term="Sam"

#Ask the user to enter a name to search for
search_name=input("Enter the name you want to search for:")

#Check if the user-provided name is in the list.
if search_term in names:
    print(search_term,"was found in the list!")
else:
    print(search_term, "was NOT found in the list!")
