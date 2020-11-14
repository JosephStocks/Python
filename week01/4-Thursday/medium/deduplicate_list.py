#Algo 1
list1 = ["a", "b", "c", "d", "e", "b"]
list1.sort()

deduplicated_list = []
old_element = None
for element in list1:
    if element != old_element:
        deduplicated_list.append(element)
    old_element = element

print(deduplicated_list)




















####### ALGO 2
list1 = ["a", "b", "c", "d", "e", "b"]
deduplicated_list = []
for element in list1:
    if element not in deduplicated_list:
        deduplicated_list.append(element)

# Result
print(deduplicated_list)














# # OR
# # Algo 2
# list1 = ["a", "b", "c", "d", "e", "b"]
# deduplicated_list = list(set(list1))

# # Result
# print(deduplicated_list)