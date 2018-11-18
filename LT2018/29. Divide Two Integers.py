class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
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


if __name__ == '__main__':
    y = Solution()
    # dividend = 10; divisor = 3
    dividend = 7; divisor = -3
    print(y.divide(dividend,divisor))


