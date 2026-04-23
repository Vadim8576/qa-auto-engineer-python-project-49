from brain_games.game import game
from brain_games.utils.brain_even_utils import (
    get_gcd,
    get_random_number,
)


def get_game_data():
    min_number = 0
    max_number = 100

    value1 = get_random_number(min_number, max_number)
    value2 = get_random_number(min_number, max_number)

    question = f'{value1} {value2}'
    correct_answer = get_gcd(value1, value2)
   
    return {
        question: question,
        correct_answer: correct_answer
    }


def start_game():
    task = 'Find the greatest common divisor of given numbers.'
    game(get_game_data, task)