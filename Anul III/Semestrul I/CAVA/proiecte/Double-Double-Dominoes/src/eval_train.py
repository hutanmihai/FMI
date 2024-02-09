import os
from src.constants import TRAIN_DATA_PATH, SOLUTION_PATH, NUMBER_OF_GAMES, NUMBER_OF_TURNS


########################################################################################################################
# GROUND TRUTH AND SOLUTION GETTERS
########################################################################################################################


def get_ground_truth() -> dict[tuple[int, int], str]:
    """
    Get all the ground truth values from the train data folder for each turn sorted by game_number and turn_number.
    :return: a dictionary with the key a tuple of (game_number, turn_number) and the value the ground truth string
    """
    ground_truths = {}
    for file in os.listdir(TRAIN_DATA_PATH):
        if file.endswith(".txt") and file.find("_mutari") == -1:
            # File example: 1_01.txt
            file_name = file.rstrip(".txt")
            game_number, turn = file_name.split("_")
            turn = int(turn)
            game_number = int(game_number)
            with open(os.path.join(TRAIN_DATA_PATH, file), "r") as ground_truth:
                ground_truths[(game_number, turn)] = ground_truth.read()

    ground_truths = dict(
        sorted(ground_truths.items(), key=lambda item: (item[0], item[1]))
    )  # sort by game, then by turn
    return ground_truths


def get_solution() -> dict[tuple[int, int], str]:
    solutions = {}
    for file in os.listdir(SOLUTION_PATH):
        if file.endswith(".txt"):
            # File example: 1_01.txt
            file_name = file.rstrip(".txt")
            game_number, turn = file_name.split("_")
            turn = int(turn)
            game_number = int(game_number)
            with open(os.path.join(SOLUTION_PATH, file), "r") as solution:
                solutions[(game_number, turn)] = solution.read()

    solutions = dict(sorted(solutions.items(), key=lambda item: (item[0], item[1])))  # sort by game, then by turn
    return solutions


def get_positions(dictionary: dict[tuple[int, int], str]) -> dict[tuple[int, int], tuple[str, str]]:
    positions = {}

    for k, v in dictionary.items():
        split = v.split("\n")
        pos1 = split[0].split(" ")[0]
        pos2 = split[1].split(" ")[0]
        positions[k] = (pos1, pos2)

    positions = dict(sorted(positions.items(), key=lambda item: (item[0], item[1])))  # sort by game, then by turn

    return positions


def get_values(dictionary: dict[tuple[int, int], str]) -> dict[tuple[int, int], tuple[str, str]]:
    values = {}
    for k, v in dictionary.items():
        split = v.split("\n")
        val1 = split[0].split(" ")[1]
        val2 = split[1].split(" ")[1]
        values[k] = (val1, val2)

    values = dict(sorted(values.items(), key=lambda item: (item[0], item[1])))  # sort by game, then by turn

    return values


def get_scores(dictionary: dict[tuple[int, int], str]) -> dict[tuple[int, int], int]:
    scores = {}

    for k, v in dictionary.items():
        score = v.split("\n")[2]
        scores[k] = int(score)

    scores = dict(sorted(scores.items(), key=lambda item: (item[0], item[1])))  # sort by game, then by turn

    return scores


if __name__ == "__main__":
    ground_truth = get_ground_truth()
    solution = get_solution()

    positions_truth = get_positions(ground_truth)
    positions_solution = get_positions(solution)

    values_truth = get_values(ground_truth)
    values_solution = get_values(solution)

    scores_truth = get_scores(ground_truth)
    scores_solution = get_scores(solution)

    counter_positions = 0
    counter_values = 0
    counter_scores = 0

    for i in range(1, NUMBER_OF_GAMES + 1):
        for j in range(1, NUMBER_OF_TURNS + 1):
            pos_truth = positions_truth[(i, j)]
            pos_sol = positions_solution[(i, j)]

            val_truth = values_truth[(i, j)]
            val_sol = values_solution[(i, j)]

            score_truth = scores_truth[(i, j)]
            score_sol = scores_solution[(i, j)]

            if pos_truth != pos_sol:
                counter_positions += 1
                print(f"POSITION:\nGame {i}, turn {j}:\n{pos_sol}\n!!!!!!!!!!!!!!!!!!!\n{pos_truth}\n")

            if val_truth != val_sol:
                counter_values += 1
                print(f"VALUES:\nGame {i}, turn {j}:\n{val_sol}\n!!!!!!!!!!!!!!!!!!!\n{val_truth}\n")

            if score_truth != score_sol:
                counter_scores += 1
                print(f"SCORE:\nGame {i}, turn {j}:\n{score_sol}\n!!!!!!!!!!!!!!!!!!!\n{score_truth}\n")

    print("WRONG POSITIONS:", counter_positions)
    print("WRONG VALUES:", counter_values)
    print("WRONG SCORES:", counter_scores)
