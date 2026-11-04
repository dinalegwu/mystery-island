"""Automated tests for Mystery Island game rules."""

import unittest

from game import (
    GameState,
    light_beacon,
    make_decision,
    move_player,
    new_game,
    use_item,
)


class TestGameSetup(unittest.TestCase):
    def test_new_game_has_expected_defaults(self):
        state = new_game("  Dorcas  ")
        self.assertEqual(state.player_name, "Dorcas")
        self.assertEqual(state.location, "Beach")
        self.assertEqual(state.energy, 5)
        self.assertEqual(state.inventory, [])

    def test_blank_name_uses_explorer(self):
        self.assertEqual(new_game(" ").player_name, "Explorer")


class TestMovement(unittest.TestCase):
    def test_successful_move_and_lantern_collection(self):
        state = new_game("Dorcas")
        message = move_player(state, "  jUnGlE ")
        self.assertEqual(state.location, "Jungle")
        self.assertEqual(state.energy, 4)
        self.assertIn("Lantern", state.inventory)
        self.assertIn("Jungle", message)

    def test_invalid_location_does_not_change_state(self):
        state = new_game("Dorcas")
        message = move_player(state, "Desert")
        self.assertIn("does not exist", message)
        self.assertEqual((state.location, state.energy), ("Beach", 5))

    def test_cannot_skip_a_location(self):
        state = new_game("Dorcas")
        message = move_player(state, "Cave")
        self.assertIn("cannot skip", message)
        self.assertEqual(state.energy, 5)

    def test_same_location_does_not_cost_energy(self):
        state = new_game("Dorcas")
        move_player(state, "Beach")
        self.assertEqual(state.energy, 5)

    def test_rope_is_collected_in_cave(self):
        state = new_game("Dorcas")
        move_player(state, "Jungle")
        move_player(state, "Cave")
        self.assertIn("Rope", state.inventory)

    def test_rope_is_required_for_bridge(self):
        state = GameState("Dorcas", location="Cave", energy=3)
        message = move_player(state, "Old Bridge")
        self.assertIn("Rope", message)
        self.assertEqual(state.location, "Cave")
        self.assertEqual(state.energy, 3)

    def test_lantern_is_required_for_lighthouse(self):
        state = GameState("Dorcas", location="Old Bridge", energy=2,
                          inventory=["Rope"])
        message = move_player(state, "Lighthouse")
        self.assertIn("Lantern", message)
        self.assertEqual(state.location, "Old Bridge")

    def test_map_makes_one_move_free(self):
        state = new_game("Dorcas")
        make_decision(state, "map")
        move_player(state, "Jungle")
        self.assertEqual(state.energy, 5)
        self.assertNotIn("Weathered Map", state.inventory)

    def test_zero_energy_blocks_movement(self):
        state = GameState("Dorcas", energy=0)
        message = move_player(state, "Jungle")
        self.assertEqual(state.location, "Beach")
        self.assertIn("energy", message.casefold())


class TestDecisionsAndItems(unittest.TestCase):
    def test_beach_salvage_gives_energy_pack(self):
        state = new_game("Dorcas")
        self.assertIn("Energy Pack", make_decision(state, "salvage"))
        self.assertIn("Energy Pack", state.inventory)

    def test_decision_can_only_be_made_once_per_location(self):
        state = new_game("Dorcas")
        make_decision(state, "salvage")
        message = make_decision(state, "map")
        self.assertIn("already made", message)
        self.assertNotIn("Weathered Map", state.inventory)

    def test_jungle_herbs_gives_remedy(self):
        state = new_game("Dorcas")
        move_player(state, "Jungle")
        make_decision(state, "herbs")
        self.assertIn("Herbal Remedy", state.inventory)

    def test_cave_pool_costs_energy(self):
        state = GameState("Dorcas", location="Cave", energy=4,
                          inventory=["Lantern", "Rope"])
        make_decision(state, "pool")
        self.assertEqual(state.energy, 3)
        self.assertIn("Pearl", state.inventory)

    def test_energy_pack_restores_energy_and_is_consumed(self):
        state = GameState("Dorcas", energy=2, inventory=["Energy Pack"])
        use_item(state, "energy pack")
        self.assertEqual(state.energy, 4)
        self.assertNotIn("Energy Pack", state.inventory)

    def test_energy_cannot_exceed_maximum(self):
        state = GameState("Dorcas", energy=4, inventory=["Energy Pack"])
        use_item(state, "Energy Pack")
        self.assertEqual(state.energy, 5)


class TestEnding(unittest.TestCase):
    def test_beacon_cannot_be_lit_from_beach(self):
        state = new_game("Dorcas")
        self.assertIn("reach the Lighthouse", light_beacon(state))
        self.assertFalse(state.won)

    def test_complete_winning_journey(self):
        state = new_game("Dorcas")
        move_player(state, "Jungle")
        move_player(state, "Cave")
        move_player(state, "Old Bridge")
        move_player(state, "Lighthouse")
        message = light_beacon(state)
        self.assertTrue(state.won)
        self.assertIn("rescue boat", message)

    def test_game_over_player_cannot_win(self):
        state = GameState("Dorcas", energy=0, game_over=True)
        self.assertIn("game is over", light_beacon(state))


if __name__ == "__main__":
    unittest.main()
