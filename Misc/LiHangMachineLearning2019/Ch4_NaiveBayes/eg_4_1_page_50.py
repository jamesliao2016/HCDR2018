'''
来自李航 <<统计学习方法>>第50页的例子
朴素贝叶斯
'''

class Solution():
    def __init__(self,train):
        self.train = train
    def probPrior(self,y):
        res = 0
        for i in self.train:
            if i[-1]==y:
                res += 1
        return res/len(self.train)
    def probPosteriori(self,y,test):
        priorY = self.probPrior(y)
        res = 1
        for i in range(len(test)):
            tmp_i = test[i]
            tmp_cnt = 0
            for j in self.train:
                if j[i] == tmp_i and j[-1] == y:
                    tmp_cnt += 1
            res = res * tmp_cnt / priorY / len(self.train)
        return res*priorY
    def naiveBayesClassfier(self,test):
        res,max = 0,0
        y = [-1,1]
        for i in y:
            tmp = self.probPosteriori(i,test)
            if tmp>max:
                res,max = i,tmp
        return res,max
if __name__ == '__main__':
    ipt = [[1,'s',-1],[1,'m',-1],[1,'m',1],[1,'s',1],[1,'s',-1],\
           [2,'s',-1],[2,'m',-1],[2,'m',1],[2,'l',1],[2,'l',1],\
           [3,'l',1],[3,'m',1],[3,'m',1],[3,'l',1],[3,'l',-1]]
    t1 = [2,'s']
    print(Solution(ipt).naiveBayesClassfier(t1))


