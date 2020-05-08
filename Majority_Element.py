
#==================================================================
#Name       : Majority_Element.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def majorityElement(nums):
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
        if nums_dict[b] > len(nums)/2:
            return b
            break




if __name__ == '__main__':
    nums = [1,1,2,2,2]
    return_target = majorityElement(nums)
    print(return_target)
    
    
