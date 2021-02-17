# algobowl2021

## Naming Scheme
Inputs - Should be of the form input*.txt where \* correspond to a unique number for batch testing.
Outputs - Should be of the form output*.txt whose number \* corresponds to a unique input.

## Consistency
Algorithms can be named anything, but when an algorithm is finished, run it on all of the inputs and generate a new folder in the output folder with the results consistant to that algorithm.

Additional, write a line to this readme with the following info:

Algorithm Name - Input #1 Total Additions, Input #2 Total Additions, Input #3 Total Additions, ..., Input #n Total Additions

Dr. Mehta says we do not need run times, but they might still be helpful to have? He said we have 25 hrs to run all inputs of the other 20+ groups. Not exactly sure what would be best.

## Ideas:
1. We might be able to use an exhaustive approach on small inputs and a non-exhaustive on large ones. I am assuming most groups will contribute relatively massive inputs to do some damage to competition. However, we could submit a relatively simple one with n=25 and run an exhaustive to assure our success for that input.
2. Just as a note, the largest 32-bit integer is less than 10^9, so if any groups program with ints they will hit an overflow.
3. Other weird math things this problem could be related to: the fibonacci sequence is an example of an input who's length n is nearly equal to the total number of additions (n + 1).
4. On a foundational level, this is what this problem seems very similar to: https://en.wikipedia.org/wiki/Partition_(number_theory)
5. It also seems rather similar to the minimum change problem in computer science.
6. Posted on Piazza and it looks like Dr. Mehta is recommending against a dynamic programming approach.

## Input Description
1. Size: 5, Max: 25
2. Size: 5, Max: 100
3. Size: 5, Max: 1000
4. Size: 25, Max: 1000
5. Size: 100, Max: 1000
6. Size: 100, Max: 10^9
7. Size: 250, Max: 10^9
8. Size: 500, Max: 10^9
9. Size: 750, Max: 10^9
10. Size: 1000, Max: 10^9
11. Size: 1000, Max: 10^9
12. Size: 1000, Max: 10^9

## Algorithms:
1. Heuristic #1 - 7, 13, 27, 48, 122, 576, 1099, 1872, 2563, 3226, 3226, 3221
2. Annealing Heuristic #1 - 8, 13, 23, 47, 122, 562, 1101, 1868, 2562, 3225, 3208, 3217
3. Random #1 - Not even comparable
