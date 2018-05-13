from ROOT import gSystem, gROOT
from ROOT import gBenchmark
gBenchmark.Start("All in One")
import sys
import os

INfile = "carbon_copied_data/Aqi_Beijing_day.txt"
BIN_Num_2D = 20
YBIN_Num_2D = 20
oneD_NBins = 100
N_sigma = 5    ## Skiming of txt outof specific sigma region

sys.path.append("/home/soomin/Desktop/group_study/Project-pre/func")
from d1_remake_txt import MakeiTXT
from txt_cut_apply import cut_apply
from d0_Nsigma_skiming import N_sigma_skimming 
INFile = MakeTXT(INfile)
Infile_1 = cut_apply(INFile)
Infile = N_sigma_skimming(Infile_1, N_sigma) 

sys.path.append("/home/soomin/Desktop/group_study/fruit_team/ROOT/Project/functions/rawTxt_Tree_root")
from Raw_text_to_Tree_root import Raw_text_to_Tree_root
To_Tree = Raw_text_to_Tree_root(Infile,".")


#To_Tree = "/Users/leejunho/Desktop/git/My_git/My_temp/n43_VBSWW_LL_TT_TL_lhe/madspin_root_generator/output_madspin_VBSWW_1_small.root"

#print("\n********************************************************************")
#print("** THIS is before cut applied **")
#print("Name_OF_Tree->MakeClass('NAME OF YOUR CODE')")
#print("********************************************************************")
#CUT_SETTING = "root -l " + To_Tree       ###### inside of root interpreter : "treeName"->MakeClass("MyAnalysiscode_nameit")
#os.system(CUT_SETTING)

sys.path.append("/home/soomin/Desktop/group_study/fruit_team/ROOT/Project/functions/rootTree_rootHist/func")
from Tree_to_D1H_Components import Tree_to_D1H_Components
Tree_to_D1H_Components(To_Tree)


from Tree_to_D1H_CutnGenerate_BEIJING_AIR import REGENERATE_TREE_WITH_CUT
#from Tree_to_D1H_CutnGenerate import REGENERATE_TREE_WITH_CUT
NEW_Tree_PATH = REGENERATE_TREE_WITH_CUT(To_Tree,".")



from Tree_to_D2H_Convert import CONVERT_WORKING2D
from Tree_to_D1H_Convert import CONVERT_WORKING
from Tree_to_D1H_Convert_largeBin import CONVERT_WORKING_largeBin
HistROOT_PATH = CONVERT_WORKING(NEW_Tree_PATH,"", D1_NBins=oneD_NBins)
HistROOT_PATH_largeBin = CONVERT_WORKING_largeBin(NEW_Tree_PATH,"")
HistROOT_PATH_2D = CONVERT_WORKING2D(NEW_Tree_PATH,"",NBins=BIN_Num_2D,NYBins=YBIN_Num_2D)
twoD_plot_save = "root -l -q /home/soomin/Desktop/group_study/fruit_team/ROOT/Project/functions/2Dplots_Saver/TwoD_Plot_Saver_default.C\("+"'"+'"'+HistROOT_PATH_2D+'"'+"'"+"\)"
os.system(twoD_plot_save)
os.system("mkdir 2D_defalut")
os.system("mkdir 2D_colz")
os.system("mkdir 2D_surf3")
os.system("mv *defalut_2D.pdf 2D_defalut")
os.system("mv *colz_2D.pdf 2D_colz")
os.system("mv *surf3_2D.pdf 2D_surf3")

twoD_profile_pol_save = "root -l -q /home/soomin/Desktop/group_study/fruit_team/ROOT/Project/functions/2Dplots_Saver/TwoD_profileX_pol_fitter.C\("+"'"+'"'+HistROOT_PATH_2D+'"'+"'"+"\)"
os.system(twoD_profile_pol_save)
os.system("mkdir 2D_profileX_pols")
os.system("mv *profileX_pol_2D.pdf 2D_profileX_pols")

'''
sys.path.append("/home/soomin/Desktop/group_study/fruit_team/ROOT/Project/functions/rootHist_TXT/func")
from D1H_rootHist_TXT_conversion import D1H_roothist_to_txt
from D1H_rootHist_TXT_conversion_largeBin import D1H_roothist_to_txt_largeBin
TXT_FILE_LIST =  D1H_roothist_to_txt(HistROOT_PATH, "")
TXT_FILE_LIST_largeBin =  D1H_roothist_to_txt_largeBin(HistROOT_PATH_largeBin, "")

sys.path.append("/home/soomin/Desktop/group_study/Project-pre/func")
from c1_basic_statistic import *
from c2_basic_histo_plotting import Basic_histo
#from c2_basic_histo_plotting import Basic_histo
from c4_Fit_Poisson_histo_plotting import Fit_Poisson_histo
from c5_single_sample_mean_Zdistribution import Fit_Sample_Gaus_histo
from c5_single_sample_mean_Tdistribution import t_distribution
from c7_single_sample_variance_distribution import Sample_Variance
#for Input_file in TXT_FILE_LIST:
for ij in range(len(TXT_FILE_LIST)):
    print("The file Name is :",TXT_FILE_LIST[ij])
#    MODE = most_frequent_bin(TXT_FILE_LIST[ij]);      print("MODE :",MODE)
#    DATA_RANGE = c1_data_range(TXT_FILE_LIST[ij]);    print("DATA_RANGE :",DATA_RANGE)
#    MEDIAN = c1_median(TXT_FILE_LIST[ij]);            print("MEDIAN :",MEDIAN)
#    Total_ENTRY = c1_total_ENTRY(TXT_FILE_LIST[ij]);  print("Total_ENTRY :",Total_ENTRY)
#    MEAN = c1_mean(TXT_FILE_LIST[ij]);                print("MEAN :",MEAN)
#    VARIANCE = c1_variance(TXT_FILE_LIST[ij]);        print("VARIANCE :",VARIANCE)
#    STD = c1_standard_deviation(TXT_FILE_LIST[ij]);   print("STD :",STD)
#    print("\n")
    Basic_histo(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij])
    Fit_Poisson_histo(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij])
    Fit_Sample_Gaus_histo(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij], exp_Mean_error=10)
#    t_distribution(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij], Show_T=True, Show_sample=True, Show_Gaus=False)
    t_distribution(TXT_FILE_LIST[ij],TXT_FILE_LIST_largeBin[ij], Show_T=True, Show_sample=True, Show_Gaus=True)
    Sample_Variance(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij])
gBenchmark.Show("All in One")
'''
#os.system("rm -rf ROOT_plots")
#os.system("rm -rf ROOT_hist_texts")
os.system("mkdir ROOT_plots")
os.system("mkdir ROOT_hist_texts")
os.system("mv *py.pdf python_plots")
os.system("mv *.pdf ROOT_plots")
os.system("mv *hist.txt ROOT_hist_texts")
os.system("mv *hist_largeBin.txt ROOT_hist_texts")
gBenchmark.Show("All in One")
