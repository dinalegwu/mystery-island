"""Command-line interface for Mystery Island: The Lost Lighthouse."""

from game import (
    LOCATIONS,
    get_status,
    light_beacon,
    make_decision,
    move_player,
    new_game,
    use_item,
)


def show_menu():
    """Display the main game menu."""
    print("\nWhat would you like to do?")
    print("1. Explore")
    print("2. Check status and inventory")
    print("3. Make a decision at this location")
    print("4. Use an item")
    print("5. Light the lighthouse beacon")
    print("6. Quit")


def run_game():
    """Run one complete play-through; injectable I/O makes it testable."""
    

    print("=" * 48)
    print("MYSTERY ISLAND: THE LOST LIGHTHOUSE")
    print("=" * 48)
    print(
        "A storm has stranded you on a remote island. "
        "Find the tools, make wise choices, and restore the beacon."
    )

    state = new_game(input("Enter your name: "))
    print("\nWelcome, {}!".format(state.player_name))
    print("You begin on the Beach with 5 energy.")
    print("Locations: " + " -> ".join(LOCATIONS))

    while not state.game_over and not state.won:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\nLocations: " + ", ".join(LOCATIONS))
            destination = input("Where would you like to go? ")
            print(move_player(state, destination))

        elif choice == "2":
            print(get_status(state))

        elif choice == "3":
            if state.location == "Beach":
                print("Beach decision: 'salvage' or 'map'")
            elif state.location == "Jungle":
                print("Jungle decision: 'herbs' or 'ridge'")
            elif state.location == "Cave":
                print("Cave decision: 'ledge' or 'pool' (pool costs energy)")
            else:
                print("There is no special decision at this location.")
                continue
            decision = input("Your choice: ")
            print(make_decision(state, decision))

        elif choice == "4":
            print("Usable items: Energy Pack, Herbal Remedy")
            item = input("Which item would you like to use? ")
            print(use_item(state, item))

        elif choice == "5":
            print(light_beacon(state))

        elif choice == "6":
            print("You leave the island behind. Thanks for playing!")
            break

        else:
            print("Invalid menu option. Enter a number from 1 to 6.")

        print(get_status(state))

    if state.won:
        print("\nMISSION COMPLETE")
    elif state.game_over:
        print("\nGAME OVER — your energy has run out.")

    return state


def main():
    """Program entry point."""
    run_game()


if __name__ == "__main__":
    main()
