## This class is responsible for storeing all the infomation about the current sstate of the chess game - also repsobisble for determinign he valid moves at the current state. It will also keep a move log.
import pygame as py
from chess.chess_engine import GameState

WITDH = HEIGHT = 512
DIMENSION = 8 
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations later on
IMAGES = {}

'''
Iinitalize a global dictionary of images. This will be called once to save time
'''

def loadImages():
  pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bN', 'bB', 'bK', 'bQ', 'bR']
  for piece in pieces:
    IMAGES[piece] = py.transform.scale(py.image.load('chess/assets/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))

'''
This will be main driver, handle user input and update graphics
'''

def main():
  py.init()
  screen = py.display.set_mode((WITDH, HEIGHT))
  clock = py.time.Clock()
  screen.fill(py.Color('white'))
  gs = GameState()
  loadImages() # only once, before the while loop
  running = True
  while running:
    for ev in py.event.get():
      if ev.type == py.QUIT:
        running = False
    
    drawGameState(screen, gs)
    clock.tick(MAX_FPS)
    py.display.flip()

'''
Responisble for all the grapgics within the current gamestate.
'''

def drawGameState(screen, gs):
  drawBoard(screen) #draw squares on board
  drawPieces(screen, gs.board) # draw pieces on top of the square

def drawBoard(screen):
  colours = [py.Color('white'), py.Color('gray')]
  for r in range(DIMENSION):
    for c in range(DIMENSION):
      colour = colours[((r+c) % 2)] 
      py.draw.rect(screen, colour, py.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
  pass

if __name__ == '__main__':
  main()


