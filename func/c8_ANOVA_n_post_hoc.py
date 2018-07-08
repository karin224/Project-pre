import sys, os
import scipy.stats as stats
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
from statsmodels.stats.libqsturng import psturng
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from d0_makelist_column import MakeList_column

# Infile format :: Two column on a file, and take multiple files as input, in shape of list
#Date Object
#20180101 10
#20180102 11
#   .     .
#   .     .


def ANOVA(infile_list):
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html
    #print("test") 
    ANOVA_list = []
    for i in range(len(infile_list)):
        temp_list = MakeList_column(infile_list[i])[1]
        temp_list2 = []
        for j in range(len(temp_list)):
            if j == 0 :
                continue
            temp_list2.append(float(temp_list[j]))
        #print(temp_list2)
        ANOVA_list.append(temp_list2)
    #print(len(ANOVA_list))
    Free_between = len(ANOVA_list) -1 
    Free_within = 0
    for i in range(len(ANOVA_list)):
        Free_within = Free_within + (len(ANOVA_list[i])-1)
    RES = stats.f_oneway(ANOVA_list[0],ANOVA_list[1],ANOVA_list[2],ANOVA_list[3])
    #print(RES)
    return [RES,Free_between,Free_within]
    #print(RES)

def Post_hoc(infile_list,alpha=0.05):
#http://cleverowl.uk/2015/07/01/using-one-way-anova-and-tukeys-test-to-compare-data-sets/
#https://stackoverflow.com/questions/16049552/what-statistics-module-for-python-supports-one-way-anova-with-post-hoc-tests-tu
#alpha : The significance level is the probability of rejecting the null hypothesis when it is true
#P-values are the probability of obtaining an effect at least as extreme as the one in your sample data, assuming the truth of the null hypothesis.
    ANOVA_list = []
    for i in range(len(infile_list)):
        temp_list = MakeList_column(infile_list[i])[1]
        temp_list2 = []
        for j in range(len(temp_list)):
            if j == 0 :
                continue
            temp_list2.append(float(temp_list[j]))
        #print(temp_list2)
        ANOVA_list.append(temp_list2)    
    Name_list = []
    list_1996 = ANOVA_list[0]; #name_1996= []
    for i in range(len(list_1996)):
        Name_list.append("1996-2000")
    list_2001 = ANOVA_list[1]; #name_2001= []
    for i in range(len(list_2001)):
        Name_list.append("2001-2005")
    list_2006 = ANOVA_list[2]; #name_2006= []
    for i in range(len(list_2006)):
        Name_list.append("2006-2011")
    list_2012 = ANOVA_list[3]; #name_2012= []
    for i in range(len(list_2012)):
        Name_list.append("2012-2017")
    Num_list = []
    for i in range(len(ANOVA_list)):
        for j in range(len(ANOVA_list[i])):
            Num_list.append(ANOVA_list[i][j])
    #print(len(Name_list),len(Num_list))
    mc = MultiComparison(Num_list,Name_list)
    result = mc.tukeyhsd(alpha)
 
    print(result)
    print(mc.groupsunique)
    return result

def Tukey_p_value(result_from_tukey):
    #print(result_from_tukey.meandiffs)
    P_value = psturng(np.abs(result_from_tukey.meandiffs / result_from_tukey.std_pairs), len(result_from_tukey.groupsunique), result_from_tukey.df_total)
    print(P_value)

def main():
    inputfile_list = ["PM2p5_1996_2000.txt","PM2p5_2001_2005.txt","PM2p5_2006_2011.txt","PM2p5_2012_2017.txt"]
    ANO = ANOVA(infile_list=inputfile_list)
    print(ANO)
    result = Post_hoc(infile_list=inputfile_list,alpha=0.01)
    Tukey_p_value(result)

if __name__=="__main__":
    main()



