import random

transports = ['a plane', 'a train', 'a bus', 'your vehicle', 'a taxi', 'an Uber']
destinations = ['Des Moines', 'Chicago', 'Minneapolis', 'St. Paul', 'Omaha', 'Kansas City', 'Milwaukee', 'Madison', 'LaCrosse']
restaurants = ['Applebees', 'Red Lobster', "Wendy's", "Raising Cane's", 'Olive Garden']
entertainment_options = ['the zoo', 'the clubs', 'a park', 'a museum', 'a concert', 'a game', 'a theme park', 'the sights']

def randomizer():
    selections = [random.choice(transports), random.choice(destinations), random.choice(restaurants), random.choice(entertainment_options)]
    return selections

def generation():
    approval = " "
    while approval != 'y':
        selections = randomizer()
        approval = input(f"We think you should take {selections[0]} to {selections[1]}. While you're there, you should grab {selections[2]} and enjoy {selections[3]}. Sound good? y or n: ")
    print(f"Great choice! You're going to love taking {selections[0]} to {selections[1]}, and we hope you'll enjoy {selections[2]} and {selections[3]}!")

generation()