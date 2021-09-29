import puzzle8
import time

def dfs(state, depth):
    stack = []

    blank = puzzle8.blankSquare(state)

    return dfsHelper(state, depth, blank, stack)



def dfsHelper(state, depth, blank, stack):
    #Helper function that returns the stack at the time the solution is found
    if state == puzzle8.solution():
        print(stack)
        return stack
    else:
        poss_moves = puzzle8.neighbors(blank)

        if depth == 0:
            return
        else:
            for move in poss_moves:
                temp_state = puzzle8.moveBlank(state, move)
                stack.append(move)

                #receive stack or None passed up from dfsHelper
                temp_stack = dfsHelper(temp_state, depth - 1, move, stack)

                if temp_stack:
                    #We only receive a stack if the solution is found
                    return temp_stack
                else:
                    stack.pop(-1)



def itdeep(state):
    depth = 1

    startTime = time.time()
    while True:
        stack = dfs(state, depth)
        #timing measurements
        print(depth)
        print(time.time() - startTime)
        if stack:
            #Same logic where we only receive a stack if the solution is found
            return stack
        else:
            depth += 1
