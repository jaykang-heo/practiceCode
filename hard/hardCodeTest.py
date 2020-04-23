from . import hardCode as code
from shutil import copyfile
import unittest


import json
with open('keepTrack.json', 'r') as f:
    data = json.load(f)
    data['num'] += 1
    print('Congratulations! You Are Awesome!')
    print('Total Number For Hard Code', data['num'])
with open('keepTrack.json', 'w') as file:
    json.dump(data, file)
open('hardCode.py', 'w')
copyfile('hardCodeOriginal.py', 'hardCode.py')

