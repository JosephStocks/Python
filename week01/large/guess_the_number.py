print("I am thinking of a number between 1 and 10.")
answer = 5
done = False
while True:
    guess = int(input("What's the number? "))
    if guess == answer:
        print("Yes! You win!")
        break
    elif guess > answer:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")