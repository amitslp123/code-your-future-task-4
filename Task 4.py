import random

def game():
    print("Welcome to the Number Guessing Game!\n")
    print("Guess a number between 1 and 100.")
    num = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < num:
                print("Too low! Try again.")
            elif guess > num:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    game()
