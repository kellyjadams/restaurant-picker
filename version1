import random

# GLOBAL VARIABLES LIST
cuisine = ('American', 'Asian', 'Mexican')
expense = ('Cheap', 'Not Bad', 'Expensive')
price = {'Cheap':1 , 'Not Bad': 2, 'Expensive':3 }

# CLASS DEFINITION 
class restaurant:
    def __init__(self, cuisine, expense, name):
        self.cuisine = cuisine
        self.expense = expense
        self.price = price[expense]
        self.name = name
    
    # The string representation
    def __str__(self):
        return self.name 
    
    # Returns the string representation of an ojbect 
    def __repr__(self):
        return str(self)
    
# LIST OF RESTAURANTS (Seperated by Type)

# American 
inNOut = restaurant(cuisine ='American', expense = 'Cheap', name='In N Out')
kfc = restaurant(cuisine ='American', expense='Cheap', name='KFC')
canes = restaurant(cuisine ='American', expense='Cheap', name='Raising Canes')

chillis = restaurant(cuisine ='American', expense='Not Bad', name="Chilli's")
blackbear = restaurant(cuisine ='American', expense='Not Bad', name="Black Bear Dinner")
twoChicks = restaurant(cuisine ='American', expense='Not Bad', name="Two Chicks")

bjsBrew = restaurant(cuisine ='American', expense='Expensive', name="BJ's Brewhouse")
wildRiver = restaurant(cuisine ='American', expense='Expensive', name="Wild River Grille")

# Asian
panda = restaurant(cuisine ='Asian', expense='Cheap', name='Panda Express')
pokeking = restaurant(cuisine ='Asian', expense='Cheap', name='Poke King')
pho777 = restaurant(cuisine ='Asian', expense='Cheap', name='Pho 777')

goldenFlower = restaurant(cuisine ='Asian', expense='Not Bad', name='Golden Flower')
ramen4real = restaurant(cuisine ='Asian', expense='Not Bad', name='Ramen4Real')
redBloom = restaurant(cuisine ='Asian', expense='Not Bad', name='Red Bloom')

ijji2 = restaurant(cuisine ='Asian', expense='Expensive', name='Ijji 2')
ijji4 = restaurant(cuisine ='Asian', expense='Expensive', name='Ijji 4')

# Mexican
tacoBell = restaurant(cuisine ='Mexican', expense='Cheap', name = 'Taco Bell')
lostTresToritos = restaurant(cuisine ='Mexican', expense='Cheap', name = 'Lost Tres Toritos')
chipotle = restaurant(cuisine ='Mexican', expense='Cheap', name='Chipotle')

miguels = restaurant(cuisine ='Mexican', expense='Not Bad', name="Miguel's")
tacosElRey = restaurant(cuisine ='Mexican', expense='Not Bad', name="Tacos El Rey")

# CREATE A LIST OF ALL OF THE RESTAURANTS
all_restaurants = [
    inNOut,
    kfc,
    canes,
    chillis,
    blackbear,
    twoChicks,
    bjsBrew,
    wildRiver,
    panda,
    pokeking,
    pho777,
    goldenFlower,
    ramen4real,
    redBloom,
    ijji2,
    ijji4,
    tacoBell,
    lostTresToritos,
    chipotle,
    miguels,
    tacosElRey
]

# FUNCTIONS

# How much you want to spend
def spending_input():
    
    while True:
        try:
            money = int(input('How much do you want to spend? On a scale from 1-3. With 1 being cheap, 2 being not so bad, and 3 being expensive. '))
            
            if money == 1:
                return 'Cheap'
            elif money == 2:
                return 'Not Bad'
            elif money == 3:
                return 'Expensive'
            else:
                return "I'm sorry please pick a number 1-3. "
        
        except ValueError:
            print ("Please input a number 1-3.")

# What type of cuisine you want
def cuisine_input():
    
    choice = 'wrong'
    print("\nThese are the types of cuisines you have to choose from: " + str(cuisine))    
    
    while choice not in cuisine:
        
        choice = input("Please choose the cuisine you want. ")
        
        if choice not in cuisine:
            print("Sorry that cuisine is not listed. Please choose another one. ")
            
        else:
            return choice
        
# List possible choices based on user input
def decision(money, food):
    a = []
    # choose correct list
    for x in all_restaurants:
        if x.cuisine == food and x.expense == money:
            a.append(x)
    return a

# PROGRAM LOGIC

print('Welcome to Restaurant Picker!\n')

def restaurant_picker():
    
    # Ask for how much the user wants to spend
    cash = spending_input()
    
    # Ask for what type of cuisine the user wants
    restaurant = cuisine_input()
    
    #Create a list of choices based on the user input of cash and cuisine type 
    final_choice = decision(cash, restaurant)
    
    # Choose randomly from the list above 
    final_decision = random.choice(final_choice)
    
    # Print the final choice
    print("\nThe restaurant for you is: " + str(final_decision))

restaurant_picker()
