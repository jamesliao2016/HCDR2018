class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def ret_tmp(s,l,r):
            res = []
            while l>=0 and r<len(s) and s[l] == s[r]:
                res = s[l:r + 1]
                l-=1;r+=1
            return res
        val_len = 0
        res = []
        tmp_res = []
        for i in range(len(s)):
            str_odd = ret_tmp(s,i,i)
            str_even = ret_tmp(s,i,i+1)
            if len(str_even)>len(str_odd):
                tmp_res = str_even
            else:
                tmp_res = str_odd
            if len(tmp_res) > len(res):
                res = tmp_res
        return res







if __name__ == '__main__':
    data_input = 'babad'
    # data_input = 'cbbd'
    data_output = Solution()
    print(data_output.longestPalindrome(data_input))

    '''
    # 20 nov, 2018
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

    '''