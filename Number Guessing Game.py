import random


def main():
    while True:
        print("\n============== NUMBER GUESSING GAME ==============")
        print("Select Difficulty")
        print("1. Easy   (1 - 50)")
        print("2. Medium (1 - 100)")
        print("3. Hard   (1 - 500)")

        difficulty = input("Enter your choice (1/2/3): ")

        if difficulty == "1":
            lowest_number = 1
            highest_number = 50
        elif difficulty == "2":
            lowest_number = 1
            highest_number = 100
        elif difficulty == "3":
            lowest_number = 1
            highest_number = 500
        else:
            print("Invalid choice. Please try again.")
            continue

        secret_number = random.randint(lowest_number, highest_number)
        attempts = 0

        print(f"\nGuess a number between {lowest_number} and {highest_number}.")

        while True:
            guess = input("Enter your guess: ")

            if not guess.isdigit():
                print("Invalid input. Please enter a whole number.")
                continue

            guess = int(guess)

            # FIXED: Corrected the unexpected extra indentation here
            if guess < lowest_number or guess > highest_number:
                print(f"Please enter a number between {lowest_number} and {highest_number}.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print("\n============= GAME OVER =============")
                print("Correct!")
                print(f"The secret number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                print("=====================================")
                break

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()

