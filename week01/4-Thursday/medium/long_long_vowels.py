input_string = input("sample word? ").strip()
newstring = ""
vowels = ['a', 'e', 'i', 'o', 'u']

last_char = None
for char in input_string:
    if char.lower() in vowels and last_char == char.lower():
        char *= 4
    newstring += char
    last_char = char.lower()

print(newstring)