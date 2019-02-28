class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s = {}
        res = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in dict_s:
                res = max(res,i - l + 1)
                # l = i+1
            else:
                # if l>0:
                l = max(l,dict_s[s[i]]+1)
                res = max(res, i - l + 1)
            dict_s[s[i]] = i
        return res


if __name__ == '__main__':
    # data_input = "bbbbb"
    # data_input = "pwwkew"
    # data_input = "abcabcbb"
    # data_input = "anviaj"
    data_input = "abba"
    data_output = Solution()
    print(data_output.lengthOfLongestSubstring(data_input))

'''

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
             # dec 21
             
                     res = 0
        starter = 0
        dict_n = {}
        for i in range(len(s)):
            if s[i] in dict_n:
                starter = max(starter,dict_n[s[i]]+1)
                res = max(res,i - starter + 1)
            else:
                res = max(res, i - starter + 1)
            dict_n[s[i]] = i
        return res
        
        6 dec
        if s == '':
            return 0
        l1,l2 = 0,1
        res=0
        while l2<=len(s)-1:
            if len(set(s[l1:l2+1])) == l2+1-l1:
                l2+=1
                res = max(res, l2 - l1)
            else:
                l1 +=1
                # l1 = l2
                # l2 = l1+1
        return res

'''
