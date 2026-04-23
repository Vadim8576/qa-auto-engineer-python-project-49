from random import randint

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')


def user_input(text):
    return prompt.string(text)


def show_task(task):
    print(task)


def is_even(n):
    return n % 2 == 0


def get_random_number(min_number, max_number):
    return randint(min_number, max_number)


def get_operator():
    operators = ['*', '-', '+']
    min_number = 0
    max_number = len(operators) - 1
    index = get_random_number(min_number, max_number)
    return operators[index]


def get_result_expression(operator, a, b):
    match operator:
        case '*':
            return a * b
        case '-':
            return a - b
        case '+':
            return a + b
        case _:
            return 0


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a