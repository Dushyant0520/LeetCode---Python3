


#==================================================================
#Name       : Single_Element_in_a_Sorted_Array.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def singleNonDuplicate(nums):
    nums_dict = {}
    for a in range(len(nums)):
        if nums[a] in nums_dict:
            # increment value in the dictionary by 1 if a duplicate is found
            nums_dict[nums[a]] += 1
        else:
            # keys with value 1 are created in the dictionary for the first time
            nums_dict[nums[a]] = 1

    # traverse dictionary without using range
    for b in nums_dict:
        if nums_dict[b] == 1:
            return b


if __name__ == '__main__':
    nums = [3,3,7,7,10,10,12,11,11]
    return_target = singleNonDuplicate(nums)
    print(return_target)

"""
Runtime: 76 ms
Memory Usage: 16.2 MB
Runtime beats 46.36% of python submissions
"""

"""
Solution #2 - Binary search method:

def singleNonDuplicate(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        #check if left and right subarrays are even in length
        check_if_subarrays_even = (right - mid) % 2 == 0
        if nums[mid] == nums[mid + 1]:
            if check_if_subarrays_even:
                left = mid + 2
            else:
                right = mid - 1
        elif nums[mid] == nums[mid - 1]:
            if check_if_subarrays_even:
                right = mid - 2
            else:
                left = mid + 1
        else:
            return nums[mid]
    return nums[left]


if __name__ == '__main__':
    nums = [3,3,7,7,10,10,12,11,11]
    return_target = singleNonDuplicate(nums)
    print(return_target)


Runtime: 64 ms
Memory Usage: 16.2 MB
Runtime beats 96.93% of python submissions
"""
