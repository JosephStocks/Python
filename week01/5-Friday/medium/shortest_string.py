input_string_list = ("Before you criticize someone, walk a mile in their "
                     "shoes. That way, when you do criticize them, you’re "
                     "a mile away and you have their shoes.").split()

def shortest_string(input_list):
    shortest_string = input_list[0]
    for string in input_list:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string



print(f"Input:\n{input_string_list}\n")
print(f"Shortest string: {shortest_string(input_string_list)}")
print(f"Min string: {min(input_string_list, key=len)}")