# height = int(input("Triangle height? "))
# subtract_amount = 0
# complete_string = ""
# for row in range(height):
#     for column in range(2 * height - 1):
#         if column >= subtract_amount and column <= 2 * height - 2 - subtract_amount:
#             print("*", end="")
#         else:
#             print("X", end="")
#     print()
#     subtract_amount += 1

height = int(input("Triangle height? "))
subtract_amount = 0
complete_string = ""
for row in range(height):
    temp_string = ""
    for column in range(2 * height - 1):
        if column >= subtract_amount and column <= 2 * height - 2 - subtract_amount:
            temp_string += "*"
        else:
            temp_string += " "
    temp_string += "\n"
    subtract_amount += 1
    complete_string = temp_string + complete_string

print(complete_string)
