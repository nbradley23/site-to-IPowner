import requests
from random import randint
from pyfiglet import figlet_format as figform
from termcolor import colored


def dadjokes():
    print(colored(figform('Dad Joke 3000'), 'magenta'))
    url = 'https://icanhazdadjoke.com/search'
    joke_topic = input('Let me tell you a joke! Give me a topic: ').lower()
    joke_response = requests.get(url,
                                 headers={'Accept': 'application/json'},
                                 params={'term': joke_topic})
    data = joke_response.json()['results']

    num_jokes = len(data)

    if num_jokes > 1:
        return f"I've got {num_jokes} jokes about {joke_topic}. Here's one: \n{data[randint(0,num_jokes - 1)]['joke']}"
    elif num_jokes == 1:
        return f"I've got {num_jokes} jokes about {joke_topic}. Here's it is: \n{data[0]['joke']}"
    return f"Sorry I don't have any jokes about {joke_topic}! Please try again."


print(dadjokes())
