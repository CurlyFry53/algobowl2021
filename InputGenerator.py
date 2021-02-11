import random

# Note the minumum possible number will always be two.
def generateNumbers(num, max):
    with open("Input0012.txt", "w") as file:
        file.write(str(int(num)) + "\n")
        numbers = []
        for i in range(0, num):
            numbers.append(random.randint(2, max))
        numbers.sort()
        for n in numbers:
            file.write(f'{n} ')

generateNumbers(1000, 1000000000)