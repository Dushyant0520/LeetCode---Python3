
#==================================================================
#Name       : Find_the_Town_Judge.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

def findJudge(N, trust):
    trust_dict ={}
    Label = []
    Label_Count = 0

    if len(trust) == 0:
        return N

    if len(trust) == 1:
        return trust[0][1]

    for i in range(len(trust)):
        if trust[i][1] in trust_dict:
            # increment value in the dictionary by 1 if a duplicate is found
            trust_dict[trust[i][1]] += 1
        else:
            # keys with value 1 are created in the dictionary for the first time
            trust_dict[trust[i][1]] = 1

    for a in trust_dict:
        if trust_dict[a] == max(trust_dict.values()):
            Label = a

    #Potential Judge = value in position b in trust  which has highest number of occurrences
    #If potential judge is in position a of an array element
    for b in range(len(trust)):
        if trust[b][0] == Label:
            return -1

    for x in range(len(trust)):
        if trust[x][1] == Label:
            Label_Count += 1
        else:
            continue

    if Label_Count == N-1:
        return Label
    else:
        return -1


if __name__ == '__main__':
    N = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    return_target = findJudge(N, trust)
    print(return_target)

"""
Runtime: 968 ms
Memory Usage: 18 MB
Run time beats 27.04% of python submissions
"""

"""
Youtube Solution:
-----------------
def findJudge(N, trust):
          
    if len(trust) < N-1:
        return -1
    
    trusted = [0] * (N+1)
    trusting = [0] * (N+1)
    
    for out_, in_ in trust:
        trusting[out_] += 1
        trusted[in_] += 1
        
    for a in range (1, N+1):
        if trusted[a] == N-1 and trusting[a] == 0:
            return a

"""

"""
Runtime: 968 ms
Memory Usage: 18 MB
Run time beats 49.48% of python submissions
"""
