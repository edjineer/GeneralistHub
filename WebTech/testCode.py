# Implement Sorting Algorithms

from copy import deepcopy


# Bubble Sort
# Swap adjacent elements if they are in the wrong order
def bubbleSort(input):
    finished = False
    workingList = deepcopy(input)
    while not finished:
        print(workingList)
        neededCorrection = False
        for idx, val in enumerate(workingList):
            if idx == (len(input) - 1):
                continue
            if val > workingList[(idx + 1)]:
                temp = workingList[idx]
                workingList[idx] = workingList[(idx + 1)]
                workingList[(idx + 1)] = temp
                neededCorrection = True
                print(workingList)
        if not neededCorrection:
            finished = True

    return


if __name__ == "__main__":
    inputArray = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 2, 4, -1], [], ["str"]]

    for input in inputArray:
        assert (
            bubbleSort(input) == input.sort()
        )  # TODO: Optimization to DP or cache sorted result here
