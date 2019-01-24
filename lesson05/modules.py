import os
import sys


# os.chdir('src')
# current = os.getcwd()

def func1():
    print('func1')


def func2():
    print('func2')


my_dict = {
    'test': func1,
    'action': func2
}

key = sys.argv[1]

my_dict[key]()
