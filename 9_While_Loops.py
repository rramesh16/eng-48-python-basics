# While Loops

# Syntax
# While <condition>:
    # block of code
    # block of code
    # Condition
    # Break point

num = 0
while num < 10:
    print('still less than 10')
    num += 1

# Using as a substitute for the For Loops

wish_list = ['rc car', 'cheese', 'cheerleaders', 'White shirts', 'sugar laces', 'reeses pieces', 'pasteis de nata']

print(len(wish_list))
index_length = len(wish_list)-1
counter = 0

while counter <= index_length:
    print(wish_list[counter])
    counter +=1

