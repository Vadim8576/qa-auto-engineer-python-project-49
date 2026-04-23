from brain_games.game import game
from brain_games.utils.brain_utils import (
    get_gcd,
    get_random_number,
)


def get_game_data():
    MIN_NUMBER = 0
    MAX_NUMBER = 100

    value1 = get_random_number(MIN_NUMBER, MAX_NUMBER)
    value2 = get_random_number(MIN_NUMBER, MAX_NUMBER)

    question = f'{value1} {value2}'
    correct_answer = get_gcd(value1, value2)
   
    return {
        'question': question,
        'correct_answer': correct_answer
    }


def start_game():
    TASK = 'Find the greatest common divisor of given numbers.'
    game(get_game_data, TASK)