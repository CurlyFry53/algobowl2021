from FileReader import fileReader
import copy
from math import ceil, floor
from scipy.optimize import dual_annealing, differential_evolution

def heuristic(divisions, items: list):
    items = copy.deepcopy(items)
    pool = [1] # A calculated number pool which includes our starting items
    additions = []

    # Find the largest applicable number in the pool.
    def checkPool(num):
        largest = 0
        for item in pool:
            if (item >= ceil(num / (divisions[0])) and item <= num):
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
            biggerHalf = ceil(currentItem / (divisions[1])) # Split the value of the current item in half (getting smaller half).
            currentItem -= biggerHalf 
            additions.append((currentItem, biggerHalf))
            if (currentItem != biggerHalf): # If there are two distinct halves,
                items.append(currentItem) # Add the smaller half to the computation pile first.
            items.append(biggerHalf) # Finally add the currentitem to the computation pile.
        pool.append(item) # Now that we have effectively computed this number, add it to the pool.

    additions.sort(key=(lambda x: x[1]))
    # return(additions, pool, len(additions))
    print(len(additions))
    print(divisions)
    return len(additions)

# result = dual_annealing(heuristic, [(1.1, 10), (1.1, 10)], args=(copy.deepcopy(input[1]),), maxiter=10)
# result = differential_evolution(heuristic, [(1.1, 10), (1.1, 10)], args=(copy.deepcopy(input[1]),), maxiter=100)
# for i in range(11, 300):
#     for j in range(11, 300):
#         heuristic([i/10.0, j/10.0], copy.deepcopy(input[1]))
final = []
for i in range(1, 13):
    input = fileReader(i)
    result = differential_evolution(heuristic, [(2, 15), (2, 15)], args=(copy.deepcopy(input[1]),), maxiter=100)
    print(result)
    final.append(result)
file = open("ressim2.txt", "w")
file.write(str(final))
print(final)