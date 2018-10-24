class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
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

if __name__ == '__main__':
    # data_input = "bbbbb"
    # data_input = "pwwkew"
    # data_input = "abcabcbb"
    data_input = "anviaj"
    data_output = Solution()
    print(data_output.lengthOfLongestSubstring(data_input))
