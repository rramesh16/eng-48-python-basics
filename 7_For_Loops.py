# For Loops!
# For loops will iterate over an iterable and run a block of code

# Syntax
# for <placeholder> in <iterable>:
    # doing stuff in this block
    # more things in a block

# Note: the block of code exist after the : (colon)
# It is the lines of code that ARE INDENTED
# It stops when the indentation stops

# Iterables are: list, ranges and dictionaries... and also strings

wish_list = ['rc car', 'cheese', 'cheerleaders', 'White shirts', 'sugar laces', 'reeses pieces', 'pasteis de nata']

import time
import random

counter = 1
for item in wish_list:
    print(counter, '-', item)
    counter += 1
    print('thinking...')
    # time.sleep(1.2)
    # print(random.randint(200, 210))

list_data =[[2, 4, 6, 8], [10, 12, 14, 16]]

for data in list_data:
    print(data)
    for num in data:
        print(num)

list_data2 =[['rc car', 'cheerleaders', 'white shirts', 'audi r8'], ['sugar laces', 'cheese', 'pasteis de nata', 'baklava']]

counter = 1
for data in list_data2:
    print(counter, '-', data)
    for num in data:
        print(counter, '-', num)
        counter += 1

print('1 -', 'rc car')
print('2 -', 'cheerleaders')