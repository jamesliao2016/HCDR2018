class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def toolfun(i,j):
            tmp_res = ''
            while i>=0 and j<len(s) and s[i]==s[j]:

                tmp_res = s[i:j+1]
                i -= 1;
                j += 1
            return tmp_res

        if s==' ':
            return ''
        res = ''
        for i in range(len(s)):
            # if i%2==0:
            tmp1 = toolfun(i,i)
            # else:
            tmp2 = toolfun(i, i + 1)
            if len(tmp1)>len(tmp2):
                tmp = tmp1
            else:
                tmp = tmp2
            if len(tmp)>len(res):
                res = tmp
        return res


if __name__ == '__main__':
    # data_input = 'babad'
    data_input = 'bb'
    data_output = Solution()
    print(data_output.longestPalindrome(data_input))