def main():
    # Ask for the user's name
    name = input("What is your name? ")

    # Ask for the user's age
    age = int(input("How old are you? "))

    # Ask for the user's favorite color
    color = input("What is your favorite color? ")

    # Print a personalized greeting message
    print(f"\nHello {name}!")
    print(f"You're {age} years old and your favorite color is {color}.")
    print("Thanks for sharing these details with me!")

# Call the main function to run the program
if __name__ == "__main__":
    main()
