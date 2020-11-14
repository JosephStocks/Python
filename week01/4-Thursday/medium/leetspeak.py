input_string = "I am a leet programmer"

mapping = {'a': 4,
           'e': 3,
           'g': 6,
           'i': 1,
           'o': 0,
           's': 5,
           't': 7}
new_string = []
for character in input_string:
    if character in mapping:
        character = str(mapping[character])
    new_string.append(character)

new_string = "".join(new_string)
print(new_string)