import random

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice=="paper"): 
        return "User"
    else:
        return "Computer"



def play_game():
    computer_score = 0
    user_score = 0
    while True:
        user_choice = str(input("what's your choice Rock,Paper or Scissors? ")).strip().lower()
        if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
            print(f"Scores: Computer:{computer_score} : You:{user_score}")
            computer_choice = random.choice(["rock","paper","scissors"])
            if determine_winner(user_choice,computer_choice) == "Tie":
                print("Tie")
                interest = input("Still wanna play? (yes/no) ")
                if interest == "no":
                    print("Thanks for playiing")
                    break
            elif determine_winner(user_choice,computer_choice) == "User":
                print("You won!, you have 1 additional point")
                user_score += 1
                print(f"Scores: Computer:{computer_score} : You:{user_score}")
                interest = input("Still wanna play? (yes/no) ").strip()
                if interest == "no":
                    print("Thanks for playiing")
                    break
            elif determine_winner(user_choice,computer_choice) == "Computer":
                print("You lost!, I have 1 additional point")
                computer_score += 1
                print(f"Scores: Computer:{computer_score} : You:{user_score}")
                interest = input("Still wanna play? (yes/no) ").strip()
                if interest == "no":
                    print("Thanks for playing")
                    break

if __name__ == "__main__":
    play_game()