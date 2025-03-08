# -*- coding: utf-8 -*-
"color fitness2.ipynb"

import random

bases = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N','P','Q','R','S','T','V','W','Y']
words = ['RED', 'GREEN', 'MAGENTA', 'CYAN', 'LIME', 'NAVY', 'TEAL', 'PINK', 'TAN', 'GRAY', 'MINT','LILAC']

print(words[2::3])

def calcFitness(string):
    fitness = 0
    for word in words:
        for i in range(len(string)):
            for k in range(min(len(word),len(string)-i)):
                if string[i+k] == word[k]:
                    fitness += (k+1)
                else:
                    break
            if k == len(word)-1:
                fitness += 10
    return fitness

print(calcFitness("GRED"))

def deletion(genome):
    start = random.randint(0,len(genome)-1) #4  , genome length = 10
    print("Start: ", start)
    # length = random.randint(1,len(genome)-start) #6
    length = 3
    new_genome = genome[:start] + genome[start+length:]
    return new_genome

def insertion(genome,source):
    start1 = random.randint(0,len(genome)-1) # where to insert into the genome
    start2 = random.randint(0,len(source)-1) # where to start inserting from
    length = random.randint(1,len(source)-start2) # length of section to be inserted
    new_genome = genome[:start1] + source[start2:start2+length] + genome[start1:]
    return new_genome

print(words)
word2 = deletion(words)
print(word2)