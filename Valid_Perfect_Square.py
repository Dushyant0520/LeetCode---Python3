
#==================================================================
#Name       : Valid_Perfect_Square.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================


def isPerfectSquare(num):
    start = 0
    end = num
    mid = 0
    if num == 0 or num == 1:
        return True
    while start <= end:
        mid = start + (end - start)//2
        if mid*mid == num:
            return True
        elif mid*mid < num:
            start = mid + 1
        else:
            end = mid - 1
    return False


if __name__ == '__main__':
    num = 16
    return_target = isPerfectSquare(num)
    print(return_target)

"""
Runtime: 24 ms
Memory Usage: 13.8 MB
Run time beats 91.91% of python submissions
"""
