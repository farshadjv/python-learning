name = input("What is your name? ")
name = name.capitalize()
age = int(input("What is your age? "))
country = input("Where are you living? ")
job = input("what is your Job? ")
person = {
    "Name": name,
    "Age": age,
    "Country": country,
    "Job": job
}
for key, value in person.items():
    print(key, ":", value)
