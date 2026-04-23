from brain_games.game import game
from brain_games.utils.brain_utils import (
    get_progression_arr,
    get_random_number,
)


def get_game_data():
    MIN_LENGTH = 5
    MAX_LENGTH = 10
    PROGRESSION_LENGTH = get_random_number(
        MIN_LENGTH,
        MAX_LENGTH
    )
    
    MIN_START = 0
    MAX_START = 20
    PROGRESSION_START = get_random_number(MIN_START, MAX_START)
    
    MIN_STEP = 2
    MAX_STEP = 9
    PROGRESSION_STEP = get_random_number(MIN_STEP, MAX_STEP)
    
    MIN_HIDDEN_POSITION = 0
    MAX_HIDDEN_POSITION = PROGRESSION_LENGTH - 1
    HIDDEN_POSITION = get_random_number(
        MIN_HIDDEN_POSITION,
        MAX_HIDDEN_POSITION
    )
    
    progression_arr = get_progression_arr(
        PROGRESSION_START,
        PROGRESSION_LENGTH,
        PROGRESSION_STEP,
        HIDDEN_POSITION
    )

    question = ' '.join(progression_arr)
    correct_answer = PROGRESSION_START + HIDDEN_POSITION * PROGRESSION_STEP
   
    return {
        'question': question,
        'correct_answer': correct_answer
    }


def start_game():
    TASK = 'What number is missing in the progression?'
    game(get_game_data, TASK)