from utils import * 
import numpy as np
import imageio

rgb_to_board_map = {
    (0,0,255): AGENT,
    (255,0,0): GOAL,
    (0,0,0):   WALL,
    (255,255,255): EMPTY
}

def map_RGB(image, rgb_map=rgb_to_board_map):
  board = np.zeros((image.shape[0], image.shape[1]))
  for k,v in rgb_map.iteritems():
    pixels = image[:,:,:-1]
    mask = np.sum(pixels == np.array(k), axis=2)
    board[mask == 3] = v
  return board

def load_image(location, rgb_map = rgb_to_board_map):
  image = imageio.imread(location)
  board = map_RGB(image, rgb_map)
  return board



