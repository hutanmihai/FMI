from src.constants import NUMBER_LETTER_MAP, SOLUTION_PATH


def format_single_digit_turn(turn: int) -> str:
    """
    Formats a single digit turn to a two digit turn.
    Example: 1 -> 01
    :param turn: the turn to format
    :return: the formatted turn
    """
    if turn < 10:
        return f"0{turn}"
    return str(turn)


def format_position_into_letter(position: tuple[int, int]) -> str:
    """
    Formats a position into a letter.
    Example: (10, 13) -> 10M
    """
    return f"{position[0] + 1}{NUMBER_LETTER_MAP[position[1] + 1]}"


def format_solution_text_output(
    position: tuple[tuple[int, int], tuple[int, int]],
    values: tuple[int, int],
    score: int,
) -> str:
    """
    Formats the solution text output.
    Example:
        8H 6
        8I 1
        5
    :param position: the position of the piece of domino
    :param values: the values of the piece of domino
    :param score: the score of the player
    """

    pos_val = {
        format_position_into_letter(position[0]): values[0],
        format_position_into_letter(position[1]): values[1],
    }

    positions_string_sorted = sorted(pos_val.items(), key=lambda item: (int(item[0][:-1]), item[0][-1]))

    return (
        f"{positions_string_sorted[0][0]} {positions_string_sorted[0][1]}\n"
        f"{positions_string_sorted[1][0]} {positions_string_sorted[1][1]}\n"
        f"{score}"
    )


########################################################################################################################
# SOLUTION WRITER
########################################################################################################################
def create_solution_txt_file(
    game: int,
    turn: int,
    position: tuple[tuple[int, int], tuple[int, int]] = ((5, 5), (5, 6)),
    values: tuple[int, int] = (5, 5),
    score: int = 0,
) -> None:
    """
    Creates a solution file for a given game and turn.
    :param game: the game number
    :param turn: the turn number
    :param position: the position of the piece of domino
    :param values: the values of the piece of domino
    :param score: the score of the player
    :return:
    """
    path = SOLUTION_PATH / f"{game}_{format_single_digit_turn(turn)}.txt"
    with open(str(path), "w") as file:
        file.write(format_solution_text_output(position, values, score))
