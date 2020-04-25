
#==================================================================
#Name       : Rotated_Sorted_Array.py - Binary Tree Approach
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def search(nums, target):
    pivot_index = 0
    for a in range(len(nums)-1):
        #Check if first element in the original list is the target element before splitting the list
        if nums[a] == target:
            return a
        # Identify Pivot element and create Pivot_Index
        elif nums[a]<nums[a-1]:
            pivot_index = a
    #Create 2 sub-arrays based on pivot finding
    # Remember last index/value in slice range is ignored
    nums_1 = nums[:pivot_index-1]
    print("Subarrya 1 is: ", nums_1)
    nums_2 = nums[pivot_index-1:]
    print("Subarrya 2 is: ", nums_2)

    #Check if target is in subarray 1
    begin_index_1 = 0
    end_index_1 = len(nums_1) - 1
    while begin_index_1 <= end_index_1:
        midpoint_1 = begin_index_1 + (end_index_1 - begin_index_1) // 2
        midpoint_value_1 = nums_1[midpoint_1]
        if midpoint_value_1 == target:
            return midpoint_1
        elif target < midpoint_value_1:
            end_index_1 = midpoint_1 - 1
        else:
            begin_index_1 = midpoint_1 + 1

    # Check if target is in subarray 2
    begin_index_2 = 0
    end_index_2 = len(nums_2) - 1
    while begin_index_2 <= end_index_2:
        midpoint_2 = begin_index_2 + (end_index_2 - begin_index_2) // 2
        midpoint_value_2 = nums_2[midpoint_2]
        if midpoint_value_2 == target:
            return midpoint_2 + len(nums_1)
        elif target < midpoint_value_2:
            end_index_2 = midpoint_2 - 1
        else:
            begin_index_2 = midpoint_2 + 1
    #Return -1 if the element isn't found in both subarrays
    return -1


if __name__ == '__main__':
    nums = []
    target = 1
    return_target = search(nums, target)
    print(return_target)

