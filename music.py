from PyLyrics import *
import matplotlib.pyplot as plt


def tupleIt(list1,list2):
    list3 = []
    try:
        for i in range(list1):
            list3.append([list1,list2])


    except len(list1) == len(list2):
        print('Error, the 2 lists does not have the same size')


song, singer = input("Input the name of the song and the name of the singer, separated by a '-': ").split('-')
lyrics = PyLyrics.getLyrics(song,singer)
phrases = lyrics.split('\n')#Remove new lines
phrases = ' '.join(phrases)
words = phrases.split(' ')

translation_table = dict.fromkeys(map(ord, '!?,'), None)#Remove '?',',' and '!' from each word
phrases = phrases.translate({ord(c): None for c in '!?,'})
for word in words:
    if word == ' ' or word == '':
        words.remove(word)

length = len(words)
x = []
y = []
for i in range(length):
    for j in range(length):
        if words[i] == words[j]:
            x.append(j)
            y.append(i)

fig, ax = plt.subplots()
ax.scatter(x,y,s = 1)
plt.show()