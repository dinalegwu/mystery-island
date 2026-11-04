"""Core rules and state transitions for Mystery Island: The Lost Lighthouse."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

LOCATIONS = ("Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse")
STARTING_ENERGY = 5
MAX_ENERGY = 5

LOCATION_ITEMS = {
    "Jungle": "Lantern",
    "Cave": "Rope",
}


@dataclass
class GameState:
    """All mutable information for one play-through."""

    player_name: str
    location: str = "Beach"
    energy: int = STARTING_ENERGY
    inventory: List[str] = field(default_factory=list)
    decisions: Dict[str, str] = field(default_factory=dict)
    clues: List[str] = field(default_factory=list)
    game_over: bool = False
    won: bool = False


def new_game(player_name: str) -> GameState:
    """Create a fresh game with a cleaned player name."""
    clean_name = player_name.strip() or "Explorer"
    return GameState(player_name=clean_name)


def _add_item(state: GameState, item: str) -> bool:
    """Add an item once; return True only when it is newly collected."""
    if item in state.inventory:
        return False
    state.inventory.append(item)
    return True


def move_player(state: GameState, destination: str) -> str:
    """Move one connected step, enforcing energy and item requirements."""
    if state.game_over or state.won:
        return "This game has already ended."

    requested = destination.strip().casefold()
    target = next(
        (place for place in LOCATIONS if place.casefold() == requested),
        None,
    )
    if target is None:
        return "That location does not exist. Check the location list."

    if target == state.location:
        return "You are already at that location."

    current_index = LOCATIONS.index(state.location)
    target_index = LOCATIONS.index(target)
    if abs(target_index - current_index) != 1:
        return "You cannot skip locations. Travel to a neighbouring location."

    required_item = None
    if state.location == "Cave" and target == "Old Bridge":
        required_item = "Rope"
    elif state.location == "Old Bridge" and target == "Lighthouse":
        required_item = "Lantern"

    if required_item and required_item not in state.inventory:
        return "You need the {} before you can continue.".format(required_item)

    if state.energy <= 0:
        state.game_over = True
        return "You have no energy left. Your journey is over."

    free_move_item = next(
        (item for item in ("Weathered Map", "Ridge Map")
         if item in state.inventory),
        None,
    )
    if free_move_item:
        state.inventory.remove(free_move_item)
        cost = 0
        cost_message = " Your map helped you find a quicker route."
    else:
        cost = 1
        cost_message = ""

    state.energy -= cost
    state.location = target

    collected = LOCATION_ITEMS.get(target)
    item_message = ""
    if collected and _add_item(state, collected):
        item_message = " You found the {}.".format(collected)

    if state.energy == 0 and target != "Lighthouse":
        state.game_over = True
        return (
            "You reached {}, but have no energy left. Game over.".format(target)
            + item_message
        )

    return "You travelled to {}.{}{}".format(target, cost_message, item_message)


def make_decision(state: GameState, choice: str) -> str:
    """Resolve one location-specific decision; each location is one-time."""
    if state.game_over or state.won:
        return "This game has already ended."

    place = state.location
    if place in state.decisions:
        return "You have already made your decision at the {}.".format(place)

    selected = choice.strip().casefold()

    options = {
        "Beach": {
            "salvage": ("Energy Pack", "You salvaged an Energy Pack."),
            "map": ("Weathered Map", "You studied a map of the island."),
        },
        "Jungle": {
            "herbs": ("Herbal Remedy", "You gathered a useful Herbal Remedy."),
            "ridge": ("Ridge Map", "You climbed the ridge and mapped a quicker route."),
        },
        "Cave": {
            "ledge": ("Crystal", "You found a crystal on the dry ledge."),
            "pool": ("Pearl", "You searched the pool and found a pearl."),
        },
    }

    if place not in options:
        return "There is no special decision available at this location."

    if selected not in options[place]:
        return "That is not one of the available choices."

    item, message = options[place][selected]
    state.decisions[place] = selected
    _add_item(state, item)

    if place == "Cave" and selected == "pool":
        if state.energy <= 1:
            state.energy = 0
            state.game_over = True
            return message + " The cold water exhausted your remaining energy."
        state.energy -= 1
        message += " The cold water cost you 1 energy."

    return message


def use_item(state: GameState, item_name: str) -> str:
    """Use a healing item from the inventory."""
    if state.game_over or state.won:
        return "This game has already ended."

    item = item_name.strip().casefold()
    usable = {
        "energy pack": ("Energy Pack", 2),
        "herbal remedy": ("Herbal Remedy", 1),
    }
    match = next(
        (details for key, details in usable.items() if key == item),
        None,
    )
    if match is None:
        return "That item cannot be used."

    item, boost = match
    if item not in state.inventory:
        return "You do not have that item."

    if state.energy >= MAX_ENERGY:
        return "Your energy is already full."

    state.inventory.remove(item)
    previous_energy = state.energy
    state.energy = min(MAX_ENERGY, state.energy + boost)
    restored = state.energy - previous_energy
    return "You used {} and restored {} energy.".format(item, restored)


def light_beacon(state: GameState) -> str:
    """Complete the rescue mission when its requirements are met."""
    if state.game_over:
        return "The game is over. Start a new game to try again."
    if state.location != "Lighthouse":
        return "You must reach the Lighthouse first."
    if "Lantern" not in state.inventory:
        return "You need the Lantern to light the beacon."

    state.won = True
    return (
        "The lighthouse beacon blazes across the sea. "
        "A rescue boat spots the signal. You made it, {}!".format(
            state.player_name
        )
    )


def get_status(state: GameState) -> str:
    """Return a concise player status summary."""
    inventory = ", ".join(state.inventory) if state.inventory else "Empty"
    return (
        "Location: {} | Energy: {}/{} | Inventory: {}".format(
            state.location, state.energy, MAX_ENERGY, inventory
        )
    )
