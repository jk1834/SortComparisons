import xlwt
from xlwt import Workbook

import random
from random import seed
from random import randint

import time

#random seed shenanigans
seed(42)

#generates random arrays of different lengths
def arrGenerator(size):

    #generate empty list
    lst = []

    #changes the ammount of inputs 
    for _ in range(size):

        #appends a random number to the end of the list between 0 and 1000
        lst.append(randint(0,1000))

    return lst



def merge_sort_time(wb):
    
    #creates excel sheets

    counter = 0

    sheet1.write(1,1,'Merge Sort Tmes (s)')

    for size in range(3,200):

        #generates random array of size n
        lst = arrGenerator(size)
        print('Not Sorted!')
        print(lst)

        for element in range(100):

            t0 = time.perf_counter()
            mergeSort(lst)
            t1 = time.perf_counter()
            
            counter += 1

            timeTaken = t1 - t0
            sheet1.write(counter+1,1,timeTaken)



def selection_sort_time(wb):

    #creates excel sheets
    counter = 0

    sheet1.write(1,2,'Selection Sort Tmes (s)')

    for size in range(3,200):

        #generates random array of size n
        lst = arrGenerator(size)

        for element in range(100):

            t0 = time.perf_counter()
            selectionSort(lst)
            t1 = time.perf_counter()

            counter += 1

            timeTaken = t1 - t0
            sheet1.write(counter+1,2,timeTaken)




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



# Driver Code
if __name__ == '__main__':

    
    #Create excel sheet
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok = True)

    #call the two time functions to record the time in excel
    merge_sort_time(wb)
    selection_sort_time(wb)

    #save the data
    wb.save('SortingData.xls')

    

