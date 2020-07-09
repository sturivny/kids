import emoji
import os
import random

from playsound import playsound

from emojies import good
from emojies import bad


def cls():
    os.system('clear')


def generate_number(min_n=0, max_n=11):
    return random.randint(min_n, max_n)


def generate_task():
    sign = random.choice('+-')
    x = generate_number()
    y = generate_number()
    if sign == '-':
        while x < y:
            x = generate_number()
    return {'x': x, 'y': y, 'sign': sign}


def give_task(equation):
    answer = input("\n {} {} {} = ".format(equation['x'], equation['sign'], equation['y']))
    return answer


def check_answer(equation, answer):
    if equation['sign'] == '-':
        correct_answer = equation['x'] - equation['y']
    elif equation['sign'] == '+':
        correct_answer = equation['x'] + equation['y']
    else:
        print('Impossible!!!')
        correct_answer = None
    if correct_answer == int(answer):
        return True
    else:
        return False


def pretty_print_results(result):
    bad_sounds = ['sounds/bad_1.wav', 'sounds/bad_2.wav', 'sounds/bad_3.wav', 'sounds/bad_4.wav']

    good_e = random.choice(good)
    bad_e = random.choice(bad)
    if result:
        print(emoji.emojize('\n  {}'.format(good_e), use_aliases=True))
        playsound('sounds/good_1.wav')
        return good_e
    else:
        print(emoji.emojize('\n  {}'.format(bad_e), use_aliases=True))
        playsound(random.choice(bad_sounds))
        return bad_e


def play_all():

    equation = generate_task()
    answer = give_task(equation)
    result = check_answer(equation, answer)
    pretty_print_results(result)

    while not result:
        answer = give_task(equation)
        result = check_answer(equation, answer)
        pretty_print_results(result)


def main():
    cls()
    for x in range(20):
        play_all()


if __name__ == '__main__':
    main()
