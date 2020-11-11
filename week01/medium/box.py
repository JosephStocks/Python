width = int(input("Width? "))
height = int(input("Height? "))


for row in range(height):
    if row == 0 or row == height - 1:
        for _ in range(width):
            print("*", end="")
        print()

    else:
        for column in range(width):
            if column == 0 or column == width - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()