# Mystery Island: The Lost Lighthouse

A beginner-friendly, text-based Python adventure game. After a storm leaves you stranded on Mystery Island, explore the island, collect useful items, and restore the lighthouse beacon so you can be rescued.

## Requirements

- Python 3.8 or newer (the project uses only Python's standard library).
- A terminal or command prompt.

## Getting started

1. Clone the repository:
   ```bash
   git clone https://github.com/dinalegwu/mystery-island.git
   ```
2. Move into the project directory:
   ```bash
   cd mystery-island
   ```
3. Start the game:
   ```bash
   python3 main.py
   ```

On Windows, you can use `python main.py` if `python3` is not available.

## How to play

Enter your name when prompted, then choose an option from the menu:

| Option | Action |
| --- | --- |
| 1 | Explore and enter a destination |
| 2 | Check your inventory |
| 3 | Try to light the lighthouse beacon |
| 4 | Quit the game |

The island has five locations, connected in this order:

1. Beach
2. Jungle
3. Cave
4. Old Bridge
5. Lighthouse

Movement is limited to a neighbouring location. You cannot jump over a location. Location names are accepted without regard to letter case.

## Items and rules

- You begin at the Beach with **5 energy points**.
- Each successful move costs **1 energy point**. Invalid moves and attempts to stay in the same place do not use energy.
- You find the **Lantern** when you first enter the Jungle.
- You find the **Rope** when you first enter the Cave.
- You need the Rope to travel from the Cave to the Old Bridge.
- You need the Lantern to travel from the Old Bridge to the Lighthouse.
- Items are added to your inventory only once.
- You cannot move when your energy is zero.
- To win, reach the Lighthouse with the Lantern and choose **Light the Lighthouse beacon**.
- If your energy reaches zero before you complete the mission, the game ends.

## Running the tests

From the project root, run:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover the movement function in `game.py`, including valid movement, invalid destinations, case-insensitive location matching, movement limits, and energy handling.

## Project structure

```text
mystery-island/
├── main.py              # Game menu and main gameplay loop
├── game.py              # Location list and player movement logic
├── tests/
│   └── test_game.py     # Automated tests for movement
├── .gitignore
└── README.md
```

## Current scope and known limitations

This is an introductory command-line project. The automated test suite currently tests the movement function; the interactive menu, item collection, item gates, and complete win/loss journeys are not yet covered by automated tests. Those are useful next improvements.

The game currently uses a fixed island route and a small menu rather than a saved game system. Player progress is not stored after the program exits.
