input_string = input("sample word? ").strip()
newstring_list = []
vowels = ['a', 'e', 'i', 'o', 'u']
last_char = None
for char in input_string:
    if char.lower() in vowels and last_char == char.lower():
        char *= 4
    newstring_list.append(char)
    last_char = char.lower()

newString = "".join(newstring_list)
print(newString)