current_users = ["artumarin", "admin", "pepito", "lolo", "lala"]
new_users = ["lele", "lili", "admin", "lolo", "kbza"]

for new_user in new_users:
    if new_user in current_users:
        print(f"El nombre de usuario: {new_user} esta en uso, por favor ingrese otro")
    else:
        print(f"El nombre de usuario: {new_user} esta disponible")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")