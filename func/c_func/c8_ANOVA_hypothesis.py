import sys
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from c2_basic_histo_plotting import *
from scipy.stats import f as F_TEST
#    ...This is Anova's oneway, Compeletly Randomized designed, same event number for each process...
#    ...The Null hypo is 'mu0 == mu1 == .. == muN' ...
#    ...The alternative is 'at least one of the mean value of the sample is differ with others' ...

#  sample_1  ...    sample_l 
#     A1  A2  A3 .... Al    SUM  AVERAGE
# B1  x11 x21 x31 ... xl1   Tl1   xl1_bar
# B2  x12 x22 x32 ... xl2   Tl2   xl2_bar
# .   ..  ..  ..  ... ...   ...    ...
# Bm  x1m x2m x3m ... xlm   Tlm   xlm_bar
#SUM  T1  T2  T3  ...  Tl    T
#AVE x1_bar .. .. .. xl_bar       x_bar_bar



# recommand to use "*largeBin.txt"
def Anova_oneway_Random_sameE(filelist=[], alpha=0.05): 
    # return [alpha, p_value, LEVEL(kinds of samples tested), Sample's Event NUMBER for each sample, block_number]

    # ENTRY is total block number, M, for this case 
    if(len(filelist) <= 2):
        print("...File number is lower than 2, recheck or try with Ztest/Ttest...")
        return 0

    FILENAME = []
    filename_No_Txt = []
    for j in range(len(filelist)):
        if(filelist[j][0]=="/"):
            filelist[j] = filelist[j]
        else:
            filelist[j] = os.getcwd() + "/" + filelist[j]   # get the path included filename
        loca=len(filelist[j])
        for i in range (1,len(filelist[j])+1):       # find the "/" location
            if(filelist[j][-i] == "/"):
                loca = i-1
                break
        FILENAME.append(filelist[j].replace(filelist[j][:-loca],""))   # this is the shorten filename
        filename_No_Txt.append(FILENAME[j].replace(".txt",""))
        
    ENTRY = c1_total_ENTRY(filelist[0]); ## M == ENTRY
    for i in range(len(filelist)):
        if (int(c1_total_ENTRY(filelist[i])) != ENTRY):
            print("...ERROR, sample size different between samples ...")
            return 0
    block_num = ENTRY

    NUM = len(filelist) * block_num; 
    Tot_sample = []
    Tot_sum = 0
    for i in range(len(filelist)):
        Tot_sample.append(c1_mean(filelist[i])*c1_total_ENTRY(filelist[i]))
        Tot_sum = Tot_sum + c1_mean(filelist[i])*c1_total_ENTRY(filelist[i])
    CT = Tot_sum*Tot_sum/NUM; 

    Square_sum = 0
    for i in range(len(filelist)):
        Square_sum = Square_sum + c1_square_sum(filelist[i])
    SST = Square_sum - CT;    #print(SST)
    sum_of_T_square = 0   # this is "sum_of_T_A_square"
    for i in range(len(Tot_sample)):
        sum_of_T_square = sum_of_T_square + Tot_sample[i]*Tot_sample[i]
    SSB = sum_of_T_square/block_num - CT;    #print(SSB)
    SSW = SST - SSB
    
    MSB = SSB/(len(filelist)-1);  #print(MSB)
    MSW = SSW/(len(filelist)*(block_num-1)); #print(MSW)
    dfB = len(filelist)-1
    dfW = len(filelist)*(block_num-1)
    F_Ratio = MSB/MSW; #print(F_Ratio)

    print("There are totaly", len(filename_No_Txt), "levels")
    for i in range(len(filename_No_Txt)):
        print("Level : ", filename_No_Txt[i])  
    print("Sample number : ", ENTRY)
    print("Block number : ", block_num)

    p_value = F_TEST.cdf(F_Ratio,dfB,dfW); #print(p_value)
    p_value = 1-p_value
    return [alpha, p_value, len(filelist), ENTRY, block_num]
    # "p_value < alpha" means: reject H0, accept alternative H1
    #https://stackoverflow.com/questions/21494141/how-do-i-do-a-f-test-in-python


def Anova_twoWay_Randomized_Block(filelist=[],block_num='', alpha=0.05):
    #   A1 A2 A3 ... (level, one sample for a column Ai)
    # B1 
    # B2
    # .
    # .
    # (Block)

    if(len(filelist) <= 2):
        print("...File number is lower than 2, recheck or try with Ztest/Ttest...")
        return 0
    FILENAME = []
    filename_No_Txt = []
    for j in range(len(filelist)):
        if(filelist[j][0]=="/"):
            filelist[j] = filelist[j]
        else:
            filelist[j] = os.getcwd() + "/" + filelist[j]   # get the path included filename
        loca=len(filelist[j])
        for i in range (1,len(filelist[j])+1):       # find the "/" location
            if(filelist[j][-i] == "/"):
                loca = i-1
                break
        FILENAME.append(filelist[j].replace(filelist[j][:-loca],""))   # this is the shorten filename
        filename_No_Txt.append(FILENAME[j].replace(".txt",""))

    ENTRY = c1_total_ENTRY(filelist[0])
    for i in range(len(filelist)):
        if (int(c1_total_ENTRY(filelist[i])) != ENTRY):
            print("...ERROR, sample size different between samples ...")
            return 0
    if(block_num==''):
        block_num = ENTRY
    BL = c1_data_range(filelist[0])[0]
    BH = c1_data_range(filelist[0])[1]
    for i in range(len(filelist)):
        if (c1_data_range(filelist[i])[0]) < BL :
            BL = (c1_data_range(filelist[i])[0])
        if (c1_data_range(filelist[i])[1]) > BH :
            BH = (c1_data_range(filelist[i])[1])
#    print(BL,BH)

    


    NUM = len(filelist) * block_num;
    Tot_sample = []
    Tot_sum = 0
    for i in range(len(filelist)):
        Tot_sample.append(c1_mean(filelist[i])*c1_total_ENTRY(filelist[i]))
        Tot_sum = Tot_sum + c1_mean(filelist[i])*c1_total_ENTRY(filelist[i])
    CT = Tot_sum*Tot_sum/NUM;
    Square_sum = 0
    for i in range(len(filelist)):
        Square_sum = Square_sum + c1_square_sum(filelist[i])
    SST = Square_sum - CT;    #print(SST)
    sum_of_T_A_square = 0
    for i in range(len(Tot_sample)):
        sum_of_T_A_square = sum_of_T_A_square + Tot_sample[i]*Tot_sample[i]
#    SSB = sum_of_T_A_square/block_num - CT;



    #SSAB 



def main():
#    FLIST = ["/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re_tree_cut_Aqi_Beijing_Holi_re_f_SO2_hist.txt",
#             "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re_tree_cut_Aqi_Beijing_Holi_re_f_AQI_hist.txt",
#             "../data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re_tree_cut_Aqi_Beijing_Holi_re_f_CO_hist.txt"]
#    FLIST = ["../data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re_tree_cut_Aqi_Beijing_Holi_re_f_CO_hist.txt","../data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re_tree_cut_Aqi_Beijing_Holi_re_f_CO_hist.txt","../data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re_tree_cut_Aqi_Beijing_Holi_re_f_CO_hist.txt"]
    FLIST = ["hist2_hist.txt","hist1_hist.txt","hist2_hist.txt"]
#    FLIST = ["gaus300_1.txt","gaus300_2.txt","gaus300_3.txt"]

    One_Anova = Anova_oneway_Random_sameE(filelist = FLIST)
    Two_Anova = Anova_twoWay_Randomized_Block(filelist = FLIST)
    print(One_Anova)

if __name__=="__main__":
    main()
