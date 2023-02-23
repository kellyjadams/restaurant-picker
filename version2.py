import random

# GLOBAL VARIABLES LIST
cuisine = ("American", "Asian", "Mexican")
expense = ("Cheap", "Not Bad", "Expensive")
price = {"Cheap":1 , "Not Bad": 2, "Expensive":3 }

# CLASS DEFINITION 
class Restaurant:
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
In_N_Out = Restaurant(cuisine ="American", expense = "Cheap", name="In N Out")
Kfc = Restaurant(cuisine ="American", expense = "Cheap", name="KFC")
Canes = Restaurant(cuisine ="American", expense = "Cheap", name="Raising Canes")

Chilis = Restaurant(cuisine ="American", expense="Not Bad", name="Chili's")
Black_Bear = Restaurant(cuisine ="American", expense="Not Bad", name="Black Bear Dinner")
Two_Chicks = Restaurant(cuisine ="American", expense="Not Bad", name="Two Chicks")

Bjs_Brew = Restaurant(cuisine ="American", expense="Expensive", name="BJ's Brewhouse")
Wild_River = Restaurant(cuisine ="American", expense="Expensive", name="Wild River Grille")

# Asian
Panda = Restaurant(cuisine ="Asian", expense="Cheap", name="Panda Express")
Poke_King = Restaurant(cuisine ="Asian", expense="Cheap", name="Poke King")
Pho_777 = Restaurant(cuisine ="Asian", expense="Cheap", name="Pho 777")

Golden_Flower = Restaurant(cuisine ="Asian", expense="Not Bad", name="Golden Flower")
Ramen4Real = Restaurant(cuisine ="Asian", expense="Not Bad", name="Ramen4Real")
Red_Bloom = Restaurant(cuisine ="Asian", expense="Not Bad", name="Red Bloom")

Ijji2 = Restaurant(cuisine ="Asian", expense="Expensive", name="Ijji 2")
Ijji4 = Restaurant(cuisine ="Asian", expense="Expensive", name="Ijji 4")

# Mexican
Taco_Bell = Restaurant(cuisine ="Mexican", expense="Cheap", name = "Taco Bell")
Los_Tres_Toritos = Restaurant(cuisine ="Mexican", expense="Cheap", name = "Los Tres Toritos")
Chipotle = Restaurant(cuisine ="Mexican", expense="Cheap", name="Chipotle")

Miguels = Restaurant(cuisine ="Mexican", expense="Not Bad", name="Miguel”s")
Tacos_El_Rey = Restaurant(cuisine ="Mexican", expense="Not Bad", name="Tacos El Rey")

# CREATE A LIST OF ALL OF THE RESTAURANTS
all_restaurants = [
    In_N_Out,
    Kfc,
    Canes,
    Chilis,
    Black_Bear,
    Two_Chicks,
    Bjs_Brew,
    Wild_River,
    Panda,
    Poke_King,
    Pho_777,
    Golden_Flower,
    Ramen4Real,
    Red_Bloom,
    Ijji2,
    Ijji4,
    Taco_Bell,
    Los_Tres_Toritos,
    Chipotle,
    Miguels,
    Tacos_El_Rey
]

# FUNCTIONS

# How much you want to spend
def spending_input():
    
    while True:
        try:
            money = int(input("How much do you want to spend? On a scale from 1-3. With 1 being 'Cheap', 2 being 'Not So Bad', and 3 being 'Expensive'. "))
            
            if money == 1:
                return "Cheap"
            elif money == 2:
                return "Not Bad"
            elif money == 3:
                return "Expensive"
            else:
               print("I'm sorry please pick a number 1-3. ")
        
        except ValueError:
            print ("Please input a number 1-3.")

# What type of cuisine you want
def cuisine_input():
    
    choice = "wrong"
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

print("Welcome to Restaurant Picker!\n")

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
