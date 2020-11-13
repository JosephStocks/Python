input_string = "I am a leet programmer"
char_list = list(input_string)
mapping = {'a': 4,
           'e': 3,
           'g': 6,
           'i': 1,
           'o': 0,
           's': 5,
           't': 7}
new_string = []
for character in char_list:
    if character in mapping:
        character = str(mapping[character])
    new_string.append(character)

new_string = "".join(new_string)
print(new_string)