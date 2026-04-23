from brain_games.game import game
from brain_games.utils.brain_utils import (
    get_random_number,
    is_even,
)


def get_game_data():
    MIN_NUMBER = 0
    MAX_NUMBER = 100

    question = get_random_number(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'

    return {
        'question': str(question),
        'correct_answer': correct_answer,
    }


def start_game():
    TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
    game(get_game_data, TASK)