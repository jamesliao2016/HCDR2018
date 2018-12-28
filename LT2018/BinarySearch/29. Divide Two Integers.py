class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        did2 = abs(dividend)
        dir2 = abs(divisor)
        sig = 1
        tmp = [did2+dividend,dir2+divisor]
        j = 0
        for i in tmp:
            if i==0:
                j+=1
        if j==1:
            sig = -1
        res = 0
        while did2>=dir2:
            tmp_did = did2
            tmp_dir = dir2
            j=1
            while did2>=tmp_dir:
                res += j
                did2 -= tmp_dir
                j <<1
                tmp_dir<<1
        if sig<0:
            res = -res
        return res

if __name__ == '__main__':
    y = Solution()
    # dividend = 10; divisor = 3
    dividend = 7; divisor = -3
    print(y.divide(dividend,divisor))

    '''
    
    Given two integers dividend and divisor, divide two integers without using multiplication, 
    division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only 
store integers within the 32-bit signed integer range: [−231,  231 − 1].
 For the purpose of this problem, assume that your function returns 231 − 1 when the division 
 result overflows.
    
    # dec 28
    
            val_postv = (divisor > 0) is (dividend > 0)
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp_times = 1
            tmp_div = divisor
            while dividend >= tmp_div:
                res += tmp_times
                dividend -= tmp_div
                tmp_div <<=1
                tmp_times <<=1
        res_final= min(res,pow(2,31)-1)  if val_postv else max(-res,-pow(2,31))
        return res_final

    # 20 nov, 2018
            val_postv = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        while dividend > divisor:
            i,tmp = divisor,1
            while dividend > i:
                res += tmp
                dividend -= i
                i<<=1
                tmp<<=1
        return res if val_postv == 1 else -res


    '''


