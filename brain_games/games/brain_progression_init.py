from brain_games.game import game
from brain_games.utils.brain_utils import (
    get_progression_arr,
    get_random_number,
)


def get_game_data():
    min_progression_length = 5
    max_progression_length = 10
    progression_length = get_random_number(
        min_progression_length,
        max_progression_length
    )
    
    min_start = 0
    max_start = 20
    progression_start = get_random_number(min_start, max_start)
    
    min_step = 2
    max_step = 9
    progression_step = get_random_number(min_step, max_step)
    
    min_position = 0
    max_position = progression_length - 1
    hidden_position = get_random_number(min_position, max_position)
    
    progression_arr = get_progression_arr(
        progression_start,
        progression_length,
        progression_step,
        hidden_position
    )

    question = ' '.join(progression_arr)
    correct_answer = progression_start + hidden_position * progression_step
   
    return {
        question: question,
        correct_answer: correct_answer
    }


def start_game():
    task = 'What number is missing in the progression?'
    game(get_game_data, task)