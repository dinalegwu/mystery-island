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
    output_fn("\nWhat would you like to do?")
    output_fn("1. Explore")
    output_fn("2. Check status and inventory")
    output_fn("3. Make a decision at this location")
    output_fn("4. Use an item")
    output_fn("5. Light the lighthouse beacon")
    output_fn("6. Quit")


def run_game(input_fn=input, output_fn=print):
    """Run one complete play-through with injectable input and output."""
    output_fn("=" * 48)
    output_fn("MYSTERY ISLAND: THE LOST LIGHTHOUSE")
    output_fn("=" * 48)
    output_fn(
        "A storm has stranded you on a remote island. "
        "Find the tools, make wise choices, and restore the beacon."
    )

    state = new_game(input_fn("Enter your name: "))
    output_fn("\nWelcome, {}!".format(state.player_name))
    output_fn("You begin on the Beach with 5 energy.")
    output_fn("Locations: " + " -> ".join(LOCATIONS))

    while not state.game_over and not state.won:
        show_menu(output_fn)
        choice = input_fn("Choose an option: ").strip()

        if choice == "1":
            output_fn("\nLocations: " + ", ".join(LOCATIONS))
            destination = input_fn("Where would you like to go? ")
            output_fn(move_player(state, destination))

        elif choice == "2":
            # The status is displayed once at the end of this loop.
            pass

        elif choice == "3":
            if state.location == "Beach":
                output_fn("Beach decision: 'salvage' or 'map'")
            elif state.location == "Jungle":
                output_fn("Jungle decision: 'herbs' or 'ridge'")
            elif state.location == "Cave":
                output_fn("Cave decision: 'ledge' or 'pool' (pool costs energy)")
            else:
                output_fn("There is no special decision at this location.")
                output_fn(get_status(state))
                continue
            decision = input_fn("Your choice: ")
            output_fn(make_decision(state, decision))

        elif choice == "4":
            usable_items = [
                item for item in ("Energy Pack", "Herbal Remedy")
                if item in state.inventory
            ]
            if state.energy >= 5:
                usable_items = []

            if not usable_items:
                output_fn("You have no usable items right now.")
            else:
                output_fn("Usable items: " + ", ".join(usable_items))
                item = input_fn("Which item would you like to use? ")
                output_fn(use_item(state, item))

        elif choice == "5":
            output_fn(light_beacon(state))

        elif choice == "6":
            output_fn("You leave the island behind. Thanks for playing!")
            break

        else:
            output_fn("Invalid menu option. Enter a number from 1 to 6.")

        output_fn(get_status(state))

    if state.won:
        output_fn("\nMISSION COMPLETE")
    elif state.game_over:
        output_fn("\nGAME OVER — your energy has run out.")

    return state


def main():
    """Program entry point."""
    run_game()


if __name__ == "__main__":
    main()
