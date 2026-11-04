import unittest
from game import move_player


class TestMovement(unittest.TestCase):

    def test_successful_movement(self):
        location, energy, message = move_player("Beach", "Jungle", 5)
        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)

    def test_same_location(self):
        location, energy, message = move_player("Beach", "Beach", 5)
        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)

    def test_invalid_location(self):
        location, energy, message = move_player("Beach", "Desert", 5)
        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)

    def test_lowercase_location(self):
        location, energy, message = move_player("Beach", "jungle", 5)
        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)

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

    def test_move_forward(self):
        location, energy, message = move_player("Jungle", "Cave", 5)
        self.assertEqual(location, "Cave")
        self.assertEqual(energy, 4)


if __name__ == "__main__":
    unittest.main()