#Ask the user a question and store their answer 
answer=input("What is the capital of france")

#Check if answers match exactly
if answer=="Paris":
    print("Correct!")
else:
    print("Wrong!")

#Check if answers match regardless of the capitilization
if answer.lower()=="paris!":
    print("Correct!")
else:
    print("Wrong!")

#Create a dictionary of country-capital pairs
questions={
    "France":"Paris",
    "Germany":"Berlin",
     "Italy":"Rome",
     "Spain":"Madrid",
      "Portugal":"Lisbon",
      "Netherlands":"Amsterdam",
      "Sweden":"Stockholm",
       "Norway":"Oslo",
        "Greece":"Athens",
        "Poland":"Warsaw"
}

#Loop through each question and check the user's answer
for country, capital in questions.items():
 user_answer=input(f"What is the capital of {country}?").lower()
if user_answer== capital.lower():
    print("Correct!")
else:
    print(f"Wrong! the correct answer is {capital}.")
    
