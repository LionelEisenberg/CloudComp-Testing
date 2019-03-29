### Imports
import sys

### Declare variables
NUM_ARGS = 3

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp
	return array

def bubble_sort(array):
	print("bubble sort running")
	for i in range(len(array)):
		for j in range(len(array) - i - 1):
			if array[j] > array[j+1]:
				array = swap(array, j, j + 1)
	
	return

def insertion_sort(array):
	print("insertion sort running")
	return

def selection_sort(array):
	print("selection sort running")
	return

def main():
  arguments = sys.argv

  # Check if the number of arguments is accurate to what we are expecting
  if len(arguments) != NUM_ARGS:
	  print("Error: The number of arguments given does not satisfy the required number")
	  return

  sorting_func = arguments[1]

  # Takes filename, opens file, and transcribes file contents to an array.
  filename = arguments[2]
  try:
	  with open(filename) as f:
	    array = f.readlines()
	  array = [int(i.strip()) for i in array]
  except EnvironmentError:
	  print("Error: The file you requested is not valid.")
	  return

  if sorting_func == "bubble":
	  return bubble_sort(array)
  elif sorting_func == "insertion":
	  return insertion_sort(array)
  elif sorting_func == "selection":
	  return selection_sort(array)
  else:
	  print("Error: The function you requested has not been implemented")
	  return


if __name__== "__main__":
  main()
