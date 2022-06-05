# Author:           Steven Tran
# Date:             2021-11-17
# Description:      This program plots the time it takes for bubble sort and
# insertion sort to finish sorting the same set of data (a list in this
# case). It uses the matplotlib module to graph the results of 10 different
# sized randomly generated data sets.

# Modules Imports
import time
import random
import functools
from matplotlib import pyplot
from shell_sort import shellSort
from selection_sort import selectionSort
from merge_sort import mergeSort
# from static_array import StaticArray
from dynamic_array import DynamicArray
from min_heap import MinHeap, heapsort, MinHeapException


def sort_timer(func):
	"""Wrapper for timing the duration a function takes to run."""
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		"""Prints out the total elapsed time."""
		start = time.perf_counter()
		# print(f"Start time: {start}")
		func(*args, **kwargs)
		end = time.perf_counter()
		# print(f"End time: {end}")
		total_elapsed_time = (end - start)
		print(f"Total elapsed time: {total_elapsed_time:0.4f} seconds")
		return total_elapsed_time
	return wrapper

@sort_timer
def bubble_sort(a_list):
	"""Sorts a_list in ascending order.
	Note: From Module 4"""
	for pass_num in range(len(a_list) - 1):
		for index in range(len(a_list) - 1 - pass_num):
			if a_list[index] > a_list[index + 1]:
				temp = a_list[index]
				a_list[index] = a_list[index + 1]
				a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):
	"""Sorts a_list in ascending order.
	Note: From Module 4"""
	for index in range(1, len(a_list)):
		value = a_list[index]
		pos = index - 1
		while pos >= 0 and a_list[pos] > value:
			a_list[pos + 1] = a_list[pos]
			pos -= 1
		a_list[pos + 1] = value

@sort_timer
def merge_sort(a_list):
	mergeSort(a_list)

@sort_timer
def selection_sort(a_list):
	selectionSort(a_list)

@sort_timer
def shell_sort(a_list):
	shellSort(a_list)

@sort_timer
def heap_sort(a_list):
	heapsort(a_list)

@sort_timer
def compare_sorts(sorting_alg1=bubble_sort, sorting_alg2=insertion_sort,
sorting_alg3=merge_sort, sorting_alg4=selection_sort, sorting_alg5=shell_sort,
sorting_alg6=heap_sort):
	"""Will compare the two sorting functions: bubble sort and insertion
	sort."""

	# Initializing the number of points for the list of random #s.
	point_count = 1000
	point_count_max = 9000
	point_increment = 1000

	# Initializing the sorting algorithm's x and y values
	x_axis = []
	for i in range(point_count, point_count_max + 1, point_increment):
		x_axis.append(i)
	# x_axis = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
	alg1_ytime = []
	alg2_ytime = []
	alg3_ytime = []
	alg4_ytime = []
	alg5_ytime = []
	alg6_ytime = []

	while point_count <= point_count_max:
		list_1 = []         # first list to be randomized by the plot limit
		for i in range(point_count):
			list_1.append(random.randint(1, 10000)) # randomizes value
		# between 1 and 10000
		list_2 = list_1.copy() 
		list_3 = list_1.copy()
		list_4 = list_1.copy()
		list_5 = list_1.copy()
		list_6 = DynamicArray(list_1.copy())

		# Sorting begins + info for human to know status.
		sort1 = sorting_alg1(list_1)
		alg1_ytime.append(sort1)
		print(f"* Completed {sorting_alg1.__name__} with {point_count} "
		      f"points")

		sort2 = sorting_alg2(list_2)
		alg2_ytime.append(sort2)
		print(f"* Completed {sorting_alg2.__name__} with {point_count} "
		      f"points\n")

		sort3 = sorting_alg3(list_3)
		alg3_ytime.append(sort3)
		print(f"* Completed {sorting_alg3.__name__} with {point_count} "
		      f"points\n")

		sort4 = sorting_alg4(list_4)
		alg4_ytime.append(sort4)
		print(f"* Completed {sorting_alg4.__name__} with {point_count} "
		      f"points\n")

		sort5 = sorting_alg5(list_5)
		alg5_ytime.append(sort5)
		print(f"* Completed {sorting_alg5.__name__} with {point_count} "
		      f"points\n")

		sort6 = sorting_alg6(list_6)
		alg6_ytime.append(sort6)
		print(f"* Completed {sorting_alg6.__name__} with {point_count} "
		      f"points\n")
		point_count += point_increment

	# Plot Section that plots Number of Elements Sorted versus the Time
	pyplot.plot(x_axis, alg1_ytime, 'co--', linewidth=2,
	            label=f"{sorting_alg1.__name__}")
	pyplot.plot(x_axis, alg2_ytime, 'g.-.', linewidth=2,
	            label=f"{sorting_alg2.__name__}")
	pyplot.plot(x_axis, alg3_ytime, 'rv--', linewidth=2,
	            label=f"{sorting_alg3.__name__}")
	pyplot.plot(x_axis, alg4_ytime, 'm^--', linewidth=2, 
	            label=f"{sorting_alg4.__name__}")
	pyplot.plot(x_axis, alg5_ytime, 'bX:', linewidth=1.5,
	            label=f"{sorting_alg5.__name__}")
	pyplot.plot(x_axis, alg6_ytime, color = 'orangered', linestyle='dotted',
				linewidth=2, label=f"{sorting_alg6.__name__}")
	pyplot.xlabel("Number of Elements Sorted")
	pyplot.ylabel("Time to Sort (seconds)")
	pyplot.title("Sorting Algorithm Comparison")
	pyplot.legend()
	pyplot.grid()
	pyplot.show()

def main():
	"""Per the read me, to make things a little more efficient for the TAs :)"""
	compare_sorts()

if __name__ == "__main__":
	main()