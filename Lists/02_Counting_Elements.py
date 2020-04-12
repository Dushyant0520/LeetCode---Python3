

def countElements(arr):
    count = 0
    for a in range(len(arr)):
        if arr[a] + 1 in arr:
            count = count + 1
        else:
            continue
    return count


if __name__ == '__main__':
    arr = [1,1,2,2]
    return_target = countElements(arr)
    print(return_target)
