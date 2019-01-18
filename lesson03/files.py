import os

# file_name = os.path.join('root', 'subdir', 'test.txt')  # root/subdir/test.txt

# read files

# file = open(os.path.join('data', 'input.txt'))
# content = file.readlines()
#
# print(content)
#
# file.close()

with open(os.path.join('data', 'input.txt')) as file:
    content = file.readlines()
    # print(content)

# write files
output = os.path.join('data', 'out.txt')
file_content = ['First', 'Second', 'Third']

with open(output, mode='w') as file:
    file.writelines([line + '\n' for line in file_content])

# JSON file
import json

output = os.path.join('data', 'out.json')

person = {'name': 'John', 'lastname': 'Doe', 'age': 30, 'likes': [1, 2, 3, 4]}

with open(output, mode='w') as json_file:
    json.dump(person, json_file)

with open(output, mode='r') as json_file:
    person_loaded = json.load(json_file)
    print(person_loaded)

# Python serialization (pickle)
import pickle

output = os.path.join('data', 'out.bin')

complex_item = [
    file_content,
    person,
    'Simple line',
    108
]

with open(output, mode='wb') as pickle_file:
    pickle.dump(complex_item, pickle_file)

# pickle.load()  # like JSON
