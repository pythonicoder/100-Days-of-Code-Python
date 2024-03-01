
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False

def find_highest_bider(biding_record):
    highest_bid = 0 
    winner = ""
    for bider in biding_record:
        bid_amount = biding_record[bider]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bider
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bider(bids)
    elif should_continue == 'yes':
        continue