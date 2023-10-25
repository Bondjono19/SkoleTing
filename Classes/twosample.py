import math
import scipy.stats as stats

class Twosample:

    def __init__(self,n1,x1,s1,n2,x2,s2,alpha):
        self.n1 = n1
        self.x1 = x1
        self.s1 = s1
        self.n2 = n2
        self.x2 = x2
        self.s2 = s2
        self.a = alpha

    def calcTestStatistic(self):
       #pooled standard deviation
       psd = math.sqrt((((self.n1-1)*pow(self.s1,2)+(self.n2-1)*pow(self.s2,2))/(self.n1+self.n2-2)))*math.sqrt((1/self.n1+1/self.n2))

       testStatistic = (self.x1-self.x2)/psd

       return testStatistic
    
    def tableVal(self):
        return stats.t.ppf(1-self.a/2,self.n1+self.n2-2)
    
    def res(self):
        testStatistic = self.calcTestStatistic()
        tableT = self.tableVal()
        tableTminus= tableT*-1
        return str(tableTminus)+"  "+str(testStatistic)+" "+str(tableT)