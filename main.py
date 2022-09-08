# Import Module
import DOGE
from time import sleep
from os import system
from platform import uname

# Intro
print('[̲̅D][̲̅o][̲̅g][̲̅e] [̲̅t][̲̅o] [̲̅t][̲̅h][̲̅e] [̲̅m][̲̅o][̲̅o][̲̅n][̲̅!]')
sleep(3)
if uname().system == 'Windows':
 system('cls')
else:
  system('clear')

# Setting
where = input('DOGE to the where? : ')

# To the ~
print('-----------------------------------')
DOGE.to(where)

# To the (not setting)
print('-----------------------------------')
print('And DOGE to the ')
DOGE.planet.moon()
print('and')
DOGE.planet.mars()