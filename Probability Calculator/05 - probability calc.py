import random
import copy

class Hat:
  #Initiliazes hat objects, adding the correct colored balls to a list
  def __init__(self, **kwargs):
    self.contents = []
    for color, number in kwargs.items():
      for num in range(number): #Appends each color the specified number of times
        self.contents.append(color)
  #Draw a certain number of balls, and return list of removed balls
  def draw(self, drawNum):
    self.removed = []
    if not(drawNum > len(self.contents)):
      ballsDrawn = 0
      #Continue popping random balls from hat until specified number are drawn
      while ballsDrawn < drawNum:
        remove = self.contents.pop(random.randint(0, len(self.contents) - 1))
        self.removed.append(remove) 
        ballsDrawn += 1
      return(self.removed) #List of balls drawn
    #If trying to draw more balls than available in hat
    else:
      return(self.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matches = 0 
  #Repeat num_experiments times
  for i in range(num_experiments):    
    #Create a copy of hat 
    hatCopy = copy.deepcopy(hat)
    drawn = hatCopy.draw(num_balls_drawn)
    #Turn list of balls drawn into a dictionary similar to hat {ballType:count}
    dictDrawn = {}
    for ball in drawn:
      dictDrawn[ball] = drawn.count(ball)
    for ball in expected_balls.keys():
      #If the ball is not in balls drawn, or there are not enough of them, break
      if (ball in dictDrawn.keys()) and (expected_balls[ball] <= dictDrawn[ball]):
        match = True 
      else: 
        match = False 
        break   
    if match == True:
      matches += 1
  prob = matches/num_experiments
  return(prob)