import random

print('...rock...')
print('...paper...')
print('...scissors...')

player1 = input('(enter Player 1\'s choice): ').lower()
player2 = None
rndnum = random.randint(0, 2)

if rndnum == 0:
    player2 = 'rock'
elif rndnum == 1:
    player2 = 'paper'
else:
    player2 = 'scissors'

print(f'The computer chose: {player2}')
print('SHOOT!')

if player1 == player2:
    print('It\'s a draw')
elif player1 == 'rock':
    if player2 == 'paper':
        print('player2 wins!')
    else:
        print('player1 wins')
elif player1 == 'paper':
    if player2 == 'scissors':
        print('player2 wins!')
    else:
        print('player1 wins')
elif player1 == 'scissors':
    if player2 == 'rock':
        print('player2 wins!')
    else:
        print('player 1 wins')
else:
    print('Something went wrong.')
