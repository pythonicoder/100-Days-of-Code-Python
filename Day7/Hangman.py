# Hangman game

import random

from Hangman_word import word_list

choosen_word = random.choice(word_list)
word_lenght = len(choosen_word)

end_of_game = False
lives = 6

from Hangman_art import logo
print(logo)

display = []

for _ in range(word_lenght):
    display += "_"
    
    
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_lenght):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter    
    if guess not in choosen_word:
        print(f"You guessed {guess}, that is not in the word. You lost a life.")
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print("You lost")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        print("You won!")
        
    from Hangman_art import stages
    print(stages[lives])
        
        