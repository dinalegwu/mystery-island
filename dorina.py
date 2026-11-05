"""MYSTERY ISLAND"""
name = input("Enter user name: ")
energy = 5
location = "Beach"
inventory = []

print(f"welcome to mystery island, {name}!")

location = ("Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse")
print(f"location, {location}!")

choice = 0
print("1.  Explore")
print("2.  Check inventory")
print("3.  Quit game")

choice = input("\n what would you like to do: ")

if choice == "1":
    print("You are about Explore")
elif choice == "2":
    print("Check inventory")
elif choice == "3":
    print("Goodbye")

