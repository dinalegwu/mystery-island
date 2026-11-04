# Mystery Island: The Lost Lighthouse

A text-based Python adventure game about survival, exploration, and restoring a lighthouse beacon after a storm.

## Features

- Five connected locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- A state-based game engine separated from the command-line interface.
- Energy management and item-gated progression.
- One-time decisions at the Beach, Jungle, and Cave.
- Collectible items, including the Lantern and Rope needed to complete the mission.
- Reusable healing items and one-use shortcut maps.
- Clear victory, game-over, and quit paths.
- Automated unit tests using Python's standard library.

## Requirements

- Python 3.8 or newer.
- No third-party packages are required.

## Run the game

```bash
python3 main.py
```

On Windows, use `python main.py` if `python3` is unavailable.

## Run the tests

```bash
python3 -m unittest discover -s tests -v
```

## How to play

1. Enter a player name.
2. Choose **Explore** to travel to a neighbouring location.
3. Check your status to see your energy and inventory.
4. Make the special decision available at the Beach, Jungle, and Cave.
5. Use an Energy Pack or Herbal Remedy when your energy is low.
6. Reach the Lighthouse with the Lantern and light the beacon.

### Locations and important items

| Location | Discovery or requirement |
| --- | --- |
| Beach | Choose to salvage supplies or study a map. |
| Jungle | Collect the Lantern; choose herbs or the ridge route. |
| Cave | Collect the Rope; choose the dry ledge or the pool. |
| Old Bridge | The Rope is required to continue. |
| Lighthouse | The Lantern is required to light the beacon. |

### Decisions

- **Beach:** Salvage an Energy Pack for later recovery, or study a Weathered Map to make one move free.
- **Jungle:** Gather a Herbal Remedy, or climb the ridge to obtain a one-use shortcut map.
- **Cave:** Search the dry ledge for a Crystal, or search the pool for a Pearl at the cost of energy.

Each location decision can be made only once per play-through.

### Energy rules

- You start with 5 energy; the maximum is 5.
- A normal successful move costs 1 energy.
- A map makes one successful move free and is then consumed.
- The Cave pool decision costs 1 energy.
- Energy Packs restore up to 2 energy; Herbal Remedies restore up to 1.
- Invalid moves and blocked routes do not consume energy.
- Running out of energy before completing the mission ends the game.

## Project structure

```text
mystery-island/
├── game.py              # Game state and rules (no terminal input/output)
├── main.py              # Command-line interface and program entry point
├── tests/
│   └── test_game.py     # Automated game-rule tests
├── .github/
│   └── workflows/
│       └── tests.yml    # Automated tests on pushes and pull requests
├── .gitignore
└── README.md
```

## Design notes

The game engine lives in `game.py` and works with a `GameState` object. The interface lives in `main.py`. This separation makes game rules easier to test without simulating a player's keyboard input. The `run_game` function accepts injectable input and output functions for future command-line integration tests.

The project intentionally uses only the Python standard library. Save files, graphical interfaces, sound, and online features are outside the current scope.
