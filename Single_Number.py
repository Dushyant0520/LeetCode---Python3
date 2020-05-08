

#==================================================================
#Name       : Single_Number.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================


def singleNumber(nums):
    nums_dict = {}
    for a in range(len(nums)):
        if nums[a] in nums_dict:
            #increment value in the dictionary by 1 if a duplicate is found
            nums_dict[nums[a]] += 1
        else:
            #keys with value 1 are created in the dictionary for the first time
            nums_dict[nums[a]] = 1

    #traverse dictionary without using range
    for b in nums_dict:
        if nums_dict[b] == 1:
            return b
            break

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    return_target = singleNumber(nums)
    print(return_target)
    
    
