def fileReader(inputFileNumber):
    with open(f'Input{inputFileNumber}.txt') as file:
        contents = file.readlines()
        num = int(contents[0].strip('\n'))
        items = list(map(lambda x: int(x), contents[1].strip().split(' ')))
        return (num, items)