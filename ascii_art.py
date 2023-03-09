from pyfiglet import figlet_format as ascci_art
from termcolor import colored as colored


def pyfig():
    message = input('What message do you want to print? ')
    color = input('What color? ').lower()
    allowed_colors = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey',
                      'dark_grey', 'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan')
    if color not in allowed_colors:
        color = 'cyan'

    print(colored(ascci_art(message), color))


pyfig()
