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

if __name__ == '__main__':

    one = Coordinates(100,100)
    two = Coordinates(50,300)
    print(one)

    # add(one,two)
    print(add(one,two))
    print(sub(one,two))