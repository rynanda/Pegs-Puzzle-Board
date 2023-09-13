import importlib
import importlib.util
import sys
import traceback
import pprint
import os

if len(sys.argv) != 2:
   print("Usage: python3 pegtester.py <pegs_solution_filename>")

try:
   filename = sys.argv[1]
   if os.path.basename(filename) != 'pegs.py':
      print(f"Warning!  Filename is {os.path.basename(filename)}, expected pegs.py.  Automated marker may not correctly detect your solution.")
   spec = importlib.util.spec_from_file_location('pegssolution', filename)
   if spec is None:
      print("Error when loading file.")
      sys.exit(1)
   pegssolution = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(pegssolution)
except Exception as e:
   print(f"Problem parsing the solution:")
   traceback.print_exc()
   sys.exit(1)

if 'pegsSolution' in dir(pegssolution):
   board = 'XXoXoXoXo'
   solution = pegssolution.pegsSolution(board)
   print(f"Game board is {board}")
   if solution != [(0, 'R'), (2, 'R'), (4, 'R'), (7, 'L')]:
      print("Solution differs from real solution!")
      print("Solution found: ")
      pprint.pprint(solution)
      print("Real solution: ")
      pprint.pprint([(3, 'L'), (0, 'R')])
   else:
      print("Correct solution found!")

   # We suggest that you create a method to automatically check if a solution is correct.
   # To do this, one method is to apply all moves in the solution to the starting game board 
   # and test if the result is a solved configuration.  Much of the code to do this
   # is required to find the solution anyway.
   # Note that the solution may not be unique!
else:
   print("Couldn't find pegsSolution function!")