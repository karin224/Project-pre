#Author : JUNHO LEE
#Required : n1p1>=5, and n1(1-p1)>=5, n>30
import math
from statsmodels.stats import proportion
#sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
#from c1_basic_statistic import *

# note that :: n1p1>=5, and n1(1-p1)>=5, n>30
#http://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportions_ztest.html
def bothSide_hypothesis(Proportion=0.1, event_num=100, test_proportion=0.1):
    # this is Z test for proportion test
    # returns [self calculated Zc, Zc from statsmodels, p-value from statsmodels corresponding Zc, Sample_proportion, Test_proportion]
    # H0 : P1 = Test_proportion
    # H1 : P1 != Test_proportion

    Prop = Proportion
    
    Event_num = float(event_num)
    Std = math.sqrt(Prop*(1-Prop)/Event_num) 
    Zc = (Prop-test_proportion)/math.sqrt(Prop*(1-Prop)/Event_num)

    Success = event_num*Prop; Success = int(Success); #print(type(Success)); print(Success)
    Ztest = proportion.proportions_ztest(int(Success),int(event_num),value=test_proportion, alternative='two-sided')
#    Ztest = proportion.proportions_ztest(10,100,0.09)
    LIST = [Zc, Ztest[0], Ztest[1], Prop, test_proportion]
    return LIST



def main():
    twoSigma_region = bothSide_hypothesis(Proportion=0.0315, event_num = 7000, test_proportion=0.03)
    print(twoSigma_region)    

if __name__ == "__main__":
    main()




