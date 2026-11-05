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

1. Enter a player name when the game starts.
2. Use the numbered menu to choose an action:

   | Option | Action |
   | --- | --- |
   | 1 | Explore and travel to a neighbouring location. |
   | 2 | Check your current location, energy, and inventory. |
   | 3 | Make the special decision at the Beach, Jungle, or Cave. |
   | 4 | Use an available healing item from your inventory. |
   | 5 | Light the lighthouse beacon when you reach the Lighthouse with the Lantern. |
   | 6 | Quit the game. |

3. Travel one connected location at a time. You cannot skip directly to a distant location.
4. Successful normal travel costs 1 energy. Invalid destinations and blocked routes do not cost energy.
5. Make each location's special decision only once. The game prevents a second decision at the same location.
6. Check your status regularly. The status line shows your location, current energy, and inventory.
7. When using an item, choose its displayed full name (for example, `Herbal Remedy` or `Energy Pack`). Only healing items you own and can currently use are listed; healing items are not usable when your energy is already full.
8. Reach the Lighthouse with the Lantern and choose the beacon option to win.

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
│   ├── test_game.py     # Automated game-rule tests
│   └── test_cli.py      # Simulated command-line journeys
├── .github/
│   └── workflows/
│       └── tests.yml    # Automated tests on pushes and pull requests
├── .gitignore
└── README.md
```

## Design notes

The game engine lives in `game.py` and works with a `GameState` object. The interface lives in `main.py`. This separation makes game rules easier to test without simulating a player's keyboard input. The `run_game` function accepts injectable input and output functions for future command-line integration tests.

The project intentionally uses only the Python standard library. Save files, graphical interfaces, sound, and online features are outside the current scope.

## Completion evidence

### Repository and version details

- **GitHub repository:** https://github.com/dinalegwu/mystery-island
- **Working branch submitted for review:** `odogwu`
- **Final commit SHA:** After the final commit, run `git log -1 --format=%H` and paste the full result here.
- **Python version used for testing:** Run `python3 --version` and record the exact output here.

### Run instructions

From the repository folder, run the game:

```bash
python3 main.py
```

Run the automated tests:

```bash
python3 -m unittest discover -s tests -v
```

### Test evidence

The latest test result reported during local testing was:

```text
Ran 25 tests in 0.001s

OK
```

Run the tests again before submission and replace this with the exact output from your final run if it differs.

### AI learning log

Complete both entries using your own words and the experiments you actually performed.

**Entry 1**

- **Topic:** [Name the Python or game-development concept.]
- **What AI said:** [Briefly explain the guidance AI gave you.]
- **Your experiment:** [Describe the code you tried or the test you ran.]
- **Your conclusion:** [Explain what you learned from the result.]

**Entry 2**

- **Topic:** [Name a different concept.]
- **What AI said:** [Briefly explain the guidance AI gave you.]
- **Your experiment:** [Describe the code you tried or the test you ran.]
- **Your conclusion:** [Explain what you learned from the result.]

### Personal reflection

Complete this paragraph in your own words:

> The concept I understand now that I didn't before is... [Explain the concept, what confused you at first, and what helped you understand it.]
