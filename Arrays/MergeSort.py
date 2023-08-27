# Tags: divideconquerlc, mergesortlc, 

# TIME COMPLEXITY: O(n log n)
    # merge() takes O(n) time
    # The main function, merge_sort(), splits the input array recursively and calls merge() on each half -> total no. of halving operations performed = log_2 n
    # Since merge is called for each half -> TC = O(n log n)

# SPACE COMPLEXITY: O(n)
    # In merge sort, all elements are copied into an auxiliary array of size n

###########################################################################################################

# main function that recursively splits arr into half
def merge_sort(arr):
	if len(arr) < 2: # if arr has 0 or 1 elements, arr is already sorted
		return arr

	mid = len(arr) // 2 # index at which to split arr into half
	left_arr = arr[:mid]
	right_arr = arr[mid:]

	return merge(merge_sort(left_arr), merge_sort(right_arr))

# helper function that merges left_arr and right_arr into a sorted final array
def merge(left_arr, right_arr):
	if not left_arr: return right_arr # if left arr is empty, nothing needs to be merged, return right arr
	if not right_arr: return left_arr # if right arr is empty, nothing needs to be merged, return left arr

	result = []
	left_arr_idx, right_arr_idx = 0, 0

	while len(result) < len(left_arr) + len(right_arr): # iterate both arrs until all elems from left & right arr make it into result arr
		if left_arr[left_arr_idx] < right_arr[right_arr_idx]:
			result.append(left_arr[left_arr_idx])
			left_arr_idx += 1
		else:
			result.append(right_arr[right_arr_idx])
			right_arr_idx += 1
		
		if left_arr_idx == len(left_arr): # if we reached the end of left arr, 
			result.extend(right_arr[right_arr_idx:]) # add remaining right arr elems to result arr and break out of while loop
			break
		if right_arr_idx == len(right_arr): # if we reached the end of right arr,
			result.extend(left_arr[left_arr_idx:]) # add remaining left arr elems to result array and break out of while loop
			break

	return result