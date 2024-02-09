import os

import numpy as np
import cv2 as cv

from src.constants import AUX_DATA_PATH


########################################################################################################################
# IMAGE GETTERS
########################################################################################################################


def get_images(path: str) -> dict[tuple[int, int], np.ndarray]:
    """
    Get all the data (sorted) from a given path.
    :param path:
    :return: a dictionary with the key a tuple containing the game number and the turn number and the value the image as a numpy array
    """
    images = {}
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            # File example: 1_01.jpg
            file_name = file.rstrip(".jpg")
            game_number, turn = file_name.split("_")
            turn = int(turn)
            game_number = int(game_number)
            image = cv.imread(os.path.join(path, file))
            images[(game_number, turn)] = image

    images = dict(sorted(images.items(), key=lambda item: (item[0], item[1])))  # sort by game, then by turn

    return images


def get_auxiliary_images() -> dict[str, np.ndarray]:
    """
    Get all the data (sorted) from the auxiliary data folder.
    :return: a dictionary with the key the image number and the value the image as a numpy array
    """
    aux_images = {}
    for file in os.listdir(AUX_DATA_PATH):
        if file.endswith(".jpg"):
            # File example: name.jpg
            image_name = file.rstrip(".jpg")
            image = cv.imread(os.path.join(AUX_DATA_PATH, file))
            aux_images[image_name] = image

    return aux_images


########################################################################################################################
# GAME GETTERS
########################################################################################################################
def get_game_moves(path: str) -> dict[tuple[int, int], str]:
    """
    Get all the moves from a given game sorted by game_number and turn_number.
    :param path: the path to the mode (train or test)
    :return: a dictionary with the key a tuple of (game_number, turn_number) and the value the player that made the move
    """
    game_moves = {}
    for file in os.listdir(path):
        if file.endswith("_mutari.txt"):
            # File example: 1_mutari.txt
            file_name = file.rstrip("_mutari.txt")
            game_number = int(file_name)
            with open(os.path.join(path, file), "r") as turns:
                # Example of a line: 1_01.jpg player2
                for turn in turns.readlines():
                    # Remove the new line character
                    turn = turn.strip("\n")
                    # Skip empty lines
                    if turn == "":
                        continue

                    image_file, player = turn.split(" ")
                    turn_number = int(image_file.split("_")[1].rstrip(".jpg"))
                    game_moves[(game_number, turn_number)] = player

    game_moves = dict(sorted(game_moves.items(), key=lambda item: (item[0], item[1])))  # sort by game, then by turn
    return game_moves
