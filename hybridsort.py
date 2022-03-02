import random
from random import randint


#generates random arrays of different lengths
def arrGenerator(size):

    #generate empty list
    lst = []

    #changes the ammount of inputs 
    for _ in range(size):

        #appends a random number to the end of the list between 0 and 1000
        lst.append(randint(0,1000))

    return lst


#selection sort taken from https://www.geeksforgeeks.org/selection-sort/
def selectionSort(arr):
    for i in range(len(arr)):
      
    # Find the minimum element in remaining 
    # unsorted array
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
              
    # Swap the found minimum element with 
    # the first element        
        arr[i], arr[min] = arr[min], arr[i]



#merge sort taken from https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


def hybridSort(lst):
    if(len(lst) < 86):
        selectionSort(lst)
    else:
        mergeSort(lst)


if __name__ == "__main__":

    
    
    size = int(input('Enter an integer between 3 and 200!\n'))

    #generates random array lst based on the input size
    lst = arrGenerator(size)
    print('Here is an unsorted array of size ', size,'!', sep="")
    print(lst)

    #calls the sort algorithm
    hybridSort(lst)


    if(size < 86):
        print('Here is the sorted list using Selection Sort!')
    else:
        print('Here is the sorted list using Merge Sort!')
    print(lst)
    