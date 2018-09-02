def disc_sp(x):
    i = 0
    while x[i] == ' ':
        i += 1
    return x[i:]

def proc(x):
    tmp = disc_sp(x)
    if tmp[0] not in '+-1234567890':
        return 0
    else:
        if abs(int(tmp))>=pow(2,31) or abs(int(tmp))<pow(2,-31):
            return pow(2,-31) if tmp[0]=='-' else pow(2,31)-1
        else:
            return int(tmp)

def atoi(str):
    if len(str) == 0:
        return 0
    i = 0
    while str[i] == ' ':
        i += 1
    tmp = str[i:]
    while tmp[-1] not in '1234567890':
        tmp = tmp[:-1]
        if len(tmp) == 0:
            return 0

    if tmp[0] not in '+-1234567890':
        return 0
    else:
        if abs(float(tmp)) >= pow(2, 31) or abs(float(tmp)) < pow(2, -31):
            return pow(2, -31) if tmp[0] == '-' else pow(2, 31) - 1
        else:
            return float(tmp)

if __name__ == '__main__':
    s = '+'
    # print(disc_sp(s))
    # print(proc(s))
    print(atoi(s))