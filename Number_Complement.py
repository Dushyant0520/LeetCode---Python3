#==================================================================
#Name       : Number_Complement.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def findComplement(num):
    num_bin = bin(num)
    num_str = ""
    for a in range(2,len(num_bin)):
        if int(num_bin[a]) == 0:
            num_str += "1"
        elif int(num_bin[a]) == 1:
            num_str += "0"
    num = int(num_str,2)
    return num



if __name__ == '__main__':
    num = 3
    return_target = findComplement(num)
    print(return_target)


"""
LeetCode Solution:

def findComplement(self, num: int) -> int:
        return num^(2**(len(bin(num)[2:]))-1)

"""
