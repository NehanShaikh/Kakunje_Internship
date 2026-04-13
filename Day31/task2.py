# RGB values stored in tuples
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while True:
    print("\nMenu")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("RGB Code for Red:", red)
    elif choice == 2:
        print("RGB Code for Green:", green)
    elif choice == 3:
        print("RGB Code for Blue:", blue)
    elif choice == 4:
        print("Program terminated.")
        break
    else:
        print("Invalid Choice")
