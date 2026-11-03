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
    print("3. Quit game")

    choice = input("Choose an option: ")

    if choice == "1":
        locations = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]

        print("Available locations:", locations)

        location = input("Enter location: ").strip()

        found = False

        for one in locations:
            if location.casefold() == one.casefold():
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

        if energy == 0:
        print("You have run out of energy. Game Over!")
        running = False
        print(f"Energy remaining: {energy}")