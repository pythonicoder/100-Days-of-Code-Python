#tip calculator


total = int(input('Welcome the tip calculator \nWhat was the total bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, 15 '))
people = int(input('How many peaople to split the bill '))


total_plus_tip_1 = int(tip) * int(people)
total_plus_tip_2 = int(total_plus_tip_1) + int(total)
per_person = int(total_plus_tip_2) / int(people)

print(f'Each person should pay:{per_person}')
