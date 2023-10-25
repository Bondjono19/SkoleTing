from Classes.owanova import Anova
from Classes.confidence import Confidence
from Classes.twosample import Twosample

obj = Twosample(25,72.9,2.5,25,70.8,2.8,0.05)

print(obj.res())

obj2 = Anova(0.05,[[12,8,11,17,16,15],[5,9,2,0,1,3],[6,10,5,9,8,6]])

obj2.anova()

obj3 = Confidence([5460,5900,6090,6310,7160,8440,9930],5475,0.01)

obj3.confInterval()