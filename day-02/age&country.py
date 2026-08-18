age = int(input("Enter your age: "))
country = input("Enter your country: ")
if age < 18:
    print("You are too young")
elif age >= 18 and country == "Germany":
    print("You can apply in Germany")
elif age >= 18 and country == "Oman":
    print("You can apply in Oman")
else:
    print("Country is not supported")
