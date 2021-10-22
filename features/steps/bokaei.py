from behave import *
from tictactoe import EMPTY_BOARD, play, play_best_move


# first move scenario
@given('we have an empty tic-tac-toe board')
def step_impl(context):    
    context.board = EMPTY_BOARD # clear the 3 x 3 tictactoe board
    context.winner = None # set the winner to Noneassert board == EMPTY_BOARD

# test for all given pieces on all given positions
@when('I play {piece} on column {col} and row {row} on the board')
def step_impl(context,piece,col,row):

    col = int(col)-1
    row = int(row)-1
    context.board, context.winner = play(context.board, piece,col,row)
    
    position_piece_on_board = row * 3 + col
    assert context.board[position_piece_on_board] == piece
    
@when('I ask the computer to do its best move for {piece}')
def step_impl(context,piece):
    context.board, context.winner = play_best_move(context.board, piece) # play the best move


@then('the board has a {piece} in column {col} and row {row} on the board')
def step_impl(context,piece,col,row):
    col = int(col)-1
    row = int(row)-1
    position_piece_on_board = row * 3 + col
    assert context.board[position_piece_on_board] == piece
    
# computer wins scenario

@then('{subject} is the winner of the game')
def step_impl(context,subject):
    if subject == 'X':
        assert context.winner == 'X'
    elif subject == 'O':
        assert context.winner == 'O'
    elif subject == 'Noone': # tied game
        assert context.winner == 'T'
    else:
        raise NotImplementedError(u'STEP: the game did not appoint a winner or tie when it should have')



# @then('it\'s a tied game')
# def step_impl(context):
    
#     assert context.winner == 'T'