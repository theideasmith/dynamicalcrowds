from utils import *
import time
import numpy as np

from matplotlib.pyplot import *
import cv2
import imageio
from scipy.misc import imresize
from imageload import sample_image
def animate():
    f = figure()
    ax = f.add_subplot(111)      
    board = np.array(sample_image).astype(np.int)
    board_h, board_w = board.shape
    #board = np.ones((board_h, board_w))*EMPTY

   # board[0,1:4] = GOAL
   # board[0,0] = WALL
   # board[0,-2:] = WALL
   # board[-10:-1,-3:] = AGENT
    agents = np.sum(board==AGENT)
    t = 0
    states = []
    exited_agents=0
    while exited_agents < agents:
      print np.sum(board==AGENT)
      #board = add_agents(np.array(board))
      newboard = add_agents(np.array(board))
      for i in xrange(board_h):
        for j in xrange(board_w):
          if board[i,j] != AGENT:
            continue
          newpos = agentStep(board, (i,j))
          if newpos is None:
            continue
          x,y = newpos
          if board[x,y] == GOAL:
            newboard[i,j] = EMPTY
            exited_agents+=1
          else :
            newboard[x,y] = AGENT
            newboard[i,j] = EMPTY
          states.append( newboard )

      drawable = imresize(newboard, size=1000)
      drawable = np.flipud(drawable)
      cv2.imshow('Board', drawable)
      cv2.waitKey(1)
          #imageio.imwrite('./test2/{0}.jpeg'.format(t), drawable)
        
      board = newboard

animate()
