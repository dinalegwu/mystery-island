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


def show_menu(output_fn=print):
    """Display the main game menu."""
    print("\nWhat would you like to do?")
    output_fn("1. Explore")
    output_fn("2. Check status and inventory")
    output_fn("3. Make a decision at this location")
    output_fn("4. Use an item")
    output_fn("5. Light the lighthouse beacon")
    output_fn("6. Quit")


def run_game(input_fn=None, output_fn=print):
    """Run one complete play-through; injectable I/O makes it testable."""
    read = input_fn or input
    write = output_fn

    write("=" * 48)
    write("MYSTERY ISLAND: THE LOST LIGHTHOUSE")
    write("=" * 48)
    write(
        "A storm has stranded you on a remote island. "
        "Find the tools, make wise choices, and restore the beacon."
    )

    state = new_game(read("Enter your name: "))
    write("\nWelcome, {}!".format(state.player_name))
    write("You begin on the Beach with 5 energy.")
    write("Locations: " + " -> ".join(LOCATIONS))

    while not state.game_over and not state.won:
        show_menu(write)
        choice = read("Choose an option: ").strip()

        if choice == "1":
            write("\nLocations: " + ", ".join(LOCATIONS))
            destination = read("Where would you like to go? ")
            write(move_player(state, destination))

        elif choice == "2":
            write(get_status(state))

        elif choice == "3":
            if state.location == "Beach":
                write("Beach decision: 'salvage' or 'map'")
            elif state.location == "Jungle":
                write("Jungle decision: 'herbs' or 'ridge'")
            elif state.location == "Cave":
                write("Cave decision: 'ledge' or 'pool' (pool costs energy)")
            else:
                write("There is no special decision at this location.")
                continue
            decision = read("Your choice: ")
            write(make_decision(state, decision))

        elif choice == "4":
            write("Usable items: Energy Pack, Herbal Remedy")
            item = read("Which item would you like to use? ")
            write(use_item(state, item))

        elif choice == "5":
            write(light_beacon(state))

        elif choice == "6":
            write("You leave the island behind. Thanks for playing!")
            break

        else:
            write("Invalid menu option. Enter a number from 1 to 6.")

        write(get_status(state))

    if state.won:
        write("\nMISSION COMPLETE")
    elif state.game_over:
        write("\nGAME OVER — your energy has run out.")

    return state


def main():
    """Program entry point."""
    run_game()


if __name__ == "__main__":
    main()
