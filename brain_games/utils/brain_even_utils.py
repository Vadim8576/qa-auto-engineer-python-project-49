from random import randint

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')


def user_input(text):
    return prompt.string(text)


def show_rules(rules):
    print(rules)


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


def get_result_expression(operator, value1, value2):
    match operator:
        case '*':
            return value1 * value2
        case '-':
            return value1 - value2
        case '+':
            return value1 + value2
        case _:
            return 0