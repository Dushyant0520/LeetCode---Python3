#==================================================================
#Name       : First_Unique_Character_in_a_String.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def firstUniqChar(s):
    count = 0
    for a in range(len(s)):
        if s[a] in s[:a] or s[a] in s[a+1:]:
            count += 1
            continue
        else:
            return a
    if count == len(s):
        return -1


if __name__ == '__main__':
    s = "sadfmasdf"
    return_target = firstUniqChar(s)
    print(return_target)
