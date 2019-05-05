# def disc_sp(x):
#     i = 0
#     while x[i] == ' ':
#         i += 1
#     return x[i:]
#
# def proc(x):
#     tmp = disc_sp(x)
#     if tmp[0] not in '+-1234567890':
#         return 0
#     else:
#         if abs(int(tmp))>=pow(2,31) or abs(int(tmp))<pow(2,-31):
#             return pow(2,-31) if tmp[0]=='-' else pow(2,31)-1
#         else:
#             return int(tmp)
#
# def atoi(str):
#     if len(str) == 0:
#         return 0
#     i = 0
#     while str[i] == ' ':
#         i += 1
#     tmp = str[i:]
#     while tmp[-1] not in '1234567890':
#         tmp = tmp[:-1]
#         if len(tmp) == 0:
#             return 0
#
#     if tmp[0] not in '+-1234567890':
#         return 0
#     else:
#         if abs(float(tmp)) >= pow(2, 31) or abs(float(tmp)) < pow(2, -31):
#             return pow(2, -31) if tmp[0] == '-' else pow(2, 31) - 1
#         else:
#             return float(tmp)

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num_set = '0123456789'
        for ii in str:
            if ii == ' ':
                str = str[1:]
            else:
                if ii in num_set+'+-':
                    break
                else:
                    return 0


        def toolfun(i,j):
            tmp_rlt = ''
            while j<len(str) and str[j] in num_set:
                j+=1
            j-=1
            while i >= 0 and str[i] in (num_set + '+-') and str[j] in num_set:
                tmp_rlt = str[i:j+1]
                if str[i] in '+-':
                    return tmp_rlt
                i-=1
            return tmp_rlt
        if str=='':
            return ''

        res=''
        for i in range(len(str)):
            tmp1 = toolfun(i,i)
            tmp2 = toolfun(i,i+1)
            if len(tmp1)>len(tmp2):
                tmp = tmp1
            else:
                tmp = tmp2
            if len(tmp)>len(res) and tmp not in '+-':
                res = tmp
        res = int(res) if len(res)>0  else 0
        if res>pow(2,31)-1 or res<-pow(2,31):
            res = pow(2,31)-1 if res>0 else -pow(2,31)
        return res


if __name__ == '__main__':
    # s = '+'
    # print(disc_sp(s))
    # print(proc(s))
    # data_input = "+"
    data_input = "words and 987"
    # data_input = "4193 with words"
    # data_input = "   -42"
    # data_input = "+42"
    # data_input = "3.14159"
    # data_input = "-91283472332"
    # print(atoi(s))
    data_output = Solution()
    print(data_output.myAtoi(data_input))