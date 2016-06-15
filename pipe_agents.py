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
    print board
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
      board = add_agents(np.array(board))
      for i in xrange(board_h):
        for j in xrange(board_w):
          if board[i,j] != AGENT:
            continue
          newpos = agentStep(board, (i,j))
          if newpos is None:
            continue
          x,y = newpos
          if board[x,y] != GOAL:
              board[x,y] = AGENT
          else:
              exited_agents+=1
          board[i,j] = EMPTY
          states.append( board )

        #   imageio.imwrite('./images/{0}.jpeg'.format(t), drawable)
        # ax.imshow(drawable)
        #ax.set_yticks([])
        #ax.set_xticks([])
        #f.savefig('./matimages/{0}.jpeg'.format(t))
        t+=1
      drawable = imresize(board, size=10000)
      cv2.imshow('Board', drawable)
      cv2.waitKey(100)
      

animate()
