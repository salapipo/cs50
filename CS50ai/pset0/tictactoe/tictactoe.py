"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x=0
    count_o=0
    for row in board:
        for cell in row:
            if cell==X:
                count_x+=1
            elif cell==O:
                count_o+=1
    if count_o==0 and count_x==0:
        return  X
    elif count_x>count_o:
        return  O
    else:
        return  X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action=set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell==EMPTY:
                action.add((i,j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not 0<=action[0]<=2 or not 0<=action[1]<=2:
        raise Exception

    new_board=copy.deepcopy(board)
    if new_board[action[0]][action[1]]==EMPTY:
        new_board[action[0]][action[1]]=player(board)
    else:
        raise Exception
    return new_board




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    columns={}
    diagonal1=[]
    for i, row in enumerate(board):
        if row.count(X)==3:
            return X
        elif row.count(O)==3:
            return O
        for j, cell in enumerate(row):
            if j not in columns:
                columns[j] = []
            columns[j].append(cell)
            if i==j:
                diagonal1.append(cell)
    diagonal2=[board[0][2],board[1][1],board[2][0]]
    for col in columns:
        if columns[col].count(X)==3:
            return X
        elif columns[col].count(O)==3:
            return O
    diagonals=[diagonal1,diagonal2]
    for diag in diagonals:
        if diag.count(X)==3:
            return X
        elif diag.count(O)==3:
            return O



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    elif len(actions(board))==0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if win==X:
        return 1
    elif win==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        analysis={}
        turn=player(board)
        actions_list=actions(board)
        if len(actions_list)==9:
            return random.choice(tuple(actions_list))

        for action in actions_list:
            if turn==X:
                v=min_value(result(board, action))

                if v==1:
                    return action

                if v not in analysis:
                    analysis[v]=[]
                analysis[v].append(action)


            else:
                v=max_value(result(board, action))

                if v==-1:
                    return action

                if v not in analysis:
                    analysis[v]=[]
                analysis[v].append(action)


        return analysis.get(0)[0]




def max_value(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,max_value(result(board,action)))
    return v
