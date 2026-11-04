from game import move_player

print("MYSTERY ISLAND: THE LOST LIGHTHOUSE")

player_name = input("Enter your name: ")
print(f"Welcome to Mystery Island, {player_name}!")

energy = 5
location = "Beach"
inventory = []

print(f"Energy: {energy}")
print(f"Location: {location}")
print(f"Inventory: {inventory}")

running = True

while running:
    print("1. Explore")
    print("2. Check inventory")
    print("3. Light the Lighthouse beacon")
    print("4. Quit game")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Available locations:", [
            "Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"
        ])

        destination = input("Enter location: ").strip()

        if (
            location == "Cave"
            and destination.casefold() == "old bridge"
            and "Rope" not in inventory
        ) or (
            location == "Old Bridge"
            and destination.casefold() == "lighthouse"
            and "Lantern" not in inventory
        ):
            print("You don't have the required item to continue!")
            message = "Movement blocked!"

        else:
            location, energy, message = move_player(
                location, destination, energy
            )

        print(message)
        print(f"Current location: {location}")
        print(f"Energy remaining: {energy}")

        if message == "Movement successful!":
            if location == "Cave":
                if "Rope" not in inventory:
                    inventory.append("Rope")
                    print("You found a Rope!")

            if location == "Jungle":
                if "Lantern" not in inventory:
                    inventory.append("Lantern")
                    print("You found a Lantern!")

    elif choice == "2":
        print(f"Your inventory: {inventory}")

    elif choice == "3":
        if location == "Lighthouse" and "Lantern" in inventory:
            print("The Lighthouse beacon is now shining!")
            print("Congratulations! You have been rescued!")
            running = False
        else:
            print("You need to be at the Lighthouse and have a Lantern!")

    elif choice == "4":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Try again.")

    if energy == 0 and running:
        print("You have run out of energy. Game Over!")
        running = False