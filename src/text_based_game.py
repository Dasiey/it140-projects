"""Project Two starter for the student's text-based adventure game."""

Daija Walls


def show_instructions():
    """Display the game objective and available commands."""
    print("Capture the Coach Game!")
    print("An alien captured your head basketball coach.")
    print("Commands:")
    print("go North, go South, go East, go West")
    print("get {item name})
    print("exit")
    print("----------------------------")

def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("--------------------")
    print("You are in the" + current_room)
    print("Inventory: " + str(inventory))

    #Check if there is an item in the current room
    if "item" in rooms[current_room]:
        print(You see a " + rooms[current_room]["item"])
        print("-------------------------")
    


def main():
    """Run the main gameplay loop."""
    #Dictionary connecting rooms, directions, and items
    rooms ={
        "Student Center": {"South": "Dormitory", "North": "Library"< "East": "Gymnasium", "West": "Cafeteria"},
        "Dormitory": {"North": "Student Center", "East",: "Rec Center", "item": "Laser-Whistle"},
        "Rec Center": {"West": "Dormitory", "item": "Plasma-Ball"},
        "Cafeteria": {"East": "Student Center", "item": "Acid-Gatorade"},
        "Gynmasium": {"West": "Student Center", "North": "Training Room", "item": "Electrified-Net"},
        "Training Room": {"South": "Gymnasium", "item": "Stun-Jersey"}
        "Library": {"South": "Student Center", "East": "Arena", "item": "laser-Sneakers"}
        "Arena": {"item": "Alien Commander"}
}

# Set initial state
current_room = "Student Center"
inventory = []

# Display instructions at start
show_instructions()

# Main gameplay loop
while True:

    # Game over condition if player enters Arena (villain room)
    if current_room == "Arena":
        print("You walked into the Arena without all 6 items!")
        print("The Alien Commander defeatedyour team.")
        print("GAME OVER! Coach is still captured.")
        break

    # Display current room and inventory
    show_status(current_room, inventory, rooms)

    # Get command from user
    user_input = input("Enter your move: ")

    # Check for exit command
    if user_input.lower() -- "exit":
        print("Thanks for playing!")
        break

    # Handle movement commands (e.g, "go North")
    if len(parts) >= 2 and parts[0].lower() == "go":
        direction = parts[1].capitaliza()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You cannot go that wat!")

    # Handle item pickup commands (e.g., "get Laser-Whistle")
    elif len(parts) >= 2 and parts[0].lower() == "get":
        # Rejoin words after "get" for multi-word item names
        item_requested = " ".join(parts[1:]).title()

        if "item" in rooms[current_room] and rooms[current_room]["item"].title() == item_requested:
            collected_item = rooms[current_room]["item"]
            inventory.append(collected_item)
            del rooms[current_room]["item"]
            print("You got the " + collected_item + "!")

        # Check in condition
        if len(inventory) == 6:
            print("You collected all 6 items and defeated the Alien Commander!")
            print("YOU WIN! You rescued Coach!")
            break
    else:
        print("Can;t get " + item_requested + "!")

    else:
        print("Invalid command! Use "go[direction]" or "get [item]".")

    


if __name__ == "__main__":
    main()
