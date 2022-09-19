import random
import time
from time import sleep

transports = ['a plane', 'a train', 'a bus', 'your vehicle', 'a taxi', 'an Uber']
destinations = ['Des Moines', 'Chicago', 'Minneapolis', 'St. Paul', 'Omaha', 'Kansas City', 'Milwaukee', 'Madison', 'LaCrosse']
restaurants = ['Applebees', 'Red Lobster', "Wendy's", "Raising Cane's", 'Olive Garden', 'a buffet', 'a taco truck', 'a BBQ joint', 'a literal live fish']
entertainment_options = ['the zoo', 'the clubs', 'a park', 'a museum', 'a concert', 'a game', 'a theme park', 'the sights']

def update_list(article, from_list):
    from_list.remove(article)

def restore_original_list(main_list, refill_list):
    if len(main_list) == 0:
        main_list = refill_list.copy()
        print('We ran out of options, bud. Let\'s start over, shall we?')
    return main_list

def item_selection(list, prompt):
    working_list = list.copy()
    selection = random.choice(working_list)
    approval = input(f"How about {prompt} {selection}. Sound good to you? y or n: ")
    while approval != 'y':
        working_list.remove(selection)
        working_list = restore_original_list(working_list, list)
        selection = random.choice(working_list)
        sleep(.25)
        print('Hmmm...')
        sleep(1)
        approval = input(f"How about {selection}? y or n: ")
    print(f'It\'s decided then, you\'ll be {prompt} {selection}!')
    sleep(.1)
    return selection

def full_generator():
    finalized_choices = []
    approval = ''
    while approval != 'y':
        finalized_choices.clear()
        print('Welcome! Let\'s see what we can plan for you...')
        sleep(.5)
        finalized_choices.append(item_selection(transports, 'taking'))
        finalized_choices.append(item_selection(destinations, 'visiting'))
        finalized_choices.append(item_selection(restaurants, 'eating at'))
        finalized_choices.append(item_selection(entertainment_options, 'enjoying'))
        approval = input(f'Okay, great! So you\'d like to take {finalized_choices[0]} to {finalized_choices[1]}, and while you\'re there you\'ll be eating at {finalized_choices[2]}, and enjoying {finalized_choices[3]}. Ready to lock in your selections? y or n: ')
        print(f"Wonderful! To recap, you're taking {finalized_choices[0]} to {finalized_choices[1]}, {finalized_choices[2]} and {finalized_choices[3]} when you get there.")
    sleep(1)
    print()
    print("Thank you so much for using our generator! Enjoy your day trip!")

full_generator()