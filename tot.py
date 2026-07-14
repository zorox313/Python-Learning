direction = input("Count 'up' or 'down'? ").strip().lower()
if direction == "up":
    top = int(input("Enter the top number: "))
    for i in range(1, top + 1):
        print(i)
elif direction == "down":
    bottom = int(input("Enter a number below 20: "))
    if bottom <= 20:
        for i in range(20, bottom - 1, -1):
            print(i)
    else:
        print("Number must be 20 or less.")
else:
    print("Please choose 'up' or 'down'.")