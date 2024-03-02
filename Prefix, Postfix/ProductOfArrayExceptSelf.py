# https://leetcode.com/problems/product-of-array-except-self/description/
# MEDIUM
# prefixlc, #238

# GIVEN:
    # integer array, nums

# TASK:
    # return an array answer such that answer[i] = product of all the elements of nums except nums[i]
    # NOTE: must write an algorithm that runs in O(n) time and without using division

# EXAMPLES:
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]

    # Input: nums = [-1,1,0,-3,3]
    # Output: [0,0,9,0,0]

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS + PREFIX / POSTFIX PRODUCT (unoptimized i.e. O(n) space)
# pre array stores prefix products (i.e. products of all elements up till and including pre[i])
# post array stores postfix products (i.e. products of all elements after and including pre[i])
# Use 1 pointer (pre_ptr) starting from the 2nd elem and another pointer (post_ptr) starting from 2nd last elem
# Iterate both pointers through nums at the same time, filling up and pre and post arrays by multiplying each element nums[i] in nums with the element in pre[i-1] and post[i+1] respectively
# iterate through nums with iterator i and append each pre[i-1] * post[i+1] to result
    # if i-1 or i+1 are out of bounds, multiply by 1 instead

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def productExceptSelf(nums):
        pre, post = [1] * len(nums), [1] * len(nums)
        pre[0], post[-1] = nums[0], nums[-1]
        result = []
        pre_ptr, post_ptr = 1, len(nums)-2 # pre's pointer starts @ 2nd elem, post's pointer starts @ 2nd last elem

        while pre_ptr < len(nums) and post_ptr >= 0:
            pre[pre_ptr] = pre[pre_ptr-1] * nums[pre_ptr]
            post[post_ptr] = post[post_ptr+1] * nums[post_ptr]
            pre_ptr += 1
            post_ptr -= 1
        
        # at this step, 
        # nums = [1, 2, 3, 4]
        # pre =  [1, 2, 6, 24]
        # post = [24, 24, 12, 4]
        # final result should be = [1*24, 1*12, 2*4, 6*1]
            # each result[i] = pre[i-1] * post[i+1]
        
        for i in range(len(nums)):
            result.append((pre[i-1] if i-1 >= 0 else 1) * (post[i+1] if i+1 < len(nums) else 1))
        return result

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: PREFIX / POSTFIX PRODUCT ONLY (optimized i.e. O(1) space complexity)
# Instead of having a prefix/postfix array, use a running integer variable for prefix and postfix
# Add each prefix element to result array
# Multiply each postfix element with corresponding prefix element in result to get the final array

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def productExceptSelf(nums): # nums = [1, 2, 3, 4]
    result = [1] * len(nums) # result array will first store prefix values through the 1st for-loop
        
    prefix = 1 # initialize prefix to 1, since the prefix of the 1st element in nums would be 1
    for i in range(len(nums)):
        result[i] = prefix # if i=0 (i.e. 1st element of nums), prefix will be 1
        prefix = prefix * nums[i] # this prefix value set here is meant for the next no. (i.e. at i+1)
        # here, we set the prefix for the next number, then add it to result array in the next iteration
    
    # at this step, prefix = [1, 1, 2, 6]
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1): # iterate result array backwards
        result[i] = postfix * result[i] # we have to multiply the existing value in result (which is the prefix of current nums[i]) with the postfix value because answer[i] = prefix[i] * postfix[i]
        postfix = postfix * nums[i] # this postfix value is the postfix for the no. in the next iteration (i.e. the previous no.)

    # postfix values before multiplying by prefix values = [24, 12, 4, 1]

    return result
    # result = [24,12,8,6]

#==========================================================================================================

# ✅✅✅ ALGORITHM 2B: MY SOLUTION with O(1) space (attempted March 2, 2024)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def productExceptSelf(nums):
    result = [1] * len(nums) # this will be prefix array first
    
    # GET PREFIXES
    # result[0] = 1 (prefix of 1st elem is always 1, since there are no elems on the left of the 1st elem)
    for i in range(1, len(nums)): # start from 2nd element, since prefix of 1st elem is already set
        result[i] = result[i-1] * nums[i-1] # FORMULA: prefix(n) = prefix(n-1) * nums(n-1)
    
    # at this point, result = array of prefixes of nums
        
    # GET POSTFIXES
    # postfix of last elem is always 1, so we skip last element and go to 2nd last elem
    postfix = nums[-1] # for the 2nd last elem in nums, its postfix is the last elem in nums
    for i in range(len(nums)-2, -1, -1):
        result[i] = result[i] * postfix # FORMULA: result(i) = prefix(i) * postfix
        postfix *= nums[i] # update postfix value for the nums elem (nums[i-1]) in the next iteration; postfix for i-1 = postfix(n) * nums[n]
    
    return result