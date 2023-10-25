from scipy import stats
import math
import statistics


class Anova:

    def __init__(self,alpha,data):
        self.alpha = alpha
        self.data = data
        for i in range(len(data)):
            for h in range(len(data[i])):
                data[i][h]= float(data[i][h])
    
    def anova(self):
        liste = list()
        bN = 0
        sN = 0
        totalSum = 0
        count = 0
        for i in range(len(self.data)):
            liste.append(sum(self.data[i])/len(self.data[i]))
            for h in range(len(self.data[i])):
                totalSum += self.data[i][h]
                count = count + 1
        avg = totalSum / count 
        for i in range(len(self.data)):
            bN += len(self.data[i])
        k = len(self.data)
        if len(self.data) == 0:
            return "invalid data, need 2 or more data groups"
        elif len(self.data) == 1:
            return "invalid data, need 2 or more data groups"
        elif len(self.data) == 2:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1])
        elif len(self.data) == 3:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2])
        elif len(self.data) == 4:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2],self.data[3])
        elif len(self.data) == 5:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4])
        elif len(self.data) == 6:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5])
        elif len(self.data) == 7:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],self.data[6])
        elif len(self.data) == 8:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],self.data[6],self.data[7])
        elif len(self.data) == 9:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],self.data[6],self.data[7],self.data[8])
        elif len(self.data) == 10:
            f_ratio, p_value = stats.f_oneway(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],self.data[6],self.data[7],self.data[8],self.data[9])
        f_table = stats.f.ppf(1- self.alpha,k-1,bN-k)
        t_table = stats.t.ppf(1-self.alpha/2,bN-k)
        print("calculated f value: " + str(f_ratio))
        print("Table fvalue: " + str(f_table))

        #LSD intervaller: MSresiduals
        #sumsquare
        newSum = 0
        for i in range(len(self.data)):
            sN = len(self.data[i])
        for i in range(len(liste)):
           newSum = newSum + pow((liste[i]-avg),2)*sN
        Df = len(self.data)-1
        #meansqure
        ms = newSum / Df
        #meanssquareresiduals
        msRes = ms/f_ratio
        #lsd
        lsd = ((math.sqrt(2))/2)*t_table*(math.sqrt((msRes/sN)))

        return lsd, f_ratio, f_table, liste
        
        for i in range(len(liste)):
            print("Interval group: " + str(i+1))
            print(liste[i]+lsd)
            print(liste[i]-lsd)



    def sampStDev(self):
        return statistics.stdev(self.data)
    
    def sampVar(self):
        return statistics.variance(self.data)
    
    def twoSamp(self):
        df = len(self.data[0]+self.data[1]-2)
        t_value, p_value = stats.ttest_ind(self.data[0],self.data[1])
        t_table = stats.t.ppf(1-self.alpha/2,df)
        print("calculated t-value is: " + str(t_value))
        print("Table t-value is: " + str(t_table))