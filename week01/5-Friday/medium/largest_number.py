input_list = [3, 2, 1, 5, 8, -30]

def largest(alist):
    # ALGO 1: NO BUILTIN FUNCTIONS
    largest = float('-inf')
    for number in input_list:
        if number > largest:
            largest = number
    return largest

print(f"Input list: {input_list}")
print(f"Smallest number: {largest(input_list)}")




##########################################################################
input_list = [3, 2, 1, 5, 8, -30]

# ALGO 1: USING BUILTIN FUNCTION
largest = max(input_list)

print(f"Input list: {input_list}")
print(f"Smallest number: {largest}")