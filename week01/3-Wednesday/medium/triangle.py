# height = int(input("Triangle height? "))
# subtract_amount = 0
# complete_string = ""
# for row in range(height):
#     temp_string = ""
#     for column in range(2 * height - 1):
#         if column >= subtract_amount and column <= 2 * height - 2 - subtract_amount:
#             temp_string += "*"
#         else:
#             temp_string += " "
#     temp_string += "\n"
#     subtract_amount += 1
#     complete_string = temp_string + complete_string

# print(complete_string)
##############################################


# ANOTHER VERSION
height = int(input("Triangle height? "))
num_stars = 1
for num_blanks in range(5, 0, -1):
    print(" " * num_blanks + "*" * num_stars)
    num_stars += 2

# VERSION 3 (WITH WHILE LOOP)
# height = int(input("Triangle height? "))
# counter = 0
# num_stars = 1
# num_blanks = height
# while counter < height:
#     print(" " * num_blanks + "*" * num_stars)
#     num_stars += 2
#     num_blanks -= 1
#     counter += 1

