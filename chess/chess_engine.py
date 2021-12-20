## This is our main driver file - responsible for handling user input and displaying the current game state object.

class GameState():
  def __init__(self):
    # Board is and 8x8 2d list, each element of list has two characters
    # first character represetns colout, second character represents type of the piece
    self.board = [
                  ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                  ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                  ['--', '--', '--', '--', '--', '--', '--', '--'],
                  ['--', '--', '--', '--', '--', '--', '--', '--'],
                  ['--', '--', '--', '--', '--', '--', '--', '--'],
                  ['--', '--', '--', '--', '--', '--', '--', '--'],
                  ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                  ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
                ]

    self.whiteToMove = True
    self.moveLog = []
