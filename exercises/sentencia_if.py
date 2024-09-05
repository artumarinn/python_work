color_alien = "red"

if color_alien == "green":
    print("Great!, you win 5 points")
elif color_alien == "yellow":
    print("Great!, you win 10 points")
else:
    print("Great!, you win 15 points")

edad = 55

if edad < 2:
    print("Its a baby")
elif edad >= 2  and edad <= 4:
    print("Its a little boy")
elif edad >= 4 and edad < 13:
    print("Its a child")
elif edad > 13 and edad < 20:
    print("Its a teenager")
elif edad >= 20 and edad < 65:
    print("Its a adult")
else:
    print("He is over 65")
