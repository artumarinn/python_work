
numbers = [value for value in range(1, 21)]
print(numbers)

numbers02 = [value for value in range(1, 1000001)]
#print(numbers02)

numbers03 = [value + value for value in range(1, 1000001)]
#print(numbers03)

#print(max(numbers03))
#print(min(numbers03))

numbers04 = [value for value in range(1, 20, 2)]
print(numbers04)

numbers05 = []
for value in range(3, 30):
    if value % 3 == 0:
        numbers05.append(value)
print(numbers05)

numbers06 = [value ** 3 for value in range(1, 11)]
print(numbers06)