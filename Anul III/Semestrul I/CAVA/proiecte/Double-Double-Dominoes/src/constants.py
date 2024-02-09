from pathlib import Path

import numpy as np

# CONSTANTS USED FOR DEBUGGING
SHOW_BOARD_EXTRACTION_POINTS = False
SHOW_BOARD_LINES = False
SHOW_PATCHES = False
SHOW_TEMPLATES_ON_GENERATION = False
SHOW_PATCHES_PREPROCESSING = False
SHOW_DETECTED_PIECES = False
SHOW_BOARD_EXTRACTION_STEPS = False
SHOW_AUGMENTATION_STEPS = False

AUGMENT_DATA = False
PREPROCESS_PATCHES = True  # Preprocess the patches before classification and the templates at creation

MODE = "test"  # Mode of operation (train or test)

# TRAIN
TRAIN_DATA_PATH = Path("data/train")

# TEST
TEST_DATA_PATH = Path("data/test/data")
GROUND_TRUTH_PATH = Path("data/test/ground-truth")

# SOLUTION FOR BOTH TEST AND TRAIN
SOLUTION_PATH = Path("data/solution")

# TEMPLATES
TEMPLATES_PATH = Path("data/templates")
VERTICAL_TEMPLATES_PATH = TEMPLATES_PATH / "vertical"
HORIZONTAL_TEMPLATES_PATH = TEMPLATES_PATH / "horizontal"
CENTER_TEXT_PATH = Path("data/templates/center-text")

# AUXILIARY DATA
AUX_DATA_PATH = Path("data/auxiliary")
AUGMENT_DATA_PATH = Path("data/augment")

LOWERB_BOARD = np.array([80, 0, 0])  # Lower bound for board color (used in board extraction)
UPPERB_BOARD = np.array([102, 255, 255])  # Upper bound for board color (used in board extraction)

LOWERB_PIECE = np.array([78, 0, 158])
UPPERB_PIECE = np.array([123, 99, 255])

NUMBER_OF_GAMES = 5
NUMBER_OF_TURNS = 20

TEST_NUMBER_OF_GAMES = 5
TEST_NUMBER_OF_TURNS = 20

BOX_SIZE = 100  # Size of the box containing half a domino piece after board extraction and warp
BOARD_WIDTH = 15  # Number of columns in the board
BOARD_HEIGHT = 15  # Number of rows in the board

# Player types
P1 = "player1"
P2 = "player2"

CENTER_TEXT_POSITIONS = ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8))

NUMBER_LETTER_MAP = {  # Map from number to letter for writing the solution
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
}

SCORE_BOARD = (  # The score board for the game
    1,
    2,
    3,
    4,
    5,
    6,
    0,
    2,
    5,
    3,
    4,
    6,
    2,
    2,
    0,
    3,
    5,
    4,
    1,
    6,
    2,
    4,
    5,
    5,
    0,
    6,
    3,
    4,
    2,
    0,
    1,
    5,
    1,
    3,
    4,
    4,
    4,
    5,
    0,
    6,
    3,
    5,
    4,
    1,
    3,
    2,
    0,
    0,
    1,
    1,
    2,
    3,
    6,
    3,
    5,
    2,
    1,
    0,
    6,
    6,
    5,
    2,
    1,
    2,
    5,
    0,
    3,
    3,
    5,
    0,
    6,
    1,
    4,
    0,
    6,
    3,
    5,
    1,
    4,
    2,
    6,
    2,
    3,
    1,
    6,
    5,
    6,
    2,
    0,
    4,
    0,
    1,
    6,
    4,
    4,
    1,
    6,
    6,
    3,
)

BONUS_BOARD = {  # Where the bonus points are located on the board
    (0, 0): 5,
    (0, 14): 5,
    (14, 0): 5,
    (14, 14): 5,
    (0, 3): 4,
    (0, 11): 4,
    (1, 5): 4,
    (1, 9): 4,
    (3, 0): 4,
    (3, 14): 4,
    (5, 1): 4,
    (5, 13): 4,
    (9, 1): 4,
    (9, 13): 4,
    (11, 0): 4,
    (11, 14): 4,
    (13, 5): 4,
    (13, 9): 4,
    (14, 3): 4,
    (14, 11): 4,
    (0, 7): 3,
    (1, 2): 3,
    (1, 12): 3,
    (2, 1): 3,
    (2, 13): 3,
    (3, 3): 3,
    (3, 11): 3,
    (7, 0): 3,
    (7, 14): 3,
    (11, 3): 3,
    (11, 11): 3,
    (12, 1): 3,
    (12, 13): 3,
    (13, 2): 3,
    (13, 12): 3,
    (14, 7): 3,
    (2, 4): 2,
    (2, 10): 2,
    (3, 5): 2,
    (3, 9): 2,
    (4, 2): 2,
    (4, 12): 2,
    (5, 3): 2,
    (5, 11): 2,
    (9, 3): 2,
    (9, 11): 2,
    (10, 2): 2,
    (10, 12): 2,
    (11, 5): 2,
    (11, 9): 2,
    (12, 4): 2,
    (12, 10): 2,
    (4, 4): 1,
    (4, 6): 1,
    (4, 8): 1,
    (4, 10): 1,
    (5, 5): 1,
    (5, 9): 1,
    (6, 4): 1,
    (6, 10): 1,
    (8, 4): 1,
    (8, 10): 1,
    (9, 5): 1,
    (9, 9): 1,
    (10, 4): 1,
    (10, 6): 1,
    (10, 8): 1,
    (10, 10): 1,
}

# BOARD INTEREST POSITIONS FOR TEMPLATE GENERATION (WHERE THE DOMINOES ARE PLACED IN THE AUX IMAGES)
BOARD_INTEREST = {
    "vertical": {
        0: [(0, 0), (1, 0), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (1, 12)],
        1: [(0, 2), (3, 0), (4, 0), (4, 2), (4, 4), (4, 6), (4, 8), (4, 10)],
        2: [(0, 4), (3, 2), (6, 0), (7, 0), (7, 2), (7, 4), (7, 6), (7, 8)],
        3: [(0, 6), (3, 4), (6, 2), (9, 0), (10, 0), (10, 2), (10, 4), (10, 6)],
        4: [(0, 8), (3, 6), (6, 4), (9, 2), (12, 0), (13, 0), (13, 2), (13, 4)],
        5: [(0, 10), (3, 8), (6, 6), (9, 4), (12, 2), (9, 12), (9, 14), (10, 12)],
        6: [(0, 12), (3, 10), (6, 8), (9, 6), (12, 4), (10, 14), (12, 14), (13, 14)],
    },
    "horizontal": {
        0: [(0, 0), (0, 1), (0, 3), (0, 6), (0, 9), (0, 12), (2, 0), (2, 3)],
        1: [(0, 4), (2, 6), (2, 7), (2, 9), (2, 12), (4, 0), (4, 3), (4, 6)],
        2: [(0, 7), (2, 10), (4, 9), (4, 10), (4, 12), (6, 0), (6, 3), (6, 6)],
        3: [(0, 10), (2, 13), (4, 13), (6, 9), (6, 10), (6, 12), (8, 0), (8, 3)],
        4: [(0, 13), (4, 1), (6, 1), (6, 13), (8, 6), (8, 7), (8, 9), (8, 12)],
        5: [(2, 1), (4, 4), (6, 4), (8, 1), (8, 10), (10, 0), (10, 1), (10, 3)],
        6: [(2, 4), (4, 7), (6, 7), (8, 4), (8, 13), (10, 4), (10, 6), (10, 7)],
    },
}
