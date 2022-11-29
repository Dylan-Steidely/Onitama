


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]




List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
swapPositions(List, pos1-1, pos2-1)
print(List)
