list1 = [2, 3, 4]
list2 = [2, 3, 6]

listResult = []
for x, y in zip(list1, list2):
    listResult.append(x * y)

# OR

listResult = []
for index in range(len(list1)):
    listResult.append(list1[index] * list2[index])

# OR

listResult = []
for index, _ in enumerate(list1):
    listResult.append(list1[index] * list2[index])

print(f"{list1} x {list2} = {listResult}")

