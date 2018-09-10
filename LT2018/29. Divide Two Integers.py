class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        tmp_diff_pos = dividend - divisor
        tmp_diff_neg = dividend + divisor
        val_sign = 1
        if (abs(dividend)>dividend and abs(divisor)==divisor) or (abs(dividend)==dividend and abs(divisor)>divisor):
            val_sign = -1
            dividend = abs(dividend)
            divisor = abs(divisor)
        # t = 0
        # while dividend > divisor:
        #     dividend -= divisor
        #     t += 1
        # return t * val_sign

        res = 0
        while divisor <= dividend:
            tmp,i = divisor,1
            while tmp <= dividend:
                res += i
                dividend -= tmp
                tmp <<= 1
                i <<= 1
        return val_sign * res



if __name__ == '__main__':
    y = Solution()
    # dividend = 10; divisor = 3
    dividend = 7; divisor = -3
    print(y.divide(dividend,divisor))


