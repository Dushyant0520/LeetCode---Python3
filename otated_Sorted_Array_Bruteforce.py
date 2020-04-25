
#==================================================================
#Name       : Rotated_Sorted_Array.py - Brute Force Approach
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def search(nums, target):
    print(len(nums))
    for a in range(len(nums)):
        if nums[a] == target:
            return a
        else:
            continue
    return -1

if __name__ == '__main__':
    nums = []
    target = 2
    return_value = search(nums, target)
    print(return_value)
