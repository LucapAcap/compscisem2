import random
resturants = ["Seasoning Alley","Jersey Mike's", "The Habit"]
SeasongAlley = ["Kebab","shawarma","dolma"]
JerseyMikes = ["sandwich", "Mikes way", "chip"]
TheHabit = ["double bbq bacon charburger", "milkshake", "onion rings"]

resturants = resturants[random.randrange(0,3)]
print("The resturant is " + resturants)

if resturants == "Seasoning Alley":
    item = SeasongAlley[random.randrange(0,3)]
    print("The menu item is " + item)
    
elif resturants == "Jersey Mikes":
    item = JerseyMikes[random.randrange(0,3)]
    print("The menu item is " + item)
    
elif resturants == "The Habit":
    item = TheHabit[random.randint(0,3)]
    print("The menu item is "+ item)