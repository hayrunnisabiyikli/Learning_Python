import random

# Dictionary of U.S. states and their capitals
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "St. Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# Convert the dictionary to a list of (state, capital) tuples
states = list(state_capitals.keys())

# Initialize counters for correct and incorrect responses
correct = 0
incorrect = 0

# Quiz the user
while True:
    # Check if all states have been asked
    if len(states) == 0:
        print("All states have been covered.")
        break

    # Select a random state from the list
    state = random.choice(states)

    # Get the capital of the selected state
    capital = state_capitals[state]

    # Ask the user to enter the capital of the state
    answer = input(f"What is the capital of {state}? ")

    # Check if the answer is correct
    if answer.lower() == capital.lower():
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect. The capital of {state}")
        incorrect += 1

        # Remove the state from the list
    states.remove(state)

    # Check if 5 questions have been asked
    if (correct + incorrect) % 5 == 0:
        finish_quiz = input("Do you want to finish the quiz? (yes/no) ")
        if finish_quiz.lower() == "yes":
            break

# Print the final results
print(f"\nCorrect responses: {correct}")
print(f"Incorrect responses: {incorrect}")
