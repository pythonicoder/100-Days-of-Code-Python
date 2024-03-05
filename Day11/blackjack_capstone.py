import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose, opponent has blackjack."
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Opponent went over, you win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    
    print(logo)
    
    user_card = [] 
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:    
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"  Your cards: {user_card}, current score: {user_score}")
        print(f"  Computer's first card: {computer_card[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        
    print(f"  Your final hand is: {user_card}, and final score is: {user_score}")
    print(f"  Computer's final hand is: {computer_card}, and final score is: {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()== 'y':
    play_game()