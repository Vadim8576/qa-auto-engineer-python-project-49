from brain_games.game import game
from brain_games.utils.brain_utils import (
    get_operator,
    get_random_number,
    get_result_expression,
)


def get_game_data():
    min_number = 0
    max_number = 100

    value1 = get_random_number(min_number, max_number)
    value2 = get_random_number(min_number, max_number)
    
    operator = get_operator()

    question = f'{value1} {operator} {value2}'
    correct_answer = get_result_expression(operator, value1, value2)
   
    return {
        question: question,
        correct_answer: correct_answer
    }


def start_game():
    task = 'What is the result of the expression?'
    game(get_game_data, task)