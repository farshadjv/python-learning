attempt = 0
while (attempt < 3):
    attempt = attempt + 1
    password = input("Enter a password: ")
    if password == "python123":
        print("Access granted!")
        break
    elif attempt < 3:
        print("Access denied! Try again.")
    else:
        print("too many attempts! Access denied.")
