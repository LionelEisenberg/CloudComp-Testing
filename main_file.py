### Imports
import sys

### Declare variables
NUM_ARGS = 3

def sorting_func_a(array):
	print("a function running")
	return

def sorting_func_b(array):
	print("b function running")
	return

def sorting_func_c(array):
	print("c function running")
	return


def main():
  arguments = sys.argv

  # Check if the number of arguments is accurate to what we are expecting
  if len(arguments) != NUM_ARGS:
	  print("Error: The number of arguments given does not satisfy the required number")
	  return

  sorting_func = arguments[1]

  filename = arguments[2]
  with open(filename) as f:
    array = f.readlines()

  array = [i.strip() for i in content]

  if sorting_func == "a":
	  return sorting_func_a(array)
  elif sorting_func == "b":
	  return sorting_func_b(array)
  elif sorting_func == "c":
	  return sorting_func_c(array)
  else:
	  print("Error: The function you requested has not been implemented")
	  return


if __name__== "__main__":
  main()
