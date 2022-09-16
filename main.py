import random
import time
from time import sleep

destinations = ['Des Moines', 'Chicago', 'Minneapolis', 'St. Paul', 'Omaha', 'Kansas City']
transports = ['a plane', 'a train', 'a bus', 'your vehicle']
# automobiles = ['your own vehicle', 'an uber', 'a bus']
restaurants = ['Applebees', 'Red Lobster', "Wendy's", "Raising Cane's", 'Olive Garden']
entertainment_options = ['the zoo', 'the clubs', 'a park', 'a museum', 'a concert']

def name_capture():
    print('Hello, User!')
    user_name = input('What is your name? ')
    return user_name

def transport_select():
    transportation = random.choice(transports)
    return transportation

# this was barely conceived when you popped in for a chat - probably still rough. Please ignore.
# def transport_approve():
    # approval = input(f"{user}, if you're going on a trip, we think you should take {transportation}. Sound good to you? y or n: ")
    # while approval == 'n':
    #     transports.remove(transportation)
    #     approval = input(f"Okay, {user}, let's try again. How about {transportation}? y or n: ")

def destination_select():
    destination = random.choice(destinations)
    return destination

def food_select():
    food = random.choice(restaurants)
    return food

def fun_select():
    fun = random.choice(entertainment_options)
    return fun

user = name_capture()


def generation():
    transport = transport_select()
    destination = destination_select()
    food = food_select()
    fun = fun_select()

def confirmation():
    approval = ""
    while approval == "" or approval == "n":
        generation()
        print(f"We think you should take {transport} to {destination}. While you're there, you should grab {food} and enjoy {fun}. Sound good? y or n: ")


generation()
confirmation()

# def confirmation():
#     approval = ""
#     while approval == "" or approval == "n":
#         generation()
#     else:
#         print('Great! To confirm: You will take ')