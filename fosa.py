# Std lib
import itertools
import subprocess
import time

# Third party modules
import pyautogui


def create_perms(forgotten_phrase):
    perms = itertools.permutations(forgotten_phrase)
    return perms


def open_program(program):
    subprocess.Popen(program)


def click_coords(positions):
    for i, (c, x, y) in enumerate(positions, start=1):
        if i == 5:
            pyautogui.write('XXX')  # Email address goes here.
        pyautogui.click(clicks=c, x=x, y=y, interval=3)


def main():
    open_program("XXX")  # Path to password manager.
    time.sleep(10)
    click_coords([(2, 670, 1052), (1, 510, 400), (1, 972, 594),
                  (1, 953, 632), (1, 780, 446), (1, 822, 508)])

    with open('checked_phrases.txt', 'r+') as file:
        for phrase in create_perms('test'):
            file.seek(0)
            guesses = [line.strip() for line in file.readlines()]

            if phrase not in guesses:
                file.write(f'{phrase}\n')

            pyautogui.write(phrase)
            pyautogui.click(1098, 703, interval=0.6)
            pyautogui.click(879, 565)


if __name__ == '__main__':
    main()