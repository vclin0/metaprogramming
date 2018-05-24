

from os import listdir
from os.path import isfile, join
files = [f for f in listdir('./') if isfile(join('./', f)) and 'prisoner.py' in f and '~' not in f]

print(files)

from importlib import import_module
from pprint import pprint

prisoners = []

for f in files:
    #module = __import__(join('./', f))
    module = __import__(f[:-3])
    #pprint(module.__dict__)
    for key, val in module.__dict__.items():
        if isinstance(val, type):
            prisoners.append(val)

print(prisoners)

from collections import defaultdict

scoreboard = defaultdict(int)

runs = 100

sentences = (5, 2, 0, 6)

score_map = {
    (True, True) : (sentences[0], sentences[0]),
    (False, False) : (sentences[1], sentences[1]),
    (True, False) : (sentences[2], sentences[3]),
    (False, True) : (sentences[3], sentences[2]),
}

#def score(i1, i2):
    


def play(p1, p2):
    i1, i2 = p1(*sentences), p2(*sentences)
    for _ in range(100):
        s1, s2 = score_map[(i1.decide(), i2.decide())]
        i1.sentence(s1)
        i2.sentence(s2)
        scoreboard[type(i1)] += s1
        scoreboard[type(i2)] += s2

play(prisoners[0], prisoners[1])
pprint(scoreboard)