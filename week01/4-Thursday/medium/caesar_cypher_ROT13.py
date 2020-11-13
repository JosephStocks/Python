alphabet = "abcdefghijklmnopqrstuvwxyz"
input_string = "lbh zhfg hayrnea jung lbh unir yrnearq"

output_string = ""
for char in input_string:
    if char != " ":
        index = alphabet.index(char)
        new_index = (index + 13) % 26
        new_char = alphabet[new_index]
    else:
        new_char = " "
    output_string += new_char

print(output_string)