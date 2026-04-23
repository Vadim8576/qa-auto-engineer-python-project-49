from math import sqrt
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
    OPERATORS = ['*', '-', '+']
    MIN_NUMBER = 0
    MAX_NUMBER = len(OPERATORS) - 1
    index = get_random_number(MIN_NUMBER, MAX_NUMBER)
    return OPERATORS[index]


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


def get_progression_arr(start, length, step, hidden_position):
    progression = []
    for i in range(length + 1):
        currentElement = start + i * step if i != hidden_position else '..'
        progression.append(str(currentElement))
    return progression


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True