from brain_games.game import game
from brain_games.utils.brain_utils import (
    get_random_number,
    is_prime,
)


def get_game_data():
    min_number = 0
    max_number = 100

    question = get_random_number(min_number, max_number)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return {
        question: str(question),
        correct_answer: correct_answer,
    }


def start_game():
    task = 'Answer "yes" if the number is prime, otherwise answer "no".'
    game(get_game_data, task)