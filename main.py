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
sleep(3)

def generation():
    transport = transport_select()
    destination = destination_select()
    food = food_select()
    fun = fun_select()
    print(f"Alright, {user}! We think you should take {transport} to {destination}. While you're there, wanna grab {food} and hit {fun}?")

generation()