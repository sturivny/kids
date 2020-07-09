import emoji
import os
import random

from playsound import playsound

from emojies import good
from emojies import bad


def cls():
    os.system('clear')

class Game:
    def __init__(self, min_x=0, min_y=0, max_x=12, max_y=12):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

        self.all_answers = {'good': '', 'bad': ''}

    @staticmethod
    def generate_number(min_n=0, max_n=11):
        return random.randint(min_n, max_n)

    def generate_task(self):
        sign = random.choice('+-')
        x = self.generate_number(min_n=self.min_x, max_n=self.max_x)
        y = self.generate_number(min_n=self.min_y, max_n=self.max_y)
        if sign == '-':
            while x < y:
                x = self.generate_number()
        return {'x': x, 'y': y, 'sign': sign}

    def give_task(self, equation):
        answer = input("\n {} {} {} = ".format(equation['x'], equation['sign'], equation['y']))
        return answer

    def check_answer(self, equation, answer):
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

    def pretty_print_results(self, result):
        bad_sounds = ['sounds/bad_1.wav', 'sounds/bad_2.wav', 'sounds/bad_3.wav', 'sounds/bad_4.wav']

        good_e = random.choice(good)
        bad_e = random.choice(bad)
        if result:
            self.all_answers['good'] += good_e + ' '
            print(emoji.emojize('\n  {}'.format(self.all_answers['good']), use_aliases=True))
            playsound('sounds/good_1.wav')
        else:
            self.all_answers['bad'] += bad_e + ' '
            print(emoji.emojize('\n  {}'.format(self.all_answers['bad']), use_aliases=True))
            playsound(random.choice(bad_sounds))

    def pretty_print_gathered_bages(self):
        print(emoji.emojize(':small_orange_diamond:'*30, use_aliases=True))
        print(emoji.emojize('\n :white_check_mark: ===> {}'.format(self.all_answers['good']), use_aliases=True))
        print(emoji.emojize('\n :red_circle: ===> {}'.format(self.all_answers['bad']), use_aliases=True))
        print('\n\n\n\n\n')

    def play_all(self):
        equation = self.generate_task()
        answer = self.give_task(equation)
        result = self.check_answer(equation, answer)
        self.pretty_print_results(result)

        while not result:
            answer = self.give_task(equation)
            result = self.check_answer(equation, answer)
            self.pretty_print_results(result)

    def play_loop(self, turnes):

        cls()
        for x in range(turnes):
            self.play_all()
        cls()
        self.pretty_print_gathered_bages()


def main():
    game = Game()
    game.play_loop(3)


if __name__ == '__main__':
    main()
