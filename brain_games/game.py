from brain_games.utils.brain_utils import (
    show_task,
    user_input,
    welcome_user,
)


def game(get_game_data, task):

    welcome_user()

    user_name = user_input('May I have your name? ')
    print(f'Hello, {user_name}!')
    
    show_task(task)

    number_of_rounds = 3
    for _ in range(0, number_of_rounds):

        question, correct_answer = get_game_data()
        print(f'Question: {question}')

        user_answer = user_input('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(
                f'"{user_answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')