"""
Morse translator:
Enter a word and it will spell it in Morse code

International morse code:
1. lenth of a dot is one unit
2. a dash is three units
3. the space between parts of the same letter is one unit
4. the space between letters is three units
5. the spase between words is seven units

we assume that one unit is 0.1 seconds last
"""

import os
import time

morse_dict = {'a': [1, 3], 'b': [3, 1, 1, 1], 'c': [3, 1, 3, 1],
              'd': [3, 1, 1], 'e': [1], 'f': [1, 1, 3, 1], 'g': [3, 3, 1],
              'h': [1, 1, 1, 1], 'i': [1, 1], 'j': [1, 3, 3, 3],
              'k': [3, 1, 3], 'l': [1, 3, 1, 1], 'm': [3, 3], 'n': [3, 1],
              'o': [3, 3, 3], 'p': [1, 3, 3, 1], 'q': [3, 3, 1, 3],
              'r': [1, 3, 1], 's': [1, 1, 1], 't': [3], 'u': [1, 1, 3],
              'v': [1, 1, 1, 3], 'w': [1, 3, 3], 'x': [3, 1, 1, 3],
              'y': [3, 1, 3, 3], 'z': [3, 3, 1, 1], '1': [1, 3, 3, 3, 3],
              '2': [1, 1, 3, 3, 3], '3': [1, 1, 1, 3, 3], '4': [1, 1, 1, 1, 3],
              '5': [1, 1, 1, 1, 1], '6': [3, 1, 1, 1, 1], '7': [3, 3, 1, 1, 1],
              '8': [3, 3, 3, 1, 1], '9': [3, 3, 3, 3, 1], '0': [3, 3, 3, 3, 3],
              }

ONE_UNIT = 0.1


def beep(x):
    os.system('play --no-show-progress --null --channels 1 \
        synth %s sine %f' % (x, 1000))
    time.sleep(ONE_UNIT)


def morse_spell(word):
    word = word.lower()
    for w in word:
        if w == ' ':
            time.sleep(7 * ONE_UNIT)
        else:
            for x in morse_dict[w]:
                beep(x * ONE_UNIT)
            time.sleep(3 * ONE_UNIT)

morse_spell(raw_input("Enter your message: "))
