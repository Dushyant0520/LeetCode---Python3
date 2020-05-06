#==================================================================
#Name       : Jewels_In_Stones.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def numJewelsInStones(J,S):
    output = 0
    for a in range(len(S)):
        if S[a] in J:
            output += 1
        else:
            continue
    return output



if __name__ == '__main__':
    J = "aAcCdD"
    S = "aAbBcCdDeEfF"
    return_target = numJewelsInStones(J,S)
    print(return_target)


#Solution 2
"""
def numJewelsInStones(J,S):
    output = 0
    for a in S:
        if a in J:
            output += 1
        else:
            continue
    return output
"""
