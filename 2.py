# Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once

import random
list1 = ['a', 'e', 'i', 'o', 'u']
random.shuffle(list1)
print(''.join(list1))
