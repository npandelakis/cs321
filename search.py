import puzzle8

GOAL = [1,2,3,8,0,4,7,6,5]
HOMES = [4,0,1,2,5,8,7,6,3]

def numWrongTiles(state):
    if puzzle8.getTile(state, 4) == 0:
        num_wrong = 0
    else:
        #avoid double count for blank
        num_wrong = -1

    for i in range(9):
        if puzzle8.getTile(state, i) != GOAL[i]:
            num_wrong += 1

    return num_wrong


def manhattanDistance(state):

    #bfs searching for a square's home
    def getDistToHome(square, start):
        queue = [start, None]
        #prevent re-checking previously seen squares
        seen = set()
        seen.add(start)

        home = HOMES[square]
        level = 0

        while True:
            temp = queue.pop(0)
            if temp is None:
                level += 1
                queue.append(None)
            elif temp == home:
                return level
            else:
                for x in puzzle8.neighbors(temp):
                    if x not in seen:
                        seen.add(x)
                        queue.append(x)

    distance = 0

    for i in range(9):
        square = puzzle8.getTile(state,i)
        if square != 0:
            distance += getDistToHome(square, i)

    return distance


    return 0
