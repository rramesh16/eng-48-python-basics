# Continuation of for loops

dict_data = {
    1: {
        'name': 'Byron',
        'money': 0.50
        },
    2: {
        'name': 'Janet',
        'money': 2.00
        },
    3: {
        'name': 'Lizzy',
        'money': 1.20
    }


    }

# When you do a simple for loop on a dictionary you get the individual keys

for key in dict_data:
    print(key)
    print(dict_data[key])

for key in dict_data:
    print(key, '--->', dict_data[key])

# We want the name of the person and how much they owe us after applying the interest (4000%)

for key in dict_data:
    print(dict_data[key]['name'], 'owe us:', (dict_data[key]['money']*4000/12) + (dict_data[key]['money']))

for values in dict_data.values():
    print(values)

# iterating string
print('Hello!'[2])
