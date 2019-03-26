### Imports
import sys

### Declare variables
NUM_ARGS = 2

def sorting_func_a():
	print("a function running")
	return

def sorting_func_b():
	print("b function running")
	return

def main():
  arguments = sys.argv
  if len(arguments) != NUM_ARGS:
	  print("Error: The number of arguments given does not satisfy the required number")
	  return

  sorting_func = arguments[1]
  if sorting_func == "a":
	  return sorting_func_a()
  elif sorting_func == "b":
	  return sorting_func_b()
  else:
	  print("Error: The function you requested has not been implemented")
	  return


if __name__== "__main__":
  main()
