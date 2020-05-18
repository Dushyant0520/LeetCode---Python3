




#==================================================================
#Name       : Find_All_Anagrams_in_a_String.py
#Author     : Dushyant Venkatesan
#email      : dhushyanth.05@gmail.com
#==================================================================


from collections import Counter


def findAnagrams(s, p):
    s_len, p_len = len(s), len(p)

    if s_len < p_len:
        return []

    p_count = Counter(p)
    s_count = Counter()

    result = []
    for i in range(s_len):
        s_count[s[i]] += 1
        if i >= p_len:
            if s_count[s[i - p_len]] == 1:
                del s_count[s[i - p_len]]
            else:
                s_count[s[i-p_len]] -= 1

            if p_count == s_count:
                result.append(i - p_len + 1)

    return result






if __name__ == '__main__':
    s = "abab"
    p = "ab"
    return_target = findAnagrams(s,p)
    print(return_target)
