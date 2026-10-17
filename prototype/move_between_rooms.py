"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

# TODO: Create the gameplay loop required by the milestone.
while True:
    print(f"\nYou are in the {current}.")

    command = input(Enter a direction (north, south, east, west) or "exit": ").lower()

    if command == "exit":
        print(Thanks for playing!")
        break
        
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
        print(f"You move {command}.")

    else:
        print(Invalid direction. Try again.")
