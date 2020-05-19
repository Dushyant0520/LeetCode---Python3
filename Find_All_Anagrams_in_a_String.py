
#==================================================================
#Name       : Find_All_Anagrams_in_a_String.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================

from collections import Counter

def findAnagrams(s, p):
    s_len, p_len = len(s), len(p)
    #boundary condition
    if s_len < p_len:
        return []

    #p_count is a fixed window
    p_count = Counter(p)
    #s_count is a sliding window, so starts empty
    s_count = Counter()

    result = []
    for i in range(s_len):
        #incrementing count of each element by 1 in s_count for each occurrence
        s_count[s[i]] += 1
        #print ("s_count",s_count)
        #print ("p_count",p_count)
        if i >= p_len:
            #
            if s_count[s[i - p_len]] == 1:
                del s_count[s[i - p_len]]
            else:
                s_count[s[i-p_len]] -= 1

        if p_count == s_count:
            #whenever contents in p_count and s_count match, return the starting index of the sliding window in s
            result.append(i - p_len + 1)
            #print("result", result)
    return result

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    return_target = findAnagrams(s,p)
    print(return_target)


"""
Runtime: 220 ms
Memory Usage: 14.9 MB
"""
