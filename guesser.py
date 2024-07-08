import random

def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def number_guesser():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    number_of_guesses = 0
    guess_history = []

    print("Welcome to the Number Guesser Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        guess = get_valid_guess()
        number_of_guesses += 1
        guess_history.append(guess)

        # Provide feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"\nCongratulations! You guessed the correct number {number_to_guess} in {number_of_guesses} tries.")
            print("Your guess history:", guess_history)

# Run the number guesser game
if __name__ == "__main__":
    number_guesser()

