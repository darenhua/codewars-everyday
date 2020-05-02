def checkdirections(dir1, dir2):
    directionlist = ["east", "south", "west", "north"]

    index1 = directionlist.index(dir1.lower())
    index2 = directionlist.index(dir2.lower())
    #if both indices are even (east and west) or odd(south and north), return true
    return (index1 - index2) % 2 == 0 and index1 != index2

def dirReduc(arr):
    reduced = arr
    index = len(arr) - 1 #start with last element
    while index >= 1:#as long as there are at least 2 elements on the list
        if checkdirections(arr[index], arr[index-1]): 
            reduced.pop(index)
            reduced.pop(index-1)
            index -= 2
            index = len(arr) - 1
        else:
            index -= 1
    return reduced
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

