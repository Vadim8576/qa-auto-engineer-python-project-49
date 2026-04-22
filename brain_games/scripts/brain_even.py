from brain_games.utils.brain_even_utils import (
    get_correct_answer,
    get_random_number,
    input_user_answer,
    input_user_name,
    show_rules,
    welcome_user,
)


def main():
    welcome_user()

    user_name = input_user_name('May I have your name? ')
    print(f'Hello, {user_name}!')
    
    show_rules()
    
    correct_answer_counter = 0

    while correct_answer_counter < 3:
        random_number = get_random_number()
        print(f'Question: {random_number}')
        user_answer = input_user_answer('Your answer: ')
        correct_answer = get_correct_answer(random_number)

        if user_answer == correct_answer:
            print('Correct!')
            correct_answer_counter += 1
        else:
            print(
                f'"{user_answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()