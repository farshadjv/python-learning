name = input("What is your name? ")
name = name.capitalize()
age = int(input("What is your age? "))
country = input("Where are you living? ")
score = int(input("What is your score? "))
person = {
    "Name": name,
    "Age": age,
    "Country": country,
    "Score": score
}
if person["Score"] >= 90:
    print(f"Hello, {person['Name']}, you are {person['Age']} years old and you are living in {person['Country']}. Your score is {person['Score']}, which is excellent!")
elif person["Score"] >= 75:
    print(f"Hello, {person['Name']}, you are {person['Age']} years old and you are living in {person['Country']}. Your score is {person['Score']}, which is good!")
elif person["Score"] >= 50:
    print(f"Hello, {person['Name']}, you are {person['Age']} years old and you are living in {person['Country']}. Your score is {person['Score']}, which is pass!")
else:
    print(f"Hello, {person['Name']}, you are {person['Age']} years old and you are living in {person['Country']}. Your score is {person['Score']}, which is fail!")
