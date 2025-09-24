# Příklad jednoduché aplikace - Game Quiz
'''

'''
from playsound import playsound

game_sounds = ['clashroyale', 'minecraft', 'fortnite', 'apexlegends', 'brawlstars']
used_choices = []

def get_num():
    num = int(input('Choose a number from 1 to 5: '))
    while num not in range(1, len(game_sounds) + 1):
        print('Invalid number. Try again.')
        num = int(input('Choose a number from 1 to 5: ')) 
    return num

def check_num(num):
    for j in used_choices:
        if num == j:
            print('You already used this number. Try again.')
            return False
    return True

print('Welcome to my Game Quiz!')
print('Five numbers. Five sounds. Five Games. Can u guess them all?')
print('(clashroyale, minecraft, fortnite, apexlegends, brawlstars)')

for i in range(len(game_sounds)):
    num = get_num()
    while not check_num(num):
        num = get_num()
    used_choices.append(num)
    game_sound = '.\\sounds\\' + game_sounds[num - 1] + '.mp3'
    playsound(game_sound)
    answer = input('Which game is this? ')
    if answer.lower() == game_sounds[num - 1]:
        print('Correct!')
    else:
        print('Wrong! It was ' + game_sounds[num - 1] + '.')