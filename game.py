LOCATIONS = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]


def move_player(location, destination, energy):
    destination = destination.strip()

    found_location = None

    for place in LOCATIONS:
        if destination.casefold() == place.casefold():
            found_location = place
            break

    if found_location is None:
        return location, energy, "Invalid location."

    if found_location == location:
        return location, energy, "You are already here!"

    if energy <= 0:
        return location, energy, "You have run out of energy!"

    current_index = LOCATIONS.index(location)
    destination_index = LOCATIONS.index(found_location)

    if abs(destination_index - current_index) != 1:
        return location, energy, "You cannot skip locations!"

    energy -= 1
    location = found_location

    return location, energy, "Movement successful!"