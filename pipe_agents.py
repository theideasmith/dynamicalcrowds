from utils import *
import time
import numpy as np
from matplotlib.pyplot import *
import cv2
import imageio
from scipy.misc import imresize
from imageload import load_image
import sys
def animate(log=False, draw=False):
    im = sys.argv[1] if len(sys.argv)>1 else './levels/test1.png'
    print im
    sample_image=load_image(im)
    board = np.array(sample_image).astype(np.int)
    print board
    board_h, board_w = board.shape
    #board = np.ones((board_h, board_w))*EMPTY
    print board_h, board_w
   # board[0,1:4] = GOAL
   # board[0,0] = WALL
   # board[0,-2:] = WALL
   # board[-10:-1,-3:] = AGENT
    agents = np.sum(board==AGENT)
    t = 0
    states = []
    exited_agents=0
    while exited_agents < agents:
      #board = add_agents(np.array(board))
      newboard = add_agents(np.array(board))
      for i in xrange(board_h):
        for j in xrange(board_w):
          #imageio.imwrite('./test2/{0}.jpeg'.format(t), drawable)
          if newboard[i,j] != AGENT:
            continue
          newpos = agentStep(board, (i,j))
          if newpos is None:
            continue
          x,y = newpos
          if newboard[x,y] == GOAL:
            if log: print 'Exited at {0}'.format((x,y))
            newboard[i,j] = EMPTY
            exited_agents+=1
          else :
            newboard[x,y] = AGENT
            newboard[i,j] = EMPTY
          board = newboard
          states.append(newboard)
          if log:
            print 'Posthoc'
            print 'Current %d' % np.sum(board==AGENT)
            print 'Exited %d' % exited_agents
            print 'Should be %d' % (np.sum(board==AGENT)+exited_agents)
          t+=1
      drawable = imresize(board, size=1000)                  
      cv2.imshow('Board', drawable)                          
      cv2.waitKey(1)    
      
    return states

animate(draw=True)
