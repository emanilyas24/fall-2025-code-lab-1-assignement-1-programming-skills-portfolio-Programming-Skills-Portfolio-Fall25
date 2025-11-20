#Define a function that checks if a number is even or odd
def check_even_odd(num):
    if num % 2==0:
        return "The number is even."
    else:
        return"The number is odd."
    
#Define the main function that runs the program
def main():
    number=int(input("Enter a number:"))
    message= check_even_odd(number)
    print(message)

#This ensures main function runs only when script is executed directly.
if __name__ == "__main__":
    main()   

