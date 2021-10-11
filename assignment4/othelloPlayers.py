import othelloBoard
import math
from collections import namedtuple
from typing import Tuple, Optional

'''You should modify the chooseMove code for the ComputerPlayer
class. You should also modify the heuristic function, which should
return a number indicating the value of that board position (the
bigger the better). We will use your heuristic function when running
the tournament between players.

Feel free to add additional methods or functions.'''

class HumanPlayer:
    '''Interactive player: prompts the user to make a move.'''
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    def chooseMove(self,board):
        while True:
            try:
                move = eval('(' + input(self.name + \
                 ': enter row, column (or type "0,0" if no legal move): ') \
                 + ')')

                if len(move)==2 and type(move[0])==int and \
                   type(move[1])==int and (move[0] in range(1,9) and \
                   move[1] in range(1,9) or move==(0,0)):
                    break

                print('Illegal entry, try again.')
            except Exception:
                print('Illegal entry, try again.')

        if move==(0,0):
            return None
        else:
            return move

# https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
# We used the above paper as a reference for heuristics

def heuristic(board) -> int:
    # Linearly combine our two heuristic functions to get a total heuristic value
    return (mobilityScore(board) + cornersCaptured(board)) / 2


def cornersCaptured(board) -> int:
    # Return a score from -100 to 100 based on corners captured
    max_corners = 0
    min_corners = 0

    if board.array[1][1] != 0:
        if board.array[1][1] < 0:
            max_corners += 1
        else:
            min_corners += 1
    if board.array[1][8] != 0:
        if board.array[1][8] < 0:
            max_corners += 1
        else:
            min_corners += 1
    if board.array[8][1] != 0:
        if board.array[8][1] < 0:
            max_corners += 1
        else:
            min_corners += 1
    if board.array[8][8] != 0:
        if board.array[8][8] < 0:
            max_corners += 1
        else:
            min_corners += 1

    if (max_corners + min_corners) != 0:
        return 100*(max_corners - min_corners)/(max_corners + min_corners)
    else:
        return 0
    

def mobilityScore(board) -> int:
    # Return a score of -100 to 100 bast on the relative amount of possible
    # moves for the max and min players
    # Slow for regular minimax on 5+ plies 

    max_score = len(legalMoves(board, othelloBoard.black))
    min_score = len(legalMoves(board, othelloBoard.white))

    if max_score + min_score != 0:
        return 100*(max_score - min_score)/(max_score + min_score)
    else:
        return 0


def legalMoves(board,color):
        moves = []
        for i in range(1,othelloBoard.size-1):
            for j in range(1,othelloBoard.size-1):
                bcopy = board.makeMove(i,j,color)
                if bcopy != None:
                    moves.append((i,j))
        return moves

class ComputerPlayer:
    '''Computer player: chooseMove is where the action is.'''
    def __init__(self,name,color,heuristic,plies) -> None:
        self.name = name
        self.color = color
        self.heuristic = heuristic
        self.plies = plies

    # chooseMove should return a tuple that looks like:
    # (row of move, column of move, number of times heuristic was called)
    # We will be using the third piece of information to assist with grading.
    def chooseMove(self,board) -> Optional[Tuple[int,int,int]]:
        '''This very silly player just returns the first legal move
        that it finds.'''
        numHeuristicCalls = 0

        def maxValue(board, plies) -> Tuple[int,Tuple[int,int]]:
            if plies == 0:
                #allow access to numHeuristic in parent function
                nonlocal numHeuristicCalls
                numHeuristicCalls += 1
                return (heuristic(board), None)
            else:
                moves = legalMoves(board, othelloBoard.black)
                if len(moves) == 0:
                    return (board.scores()[0], None)
                else:
                    best = -math.inf
                    best_move = None

                    for move in moves:
                        #tuple (best, move)
                        next_min = minValue(board.makeMove(move[0], move[1], othelloBoard.black), plies - 1)
                        if best < next_min[0]:
                            best = next_min[0]
                            best_move = move

                return (best, best_move)
                


        def minValue(board, plies) -> Tuple[int,Tuple[int,int]]:
            if plies == 0:
                nonlocal numHeuristicCalls
                numHeuristicCalls += 1
                return (heuristic(board), None)
            else:
                moves = legalMoves(board, othelloBoard.white)
                if len(moves) == 0:
                    return (board.scores()[1], None)
                else:
                    best = math.inf
                    best_move = None

                    for move in moves:
                        next_max = maxValue(board.makeMove(move[0], move[1], othelloBoard.white), plies - 1)
                        if best > next_max[0]:
                            best = next_max[0]
                            best_move = move

                return (best, best_move)

        if self.color == othelloBoard.white:
            best_move = minValue(board, self.plies)[1]
            if best_move:
                return (best_move[0], best_move[1], numHeuristicCalls)
            else:
                # None is considered a pass
                return None
        else:
            best_move = maxValue(board, self.plies)[1]
            if best_move:
                return (best_move[0], best_move[1], numHeuristicCalls)
            else:
                return None


class ComputerPlayerPruning:
    '''Computer player: chooseMove is where the action is.'''
    def __init__(self,name,color,heuristic,plies) -> None:
        self.name = name
        self.color = color
        self.heuristic = heuristic
        self.plies = plies

    # chooseMove should return a tuple that looks like:
    # (row of move, column of move, number of times heuristic was called)
    # We will be using the third piece of information to assist with grading.
    def chooseMove(self,board) -> Optional[Tuple[int,int,int]]:
        numHeuristicCalls = 0
        ReturnMove = namedtuple('ReturnMove', ['value', 'move'])

        def maxValue(board, plies, alpha, beta) -> Tuple[int,Tuple[int,int]]:
            if plies == 0:
                #allow access to numHeuristic in parent function
                nonlocal numHeuristicCalls
                numHeuristicCalls += 1
                return ReturnMove(heuristic(board), None)
            else:
                moves = legalMoves(board, othelloBoard.black)
                if len(moves) == 0:
                    #100 for max win, -100 for min win
                    max_score, min_score = board.scores()
                    if max_score > min_score:
                        return ReturnMove(100, None)
                    elif max_score < min_score:
                        return ReturnMove(-100, None)
                    else:
                        return ReturnMove(0,None)
                else:
                    best_value = -math.inf
                    best_move = None

                    for move in moves:
                        #tuple (best, move)
                        next_min = minValue(board.makeMove(move[0], move[1], othelloBoard.black), plies - 1, alpha, beta)
                        if best_value < next_min.value:
                            best_value = next_min.value
                            best_move = move
                            alpha = max(alpha, best_value)
                        if best_value >= beta:
                            return ReturnMove(best_value, best_move)
                            
                return ReturnMove(best_value, best_move)
                


        def minValue(board, plies, alpha, beta) -> Tuple[int,Tuple[int,int]]:
            if plies == 0:
                nonlocal numHeuristicCalls
                numHeuristicCalls += 1
                return ReturnMove(heuristic(board), None)
            else:
                moves = legalMoves(board, othelloBoard.white)
                if len(moves) == 0:
                    max_score, min_score = board.scores()
                    if max_score > min_score:
                        return ReturnMove(100, None)
                    elif max_score < min_score:
                        return ReturnMove(-100, None)
                    else:
                        return ReturnMove(0,None)
                else:
                    best_value = math.inf
                    best_move = None

                    for move in moves:
                        next_max = maxValue(board.makeMove(move[0], move[1], othelloBoard.white), plies - 1, alpha, beta)
                        if best_value > next_max.value:
                            best_value = next_max.value
                            best_move = move
                            beta = min(beta, best_value)
                        if best_value <= alpha:
                            return ReturnMove(best_value, best_move)

                return ReturnMove(best_value, best_move)

        if self.color == othelloBoard.white:
            best_move = minValue(board, self.plies, -math.inf, math.inf).move
            if best_move:
                return (best_move[0], best_move[1], numHeuristicCalls)
            else:
                # None is considered a pass
                return None
        else:
            best_move = maxValue(board, self.plies, -math.inf, math.inf).move
            if best_move:
                return (best_move[0], best_move[1], numHeuristicCalls)
            else:
                return None
