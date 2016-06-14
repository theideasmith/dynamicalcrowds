from utils import *

import numpy as np


board = np.ones((board_w, board_h))*EMPTY

board[0,1:3] = GOAL
board[0,0] = WALL
board[0,3] = WALL
board[3,3] = AGENT
board[3,2] = AGENT
t = 0
ttl = 4
states = np.zeros((ttl, board_w, board_h))
print board
while t < ttl:
  board = add_agents(np.array(board))
  for i in xrange(board_w):
    for j in xrange(board_h):
      if board[i,j] != AGENT:
        continue
      newpos = agentStep(board, (i,j))
      if newpos is None:
        continue
      x,y = newpos
      if board[x,y] != GOAL:
          board[x,y] = AGENT

      board[i,j] = EMPTY
      print board
      states[t,:,:] = board
  t+=1
