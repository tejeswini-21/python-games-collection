import random


OPTIONS = ("rock", "paper", "scissors")

def determine_winner(player, computer):
    """Evaluate game logic and return the round winner."""
    if player == computer:
        return "tie"

    if (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"

def main():
    player_score = 0
    computer_score = 0
    running = True

    print("=============================================")
    print("            ROCK, PAPER, SCISSORS            ")
    print("=============================================")

    while running:
        print("\nChoose one of the following:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")


        while True:
            user_input = input("\nEnter your choice (name or number): ").strip().lower()

            if user_input in ("1", "rock"):
                player = "rock"
                break
            elif user_input in ("2", "paper"):
                player = "paper"
                break
            elif user_input in ("3", "scissors"):
                player = "scissors"
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, rock, paper, or scissors.")

        computer = random.choice(OPTIONS)

        print("\n" + "---------------------------------------------")
        print(f"Player   : {player.capitalize()}")
        print(f"Computer : {computer.capitalize()}")

        result = determine_winner(player, computer)

        if result == "tie":
            print("Result   : It's a tie.")
        elif result == "player":
            print("Result   : You win this round.")
            player_score += 1
        else:
            print("Result   : Computer wins this round.")
            computer_score += 1

        print("---------------------------------------------")
        print(f"Score    : Player {player_score} | Computer {computer_score}")

        while True:
            play_again = input("\nPlay again? (y/n): ").strip().lower()

            if play_again in ("y", "yes"):
                break
            elif play_again in ("n", "no"):
                running = False
                break
            else:
                print("Invalid choice.Please enter 'y' or 'n'.")


    print("\n" + "=============================================")
    print("                 FINAL SCORE                 ")
    print("=============================================")
    print(f"Player   : {player_score}")
    print(f"Computer : {computer_score}")
    print("---------------------------------------------")

    if player_score > computer_score:
        print("Overall Winner : Player")
    elif computer_score > player_score:
        print("Overall Winner : Computer")
    else:
        print("Overall Result : Draw")

    print("=============================================")
    print("Thank you for playing.")


if __name__ == "__main__":
    main()

