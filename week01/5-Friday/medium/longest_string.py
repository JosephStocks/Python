input_string_list = ("Before you criticize someone, walk a mile in their "
                     "shoes. That way, when you do criticize them, you’re "
                     "a mile away and you have their shoes.").split()

def longest_string(input_list):
    longest_string = input_list[0]
    for string in input_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

print(f"Input:\n{input_string_list}\n")
print(f"Longest string: {longest_string(input_string_list)}")