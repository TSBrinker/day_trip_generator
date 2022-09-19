import random
import time
from time import sleep

destinations = ['Des Moines', 'Chicago', 'Minneapolis', 'St. Paul', 'Omaha', 'Kansas City', 'Milwaukee', 'Madison', 'LaCrosse']
transports = ['a plane', 'a train', 'a bus', 'your vehicle', 'a taxi', 'an Uber']
restaurants = ['Applebees', 'Red Lobster', "Wendy's", "Raising Cane's", 'Olive Garden']
entertainment_options = ['the zoo', 'the clubs', 'a park', 'a museum', 'a concert', 'a game', 'a theme park', 'the sights']

# print('Hello, User!')
# user = input('What is your name? ')

def randomizer():
    selections = [random.choice(transports), random.choice(destinations), random.choice(restaurants), random.choice(entertainment_options)]
    return selections

# def transport_select():
#     transportation = random.choice(transports)
#     return transportation

# this was barely conceived when you popped in for a chat - probably still rough. Please ignore.
# def transport_approve():
    # approval = input(f"{user}, if you're going on a trip, we think you should take {transportation}. Sound good to you? y or n: ")
    # while approval == 'n':
    #     transports.remove(transportation)
    #     approval = input(f"Okay, {user}, let's try again. How about {transportation}? y or n: ")

# def destination_select():
#     destination = random.choice(destinations)
#     return destination

# def food_select():
#     food = random.choice(restaurants)
#     return food

# def fun_select():
#     fun = random.choice(entertainment_options)
#     return fun

# def generation():
#     approval = " "
#     while approval != 'y':
#         transport = transport_select()
#         destination = destination_select()
#         food = food_select()
#         fun = fun_select()
#         approval = input(f"We think you should take {transport} to {destination}. While you're there, you should grab {food} and enjoy {fun}. Sound good? y or n: ")
#     else: 
#         print(f"Great choice! You're going to love taking {transport} to {destination}, and we hope you'll enjoy {food} and {fun}!")

def generation():
    approval = " "
    while approval != 'y':
        selections = randomizer()
        approval = input(f"We think you should take {selections[0]} to {selections[1]}. While you're there, you should grab {selections[2]} and enjoy {selections[3]}. Sound good? y or n: ")
    else: 
        print(f"Great choice! You're going to love taking {selections[0]} to {selections[1]}, and we hope you'll enjoy {selections[2]} and {selections[3]}!")


generation()

# def confirmation():
#     approval = ""
#     while approval == "" or approval == "n":
#         generation()
#         print(f"We think you should take {transport} to {destination}. While you're there, you should grab {food} and enjoy {fun}. Sound good? y or n: ")


# def confirmation():
#     approval = ""
#     while approval == "" or approval == "n":
#         generation()
#     else:
#         print('Great! To confirm: You will take ')