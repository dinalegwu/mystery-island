"""Command-line integration tests using simulated player input."""

import unittest

from main import run_game


class TestCommandLineGame(unittest.TestCase):
    def run_with_inputs(self, responses):
        prompts = iter(responses)
        output = []
        state = run_game(
            input_fn=lambda prompt: next(prompts),
            output_fn=output.append,
        )
        return state, "\n".join(output)

    def test_quit_path(self):
        state, output = self.run_with_inputs(["Dorcas", "6"])
        self.assertFalse(state.won)
        self.assertIn("Thanks for playing", output)

    def test_invalid_menu_option_recovers(self):
        state, output = self.run_with_inputs(["Dorcas", "99", "6"])
        self.assertIn("Invalid menu option", output)
        self.assertFalse(state.won)

    def test_full_winning_journey(self):
        state, output = self.run_with_inputs([
            "Dorcas",
            "1", "Jungle",
            "3", "herbs",
            "1", "Cave",
            "3", "ledge",
            "1", "Old Bridge",
            "1", "Lighthouse",
            "5",
        ])
        self.assertTrue(state.won)
        self.assertIn("MISSION COMPLETE", output)
        self.assertIn("rescue boat", output)

    def test_item_menu_shows_only_items_in_inventory(self):
        state, output = self.run_with_inputs([
            "Dorcas",
            "1", "Jungle",
            "3", "herbs",
            "4", "Herbal Remedy",
            "6",
        ])
        self.assertIn("Usable items: Herbal Remedy", output)
        self.assertNotIn("Usable items: Energy Pack", output)
        self.assertNotIn("Usable items: Energy Pack, Herbal Remedy", output)
        self.assertNotIn("Herbal Remedy", state.inventory)

    def test_item_menu_explains_when_no_items_are_usable(self):
        state, output = self.run_with_inputs(["Dorcas", "4", "6"])
        self.assertIn("You have no usable items right now.", output)
        self.assertFalse(state.won)


if __name__ == "__main__":
    unittest.main()
