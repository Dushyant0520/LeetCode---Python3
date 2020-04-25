

#==================================================================
#Name       : String_Shift.py - Brute Force Approach
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def stringShift(s, shift):
    count_shift_left = 0
    count_shift_right = 0
    count_left_total = 0
    count_right_total = 0
    action_final = ""
    count_final = 0
    count_final_new = 0
    new_str = ""
    for a in range(len(shift)):
        if shift[a][0] == 0:
            count_left_total += shift[a][1]
        elif shift[a][0] == 1:
            count_right_total += shift[a][1]
        else:
            continue
    print ("count_left_total is : ", count_left_total)
    print ("count_right_total is : ", count_right_total)

    count_final = abs (count_left_total - count_right_total)
    #Check if total shift count is greater than the length of the string
    if count_final > len(s):
        count_final_new = count_final % len(s)
    else:
        count_final_new = count_final

    print("count_final is : ", count_final)
    if count_left_total > count_right_total:
        action_final = "left"
    if count_right_total > count_left_total:
        action_final = "right"
    print ("Shift Operation : ", action_final)

    if action_final == "left":
        #shift left operation
        new_str = s[count_final_new:] + s[:count_final_new]
    elif action_final == "right":
        # shift right operation
        new_str = s[-count_final_new:] + s[:-count_final_new]
    else:
        print("Error")

    print ("Final string is :", new_str)
    return new_str

if __name__ == '__main__':
    s = "xqgwkiqpif"
    shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
    return_target = stringShift(s, shift)
    print(return_target)
