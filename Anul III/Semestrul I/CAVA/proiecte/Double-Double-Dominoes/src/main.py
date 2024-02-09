from src.constants import (
    SCORE_BOARD,
    P1,
    P2,
    MODE,
    TRAIN_DATA_PATH,
    NUMBER_OF_GAMES,
    NUMBER_OF_TURNS,
    TEST_DATA_PATH,
    TEST_NUMBER_OF_GAMES,
    TEST_NUMBER_OF_TURNS,
    BONUS_BOARD,
    AUGMENT_DATA,
    AUGMENT_DATA_PATH,
)
import numpy as np

from src.utils.augment_data import augment_data
from src.utils.board_extraction import extract_board
from src.utils.classification import classify
from src.utils.detection import get_positions
from src.utils.formatters import create_solution_txt_file
from src.utils.readers import get_images, get_game_moves
from src.utils.templates import generate_templates


class Player:
    def __init__(self, player: str):
        self.player = player
        self.score = 0
        self.position_value = -1
        self.total_score = 0

    def update_score(self, bonus_position: int = 0, bonus_value: int = 0):
        self.score = bonus_position + bonus_value
        self.total_score += self.score

    def update_position_value(self):
        if self.total_score > 0:
            self.position_value = SCORE_BOARD[self.total_score - 1]

    def __str__(self):
        return f"Player: {str(self.player)}, Score: {str(self.score)}, Position value: {str(self.position_value)}"


class HalfPiece:
    def __init__(self):
        self.position: tuple[int, int] = (1, 1)
        self.value: int = 1

    def set_position(self, position: tuple[int, int]):
        self.position = position

    def set_value(self, value: int):
        self.value = value

    def __str__(self):
        return f"Half piece: {str(self.position)}, Value: {str(self.value)}"


class DominoPiece:
    def __init__(self):
        self.half_pieces: tuple[HalfPiece, HalfPiece] = (HalfPiece(), HalfPiece())

    def is_double(self):
        return self.half_pieces[0].value == self.half_pieces[1].value

    def get_positions(self):
        return self.half_pieces[0].position, self.half_pieces[1].position

    def get_values(self):
        return self.half_pieces[0].value, self.half_pieces[1].value

    def __str__(self):
        return f"Domino piece: {str(self.half_pieces[0])}, {str(self.half_pieces[1])}"


class Turn:
    def __init__(
            self,
            turn_number: int,
            player: Player,
            image: np.ndarray,
            domino_piece: DominoPiece,
    ):
        self.turn_number = turn_number
        self.player = player
        self.image = image
        self.domino_piece = domino_piece

    def update_image(self, image: np.ndarray):
        self.image = image

    def __str__(self):
        return f"Turn number: {str(self.turn_number)}, {str(self.player)}, {str(self.domino_piece)}"

    def __int__(self):
        return self.turn_number


class Game:
    def __init__(self, game_number: int, turns: list[Turn]):
        self.game_number = game_number
        self.turns = turns
        self.players = {P1: Player(P1), P2: Player(P2)}

    def __str__(self):
        turns = "\n".join([str(turn) for turn in self.turns])
        return f"Game number: {str(self.game_number)}, Turns: {turns}"

    def __int__(self):
        return self.game_number


def init():
    if AUGMENT_DATA:
        augment_data()

    if MODE == "train":
        path = TRAIN_DATA_PATH
        games_number = NUMBER_OF_GAMES
        turns_number = NUMBER_OF_TURNS
        if AUGMENT_DATA:
            images = get_images(AUGMENT_DATA_PATH)
        else:
            images = get_images(path)
        moves = get_game_moves(path)

    else:  # MODE == 'test'
        path = TEST_DATA_PATH
        games_number = TEST_NUMBER_OF_GAMES
        turns_number = TEST_NUMBER_OF_TURNS
        images = get_images(path)
        moves = get_game_moves(path)

    games = []

    for game_number in range(1, games_number + 1):  # 1, 2, 3, 4, 5
        game = Game(game_number, [])
        for turn_number in range(1, turns_number + 1):  # 1, 2, 3, ..., 20
            current_player = moves[(game_number, turn_number)]  # 'player1' or 'player2'
            current_image = images[(game_number, turn_number)]
            turn = Turn(
                turn_number=turn_number,
                player=game.players[current_player],
                image=current_image,
                domino_piece=DominoPiece(),
            )
            game.turns.append(turn)

        games.append(game)

    return games


if __name__ == "__main__":
    generate_templates()
    games: list[Game] = init()

    # Extract board from image and update turn image
    for game in games:
        for turn in game.turns:
            turn.update_image(extract_board(turn.image))

    for game in games:
        domino_pieces_positions = []
        for turn in game.turns:
            ##############################
            # POSITION DETECTION
            ##############################
            new_domino_pieces_positions = get_positions(turn.image, domino_pieces_positions)

            # Handle case when no domino piece is detected or only one is detected
            if len(new_domino_pieces_positions) > 2:
                if len(new_domino_pieces_positions) == 0:
                    new_domino_pieces_positions = ((0, 0), (0, 1))
                else:
                    new_domino_pieces_positions = (new_domino_pieces_positions[0], (0, 0))

            new_zip = zip(new_domino_pieces_positions, turn.domino_piece.half_pieces)
            for position, half_piece in new_zip:
                half_piece.set_position(position)

            # update domino pieces positions
            for position in new_domino_pieces_positions:
                domino_pieces_positions.append(position)

            ##############################

            ##############################
            # VALUE DETECTION
            ##############################
            for half_piece in turn.domino_piece.half_pieces:
                classified_value = classify(turn.image, half_piece.position)
                half_piece.set_value(classified_value)
            ##############################

            ##############################
            # SCORE CALCULATION
            ##############################
            bonus_position = 0
            bonus_value = 0

            current_player = turn.player
            opponent_player = game.players[P1] if current_player == game.players[P2] else game.players[P2]

            # Reward for position on score board
            values = turn.domino_piece.get_values()
            if current_player.position_value in values:
                bonus_value = 3
            if opponent_player.position_value in values:
                opponent_player.update_score(3)

            # Reward for position on table
            positions = turn.domino_piece.get_positions()
            for position in positions:
                if position in BONUS_BOARD:
                    if turn.domino_piece.is_double():
                        bonus_position = 2 * BONUS_BOARD[position]
                    else:
                        bonus_position = BONUS_BOARD[position]

            turn.player.update_score(bonus_position, bonus_value)

            current_player.update_position_value()
            opponent_player.update_position_value()
            ##############################

            create_solution_txt_file(
                int(game),
                int(turn),
                turn.domino_piece.get_positions(),
                turn.domino_piece.get_values(),
                turn.player.score,
            )
