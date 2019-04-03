class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def helper(i,j):
            res = ''
            while i>=0 and j<len(s) and s[i] == s[j]:
                res = s[i:j + 1]
                i-=1;j+=1

            return res
        res = ''
        for i in range(len(s)):
            tmp0 = helper(i,i)
            tmp1 = helper(i,i+1)
            tmp = tmp0 if len(tmp0)>len(tmp1) else tmp1
            res = tmp if len(tmp)>len(res) else res
        return res

if __name__ == '__main__':
    data_input = 'babad'
    # data_input = 'cbbd'
    data_output = Solution()
    print(data_output.longestPalindrome(data_input))

    '''
    Given a string s, find the longest palindromic substring in s. 
    You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
    '''

    '''
    # 2 apr, 2019
            def helper(i,j):
            res = ''
            while i>=0 and j<len(s) and s[i]==s[j]:
                res = s[i:j+1]
                i-=1;j+=1
            return res

        res = ''
        for i in range(len(s)):
            tmp0 = helper(i,i)
            tmp1 = helper(i,i+1)
            tmp = tmp0 if len(tmp0)>len(tmp1) else tmp1
            res = tmp if len(tmp)>len(res) else res
        return res

    # 1 apr, 2019
            def helper(i,j):
            res = ''
            while i>=0 and j<len(s) and s[i]==s[j]:
                res = s[i:j+1]
                i-=1;j+=1
            return res
        res = ''
        for i in range(len(s)):
            tmp0= helper(i,i)
            tmp1 = helper(i,i+1)
            tmp0 = tmp1 if len(tmp1)>len(tmp0) else tmp0
            res = tmp0 if len(tmp0)>len(res) else res
        return res

# 11 jan, 2019

        def helper(i,j):
            res = ''
            while i>=0 and j<len(s) and s[i]==s[j]:
                res = s[i:j + 1]
                i-=1;j+=1
            return res

        res = ''
        for i in range(len(s)):
            tmp0 = helper(i,i)
            tmp1 = helper(i,i+1)
            tmp=''
            if len(tmp1)>len(tmp0):
                tmp = tmp1
            else:
                tmp = tmp0
            if len(tmp)>len(res):
                res = tmp
        return res
    
# 10 jan, 2019
        def helper(s,l,r):
            res = ''
            while l<=r and l>=0 and r<len(s) and s[l] == s[r]:
                res = s[l:r+1]
                l,r = l-1,r+1
            return res

        res = ''
        for i in range(len(s)-1):
            r1 = helper(s,i,i)
            r2 = helper(s,i,i+1)
            res1 = r1 if len(r1)>len(r2) else r2
            res = res1 if len(res1)>len(res) else res
        return res
    
    6 dec
    
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