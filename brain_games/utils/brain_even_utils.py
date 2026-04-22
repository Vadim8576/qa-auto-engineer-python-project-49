from random import randint

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')


def input_user_name(text):
    return prompt.string(text)


def input_user_answer(text):
    return prompt.string(text)


def show_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(n):
    return n % 2 == 0


def get_random_number():
    min_number = 1
    max_number = 100

    return randint(min_number, max_number)


def get_correct_answer(random_number):
    return 'yes' if is_even(random_number) else 'no'

