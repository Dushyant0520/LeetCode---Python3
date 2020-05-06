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

    
"""
Leetcode Solution:

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
        
Approach 1: Linear time solution
The best possible solution here could be of a linear time because to ensure that the character is unique you have to check the whole string anyway.

The idea is to go through the string and save in a hash map the number of times each character appears in the string. That would take \mathcal{O}(N)O(N) time, where N is a number of characters in the string.

And then we go through the string the second time, this time we use the hash map as a reference to check if a character is unique or not.
If the character is unique, one could just return its index. The complexity of the second iteration is \mathcal{O}(N)O(N) as well.

Complexity Analysis:
Time complexity : O(N) since we go through the string of length N two times.
Space complexity : O(N) since we have to keep a hash map with N elements.
"""
