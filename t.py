"MYSTERY ISLAND: THE LOST LIGHTHOUSE"

player_name = input("Enter your name: ")
print(f"welcome to Mystery Island, {player_name}!")

energy = 5
location = "Beach" 
inventory = []
print(f"Energy, {energy}")
print(f"Location, {location}")
print(f"inventory, {inventory}")

running = True
while running:
    print("1. Explore")
    print("2. Check inventory")
    print("3. Quit game")

    choice = input("Choose an option: ")

    while running:

    # choice = input("Choose an option: ")

    if choice == "1":

        locations = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]

        location = input("Enter location: ").strip()

        found = False

        for one in locations:
            if location.lower() == one.lower():
                found = True
                break

        if found:
            location = one
            print(f"You are now at {location}!")
    else:
            print("Invalid location. Try again.")

    elif choice == "2":
        print(f"Your inventory: {inventory}")

    elif choice == "3":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Try again.")
        # location = one
        # print(f"You are now at {location}!")

    #  inventory.append("Lantern")

    # if location == "Cave":
    #     inventory.append("Rope")
    #     print("You found a rope!")

    # if "Rope" not in inventory:
    #     inventory.append("Rope")
    #     print("You found a rope!")