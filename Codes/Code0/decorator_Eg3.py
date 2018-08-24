def outer(some_func):
    def inner():
        print('before some_func')
        ret = some_func()
        return ret + 1
    return inner

def foo():
    return 1

if __name__ == '__main__':
    decorated = outer(foo)
    print(decorated())

