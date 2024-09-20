# listas numericas

for value in range(1, 5):
    print(value)

# crear lista    
number = list(range(1, 5))
print(number)

# tercer paramertro, suma
even_numbers =list(range(0, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Max y min de una lista

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))

