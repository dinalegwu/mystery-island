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

    def test_wrong_item_use_does_not_crash(self):
        state, output = self.run_with_inputs(["Dorcas", "4", "Lantern", "6"])
        self.assertIn("cannot be used", output)
        self.assertFalse(state.won)


if __name__ == "__main__":
    unittest.main()
