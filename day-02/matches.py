Name = input("Enter character name: ")
match Name:
    case "Harry" | "Hermione" | "Ron":
        print("You are a Gryffindor!")
    case "Draco" | "Pansy":
        print("You are a Slytherin!")
    case _:
        print("You are in the wrong house!")
