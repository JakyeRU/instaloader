from yachalk import chalk
from art import *


def boot():
    # Cleaning the console
    print('\033c', end='')
    # Printing the boot logo
    print(f'{chalk.green_bright(text2art("InstaLoader"))}', '{:>75}'.format(chalk.white('Version 1.0.0 - Created by Jakye')), end='\n'*3)


def error(message, shouldExit=False):
    print(chalk.red_bright(f'[ERROR] {message}'))
    if shouldExit: exit(1)


def success(message):
    print(chalk.green_bright(f'[SUCCESS] {message}'))


def info(message, prefix=True):
    print(chalk.yellow_bright(f'{"[INFO]" if prefix else ""} {message}'))