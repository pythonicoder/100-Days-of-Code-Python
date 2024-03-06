import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def checking_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The number was {answer}.")

# The function of set diffuculity.
def set_diffuculity():
    level = input("Choose a diffuculuty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing the number between 1 and 100.
    print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_diffuculity()
    # Let the user guess a number.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        # Track the numer of turns reduce by 1 if they get it wrong. 
        turns = checking_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The number was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")

while input("Do you want to play game? Type 'y' or 'n': ").lower()== 'y':
    game()