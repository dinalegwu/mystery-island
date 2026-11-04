import unittest
from game import move_player


class TestMovement(unittest.TestCase):

    def test_successful_movement(self):
        location, energy, message = move_player("Beach", "Jungle", 5)
        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)
        self.assertEqual(message, "Movement successful!")

    def test_same_location(self):
        location, energy, message = move_player("Beach", "Beach", 5)
        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)
        self.assertEqual(message, "You are already here!")

    def test_invalid_location(self):
        location, energy, message = move_player("Beach", "Desert", 5)
        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)
        self.assertEqual(message, "Invalid location.")

    def test_empty_destination(self):
        location, energy, message = move_player("Beach", "", 5)
        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)
        self.assertEqual(message, "Invalid location.")

    def test_whitespace_and_case_insensitive_location(self):
        location, energy, message = move_player("Beach", "  jUnGlE  ", 5)
        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)
        self.assertEqual(message, "Movement successful!")

    def test_zero_energy(self):
        location, energy, message = move_player("Beach", "Jungle", 0)
        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 0)
        self.assertEqual(message, "You have run out of energy!")

    def test_cannot_skip_location(self):
        location, energy, message = move_player("Beach", "Cave", 5)
        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)
        self.assertEqual(message, "You cannot skip locations!")

    def test_move_backwards(self):
        location, energy, message = move_player("Cave", "Jungle", 5)
        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)
        self.assertEqual(message, "Movement successful!")

    def test_move_forward(self):
        location, energy, message = move_player("Jungle", "Cave", 5)
        self.assertEqual(location, "Cave")
        self.assertEqual(energy, 4)
        self.assertEqual(message, "Movement successful!")

    def test_last_energy_point_allows_one_move(self):
        location, energy, message = move_player("Beach", "Jungle", 1)
        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 0)
        self.assertEqual(message, "Movement successful!")

    def test_energy_cannot_become_negative(self):
        location, energy, message = move_player("Beach", "Jungle", 0)
        self.assertEqual(location, "Beach")
        self.assertGreaterEqual(energy, 0)
        self.assertEqual(message, "You have run out of energy!")

    def test_cannot_move_after_energy_reaches_zero(self):
        location, energy, message = move_player("Beach", "Jungle", 1)
        self.assertEqual((location, energy), ("Jungle", 0))

        location, energy, message = move_player(location, "Cave", energy)
        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 0)
        self.assertEqual(message, "You have run out of energy!")


if __name__ == "__main__":
    unittest.main()
