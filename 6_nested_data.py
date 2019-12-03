# Nested data in list and dictionary

mix_list = ['string', 20, ['more strings', [1,2,'important']]]
print(mix_list)

internal_list = mix_list[2]
print(internal_list)

print(mix_list[2] [1] [2])
print(internal_list [1] [2])

internal_internal_list = internal_list[1]
print(internal_internal_list [2])

embeded_dict = {
    'status' : 'operational',
    'key1': ['car keys', 'boat keys', 'mansion keys', 'dog house keys'],
    'staff': {
        'Julio Cesar': {
            'name': 'Julio',
            'last_name': 'Cesar',
            'birth_date': 1979,
            'football_club': 'Flamengo'
        },
        'Julia Venus': {
            'name': 'Julia',
            'last_name': 'Venus',
            'birth_date': 1969,
            'football_club': 'CubaFC'
        }
              }
}
# Print boat keys and dog house keys
print(embeded_dict['key1'][3])
print(embeded_dict['key1'][1])

# Julio entire dictionary inside the key staff
print(embeded_dict['staff']['Julio Cesar'])

# Julia dictionary inside the key staff, print only the name and date of birth
print(embeded_dict['staff']['Julia Venus']['name'])
print(embeded_dict['staff']['Julia Venus']['birth_date'])