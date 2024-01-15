print("Weeks letf to X years\n")
age = int(input("How old are you?\n"))
age1 = int(input("Choose the age you want:\n"))
UmAno = float(52.1786)

age2 = age1 - age
age3 = age2 * UmAno

Resultado = age3

print(f"You have {round(Resultado,1)} weeks left to {age1} years")

enter = input("\nPress Enter to close")