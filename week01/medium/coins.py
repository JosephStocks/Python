done = False
num_coins = 0
while not done:
    print(f"You have {num_coins} coins.")
    response = input("Do you want another? ")
    if response == 'yes':
        # num_coins = num_coins + 1
        num_coins += 1
    else:
        done = True

print("Bye")