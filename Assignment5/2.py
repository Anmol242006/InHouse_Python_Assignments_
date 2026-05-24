import random

choices = ["stone", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== STONE PAPER SCISSORS GAME =====")

for round in range(1, 6):

    print(f"\n----- Round {round} -----")

    user = input("Enter stone, paper or scissors: ").lower()

    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Round Draw")

    elif (
        (user == "stone" and computer == "scissors") or
        (user == "paper" and computer == "stone") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win This Round")
        user_score += 1

    else:
        print("Computer Wins This Round")
        computer_score += 1

print("\n===== FINAL RESULT =====")

print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("🎉 You Won The Game!")

elif computer_score > user_score:
    print("💻 Computer Won The Game!")

else:
    print("🤝 Game Draw")