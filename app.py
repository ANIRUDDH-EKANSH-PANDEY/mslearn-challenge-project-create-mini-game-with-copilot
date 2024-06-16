import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ")
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nScores: You - {user_score}, Computer - {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print(f"\nFinal Scores: You - {user_score}, Computer - {computer_score}")

play_game()