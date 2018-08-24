class Coordinates(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return ('Coordinates:' + str(self.__dict__))

def add(a,b):
    return Coordinates(a.x+b.x,a.y+b.y)

def sub(a,b):
    return Coordinates(a.x-b.x,a.y-b.y)

def wrapper(func):
    def checker(a,b):
        if a.x<0 or a.y<0:
            a = Coordinates(a.x if a.x>0 else 0, a.y if a.y>0 else 0)
        if b.x<0 or b.y<0:
            b = Coordinates(b.x if b.x>0 else 0, b.y if b.y>0 else 0)
        ret = func(a,b)
        if ret.x<0 or ret.y<0:
            ret = Coordinates(ret.x if ret.x>0 else 0, ret.y if ret.y>0 else 0)
        return ret
    return checker

if __name__ == '__main__':

    one = Coordinates(100,100)
    two = Coordinates(50,300)
    # print(one)

    # add(one,two)
    # print(add(one,two))
    # print(sub(one,two))

    add = wrapper(add)
    sub = wrapper(sub)
    print(sub(one,two))