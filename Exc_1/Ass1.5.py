"""You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a local restaurant. You aren’t sure if any of them have
dietary restrictions, but your restaurant choices are as follows:"""

# Hayrunnisa Bıyıklı 21091010143

# Define the restaurant menu and their dietary restrictions
restaurant_menu = {
    "Joe's Gourmet Burgers": {"Vegetarian": False, "Vegan": False, "Gluten-Free": False},
    "Main Street Pizza Company": {"Vegetarian": True, "Vegan": False, "Gluten-Free": True},
    "Corner Café": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True},
    "Mama's Fine Italian": {"Vegetarian": True, "Vegan": False, "Gluten-Free": False},
    "The Chef's Kitchen": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True}
}
# Get user input for dietary restrictions
vegetarian = input("Is anyone in your party a vegetarian? (yes/no): ").lower() == "yes"
vegan = input("Is anyone in your party a vegan? (yes/no): ").lower() == "yes"
gluten_free = input("Is anyone in your party gluten-free? (yes/no): ").lower() == "yes"

# Filter restaurants based on dietary restrictions
suitable_restaurants = []
for restaurant, restrictions in restaurant_menu.items():
    if (not vegetarian or restrictions["Vegetarian"]) and (not vegan or restrictions["Vegan"]) and (not gluten_free or restrictions["Gluten-Free"]):
        suitable_restaurants.append(restaurant)

# Display suitable restaurants
if suitable_restaurants:
    print("Here are your restaurant choices:")
    for restaurant in suitable_restaurants:
        print("- " + restaurant)
else:
    print("No suitable restaurants found for your dietary restrictions.")
