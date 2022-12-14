# Minh Nguyen
# Homework 1

from collections import deque
from typing import Deque, List, Set

# find words that are one letter off
def findWords(word: str, Dict: Set):
    result: List[str] = []
    tempWord = list(word)

    for i in range(len(tempWord)):
        s = tempWord[i]
        letter = 'a'
        while letter <= 'z':
            tempWord[i] = letter
            if ''.join(tempWord) in Dict:
                result.append(''.join(tempWord))
            letter = chr(ord(letter) + 1)
        tempWord[i] = s
    return result

# function to find shortest ladder
def findLadders(Dictionary: List[str], beginning: str, ending: str):
    # stores shortest path
    result: List[List[str]] = []
    # store visited words
    visited = set()
    # queue to find shortest path
    queue: Deque[List[str]] = deque()
    #stores words from list
    Dict = set()
    for i in Dictionary:
        Dict.add(i)
    queue.append([beginning])

    tf = False
    while queue:
        size = len(queue)
        for i in range(size):
            current = queue[0]
            queue.popleft()
            add = []
            add = findWords(current[-1], Dict)
            for j in range(len(add)):
                tempLine = current.copy()
                tempLine.append(add[j])
                if(add[j] == ending):
                    tf = True
                    result.append(tempLine)
                visited.add(add[j])
                queue.append(tempLine)

        if(tf):
            break

        for erase in visited:
            Dict.remove(erase)
        visited.clear()
    return result

# function to print the shortest ladder to the screen
def printLadder(result: List[List[str]]):
    count = 0
    for i in result:
        for j in result:
            for k in j:
                if count == len(j) - 1:
                    print(k)
                else:
                    print(k,end=' -> ')
                    count = count + 1
            break
        break

# main sort of
l = []
f1 = open('words.txt','r')
data = f1.readlines()
for line in data:
    word = line.split()
    for w in word:
        if len(w)<=7:
            l.append(w)
f1.close()

empty = []

f2 = open('pairs.txt','r')
a = f2.readlines()
for b in a:
    print('\n')
    test = b.split()
    print('** Looking for ladder from',test[0],'to',test[1])
    if(len(test[0])==len(test[1])):
        if findLadders(l, test[0], test[1]) != '':
            if findLadders(l, test[0], test[1]) == empty:
                print('no ladder exists from',test[0],'to',test[1])
            else:
                result = findLadders(l, test[0], test[1])
                print('The ladder is: ',end='')
                printLadder(result)
        else:
            print('no ladder exists from',test[0],'to',test[1])
    else:
        print('beginning and end are not the same length')
f2.close()
