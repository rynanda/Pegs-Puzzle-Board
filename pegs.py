import re

# You can define some helper functions here if you like!

# Function to check whether a given game board is solved, has a possible move to solve, or unsolvable.
def solvedBoard(gameBoard):
   if findPatternL(gameBoard) is not None:
      return('unsolved - move left')
   elif findPatternR(gameBoard) is not None:
      return('unsolved - move right')
   elif (findPatternL(gameBoard) is None) and (findPatternR(gameBoard) is None) and (gameBoard.count('X')) == 1:
      return('solved')
   elif (findPatternL(gameBoard) is None) and (findPatternR(gameBoard) is None) and (gameBoard.count('X') > 1):
      return('unsolvable')

# Function to check whether a left move is possible.
def findPatternL(V, pattern = 'oXX'):
   possibleLeft = []
   matches = re.finditer(pattern, V)
   for x in matches:
      return(x.end())

# Function to check whether a right move is possible.
def findPatternR(V, pattern = 'XXo'):
   matches = re.finditer(pattern, V)
   for x in matches:
      return(x.start())

# Function to create a tuple consisting of peg index and left move.
def pegIndexesL(V):
   if (findPatternL(V) - 1) is not None:
      tupleIndex = ((findPatternL(V) - 1), "L")
      return(tupleIndex)

# Function to create a tuple consisting of peg index and right move.
def pegIndexesR(V):
   if (findPatternR(V) + 1) is not None:
      tupleIndex = ((findPatternR(V)), "R")
      return(tupleIndex)

# Function to do a left move on a game board.
def moveLeft(V, pattern = 'oXX', replacement = 'Xoo'):
   result = re.sub(pattern, replacement, str(V), 1)
   V = result
   return(V)

# Function to do a right move on a game board.
def moveRight(V, pattern = 'XXo', replacement = 'ooX'):
   result = re.sub(pattern, replacement, str(V), 1)
   V = result
   return(V)

def pegsSolution(gameBoard):
   # Program your solution here
   pegMovelist = [] # Initialize a list for moves to solve a game board.
   initBoard = gameBoard # Initialize a string that takes a game board configuration. 
                           # Useful for backtracking without altering the given game board.

   if solvedBoard(gameBoard) == 'solved':
      pass # Do nothing if game board already solved.
   else:
      while solvedBoard(gameBoard) != 'solved':
         if gameBoard.count('X') >= 1: # Ensures at least one peg is in pegboard.
            if 'left' in solvedBoard(gameBoard):
               initBoard = moveLeft(gameBoard)
               if (solvedBoard(initBoard) == 'unsolvable') and (findPatternR(gameBoard) is not None):
                  initBoard = moveRight(gameBoard) # If a left move results in an unsolvable board but a right move is possible before, do a right move.
                  if (solvedBoard(initBoard) == 'unsolvable'):
                     return(None) # If game board is unsolvable both ways, return None.
                  else:
                     pegMovelist.append(pegIndexesR(gameBoard)) # Add the move tuple to the list.
                     gameBoard = moveRight(gameBoard) # Change game board, re-runs while loop until a solved configuration is found.
                     print(gameBoard)
               else:
                  pegMovelist.append(pegIndexesL(gameBoard)) # Left move results in a solvable board.
                  gameBoard = moveLeft(gameBoard)
                  print(gameBoard)
            elif 'right' in solvedBoard(gameBoard): # Same as above, but for a right move first.
               initBoard = moveRight(gameBoard)
               if (solvedBoard(initBoard) == 'unsolvable') and (findPatternL(gameBoard) is not None):
                  initBoard = moveLeft(gameBoard)
                  if(solvedBoard(initBoard) == 'unsolvable'):
                     return(None)
                  else:
                     pegMovelist.append(pegIndexesL(gameBoard))
                     gameBoard = moveLeft(gameBoard)
                     print(gameBoard)
               else:
                  pegMovelist.append(pegIndexesR(gameBoard))
                  gameBoard = moveRight(gameBoard)
                  print(gameBoard)
            else:
               return(None)
         else: # If no pegs are in the pegboard at all, return None.
            return(None)
   
   if gameBoard.count('X') == 1:
      return(pegMovelist) # If there is only one peg left on the game board, return the moves list (empty if already starting arrangement already solved).

## TEST HARNESS
# The following will be run if you execute the file like python3 pegs_n1234567.py
# Your solution should not depend on this code.
# You may wish to add your own test cases.
if __name__ == '__main__':
   gameBoard = 'XXXoXXXoXX' # should return [(3, 'L'), (0, 'R')]
   print(pegsSolution(gameBoard))