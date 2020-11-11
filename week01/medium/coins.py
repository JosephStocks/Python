done = False
num_coins = 0
while not done:
    print(f"You have {num_coins} coins.")
    response = input("Do you want another? ").strip().lower()[0]
    if response == 'n':
        done = True
    else:
        num_coins += 1

print("Bye")