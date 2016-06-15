import numpy as np

board_h = 40
board_w = 5
EMPTY = 0
AGENT = 1
WALL  = 2
GOAL = 3

class CellularCrowd:
  def __init__(self, board):
    self.board = board
    self.t = 0
    self.history = []
    self.exited_agents = 0
    self.ttlagents = np.sum(board==AGENT)
  
  def run(self):
    while self.exited_agents < self.ttlagents:
      agents_added = add_agents(self.board)
      stepBoard(agents_added)
      # It's passed by reference so we can add it to history
      self.history.append(agents_added)
      self.posthoc()
      self.t+=1

  def posthoc(self):
    """
    After update to board do something: like draw, etc
    """
    raise NotImplementedError('Subclasses should override this')

def dist(a,b):
	delta = b-a
	return sqrt(sum(delta))

def add_agents(board):
  """
  Draw a number of agents from a
  poisson distribution between 0 and 4
  and add them to the top
  """
  return np.array(board)

def agentStep(board, pos):
  """
  This runs a super naive agent with absolutely no
  heuristics or variable abilities
  It just goes to the adjacent square closest to the
  goal. If it's reached the goal, it returns None
  """

  # Calculating the closest goal
  goals = np.argwhere(board == GOAL)
  goal_distances = np.sqrt(np.sum((goals-pos)**2, axis=1))
  goal = closest_goal = goals[np.argmin(goal_distances)]

  # Adjacent and current cell
  positions = [
      pos+np.array([0,vertical])+np.array([horizontal,0])
      for vertical in [-1,0,1]
      for horizontal in [-1,0,1]
      if (0<=pos[1]+vertical<board.shape[1])
        and (0<=pos[0]+horizontal<board.shape[0])
  ]
  # If no positions satisfy our criteria
  # then return

  # only consider desireable cells
  positions = filter(
        lambda xy: (board[xy[0],xy[1]] in [EMPTY, GOAL]),
        positions
  )
  print len(positions)
  if len(positions) ==0: return None
  # print '-----'
  # print positions
  # print board
  # print goal

  # # Distance from these cells
  # # to the goal

  distances = map(
    lambda xy: np.sqrt(np.sum(np.subtract(xy,goal)**2)),
    positions)
  minimum = np.argmin(distances)
  destination = positions[minimum]

  if board[destination] == goal:
      return None
  return destination

def stepBoard(board):                           
  board_h, board_w = board.shape
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
  return board
def wrap(start,n,end):
    s = min([start, end])
    e = max([start, end])

    if s <= n <= e:
        return n
    elif n > e:
        return e
    elif n < s:
        return s
