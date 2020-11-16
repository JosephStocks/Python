input_list = [3, 2, 1, 5, 8, -30]

def smallest(alist):
    # ALGO 1: NO BUILTIN FUNCTIONS
    smallest = float('inf')
    for number in input_list:
        if number < smallest:
            smallest = number
    return smallest

print(f"Input list: {input_list}")
print(f"Smallest number: {smallest(input_list)}")




##########################################################################
input_list = [3, 2, 1, 5, 8, -30]

# ALGO 1: USING BUILTIN FUNCTION
smallest = min(input_list)

print(f"Input list: {input_list}")
print(f"Smallest number: {smallest}")