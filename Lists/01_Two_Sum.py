def twoSum(nums, target):
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a] + nums[b] == target:
                    return [a, b]
                else:
                    continue
        return -1

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 35
    return_target = twoSum(nums, target)
    print(return_target)
