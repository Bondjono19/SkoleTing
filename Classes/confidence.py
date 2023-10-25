import scipy.stats as stats
import math
import statistics
class Confidence:

    def __init__(self,sampSize,sampMean,popMean,standardDeviation,alpha):
        self.n = sampSize
        self.x = sampMean
        self.µ = popMean
        self.s = standardDeviation
        self.a = alpha
    
    def __init__(self,dataSet,µ,alpha):
        self.s = statistics.stdev(dataSet)
        self.x = sum(dataSet)/len(dataSet)
        self.µ = µ
        self.n = len(dataSet)
        self.a = alpha

    def confInterval(self):
        #table value
        t_table = stats.t.ppf(1-self.a/2,self.n-1)
        #t value calculation
        t_value = (self.x-self.µ)/(self.s/(math.sqrt(self.n)))
        limit = t_table*(self.s/(math.sqrt(self.n)))
        print("Confidence interval is as follows: ")
        print(str(self.x-limit) + " < µ < " + str(self.x+limit))
        print("Where t-table is: " + str(t_table))
        print("And where t-value calculated is: " + str(t_value))
