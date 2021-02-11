from FileReader import fileReader
import copy
from math import ceil, e, floor, pi


# 3226 with /2
# 3224 with /4+
# Always from pool: 3228
# 3227 with /PI
# 3226 with /e

def heuristic(items: list):
    items = copy.deepcopy(items)
    # items.reverse() # First reverse the given items
    pool = [1] # A calculated number pool which includes our starting items
    additions = []

    # Find the largest applicable number in the pool.
    def checkPool(num):
        largest = 0
        for item in pool:
            if (item >= ceil(num / 2) and item <= num):
                if (item > largest):
                    largest = item
        return largest
    
    for index, item in enumerate(items):
        currentItem = item
        # print(f'Computation Item: {currentItem}')
        # print(f'Current Pool: {pool}')
        # print(f'Remaining Computations: {items[index + 1:]}')

        poolItem = checkPool(currentItem) # Grab an applicable item from the pool.
        if (currentItem == poolItem): # In the case that we have already calculated our pool item, break.
            pass
        elif (poolItem is not 0): # If the pool returned an item:
            currentItem -= poolItem # Subtract by the amount of that pool item.
            additions.append((currentItem, poolItem)) # Add to our total additions.
            items.append(currentItem) # This is a number we still need to solve, so through it on.
        else: # If the pool didn't return an item.
            biggerHalf = ceil(currentItem / 2) # Split the value of the current item in half (getting smaller half).
            currentItem -= biggerHalf 
            additions.append((currentItem, biggerHalf))
            if (currentItem != biggerHalf): # If there are two distinct halves,
                items.append(currentItem) # Add the smaller half to the computation pile first.
            items.append(biggerHalf) # Finally add the currentitem to the computation pile.
        pool.append(item) # Now that we have effectively computed this number, add it to the pool.

    additions.sort(key=(lambda x: x[1]))
    return(additions, pool, len(additions))

final = []
for i in range(1, 13):
    input = fileReader(i)
    result = heuristic(input[1])
    print(result)
    final.append(result[2])
file = open("ressim3.txt", "w")
file.write(str(final))
print(final)