from ROOT import gSystem, gROOT
from ROOT import gBenchmark
gBenchmark.Start("All in One")
import sys
import os

os.system("rm -rf ROOT_TGraph_basic")
os.system("rm -rf ROOT_2D_colz")
os.system("rm -rf ROOT_2D_surf3")
os.system("rm -rf ROOT_2D_profileX_pols")
os.system("rm -rf ROOT_files")
os.system("rm -rf ROOT_python_plots")
os.system("rm -rf ROOT_python_hist_texts")

INfile = "/home/Project-pre/data_txt/BEIJING_Aqi/Aqi_Beijing.txt"
BIN_Num_2D = 100    # X bin number of 2D
YBIN_Num_2D = 100   # Y bin number of 2D
oneD_NBins = 100

#### option to draw ###
N_sigma = 5    ## Skiming of txt outof specific sigma region
TGraph_2d_basic = 1 ;   Marker_style = ",2";   poly19_fit =",0"
TH1D_transfer = 1
TH2D_transfer = 1
if TH2D_transfer==1:
    TH2D_colz_surf3 = 1
    TH2D_profileX = 1

PYTHON_HIST = 1  

sys.path.append("/home/Project-pre/func")
from d1_remake_txt import MakeTXT
from txt_cut_apply_py2 import cut_apply
from d0_Nsigma_skiming import N_sigma_skimming
Infile = MakeTXT(INfile)
Infile = cut_apply(Infile)
Infile = N_sigma_skimming(Infile, N_sigma)

sys.path.append("/home/fruit_team/ROOT/Project/functions/rawTxt_Tree_root")
from Raw_text_to_Tree_root import Raw_text_to_Tree_root
To_Tree = Raw_text_to_Tree_root(Infile,".")


#To_Tree = "/Users/leejunho/Desktop/git/My_git/My_temp/n43_VBSWW_LL_TT_TL_lhe/madspin_root_generator/output_madspin_VBSWW_1_small.root"

print("\n********************************************************************")
print("** THIS is before cut applied **")
print("Name_OF_Tree->MakeClass('NAME OF YOUR CODE')")
print("********************************************************************")
CUT_SETTING = "root -l " + To_Tree       ###### inside of root interpreter : "treeName"->MakeClass("MyAnalysiscode_nameit")
os.system(CUT_SETTING)

sys.path.append("/home/fruit_team/ROOT/Project/functions/rootTree_rootHist/func")
from Tree_to_D1H_Components import Tree_to_D1H_Components
Tree_to_D1H_Components(To_Tree)


from Tree_to_D1H_CutnGenerate import REGENERATE_TREE_WITH_CUT
#from Tree_to_D1H_CutnGenerate import REGENERATE_TREE_WITH_CUT
NEW_Tree_PATH = REGENERATE_TREE_WITH_CUT(To_Tree,".")

if TGraph_2d_basic==1:
    TGraph_2D_basic = "root -l -q /home/fruit_team/ROOT/Project/functions/TGraph_saver/Tree_branches_to_vector.C\("+"'"+'"'+NEW_Tree_PATH+'"'+"'"+Marker_style+poly19_fit+"\)"
    os.system(TGraph_2D_basic)
#    os.system("rm -rf ROOT_TGraph_basic")
    os.system("mkdir ROOT_TGraph_basic")
    os.system("mv *basic_*.pdf ROOT_TGraph_basic")

from Tree_to_D2H_Convert import CONVERT_WORKING2D
from Tree_to_D1H_Convert import CONVERT_WORKING
if PYTHON_HIST==1:
    from Tree_to_D1H_Convert_largeBin import CONVERT_WORKING_largeBin
if TH1D_transfer==1:
    HistROOT_PATH = CONVERT_WORKING(NEW_Tree_PATH,"", D1_NBins=oneD_NBins)
    if PYTHON_HIST==1:
        HistROOT_PATH_largeBin = CONVERT_WORKING_largeBin(NEW_Tree_PATH,"")
if TH2D_transfer==1:
    HistROOT_PATH_2D = CONVERT_WORKING2D(NEW_Tree_PATH,"",NBins=BIN_Num_2D,NYBins=YBIN_Num_2D)
    if TH2D_colz_surf3==1:
        twoD_plot_save = "root -l -q /home/fruit_team/ROOT/Project/functions/2Dplots_Saver/TwoD_Plot_Saver_default.C\("+"'"+'"'+HistROOT_PATH_2D+'"'+"'"+"\)"
        os.system(twoD_plot_save)
        #os.system("mkdir ROOT_2D_defalut")
#        os.system("rm -rf ROOT_2D_colz")
#        os.system("rm -rf ROOT_2D_surf3")
        os.system("mkdir ROOT_2D_colz")
        os.system("mkdir ROOT_2D_surf3")
        #os.system("mv *defalut_2D.pdf ROOT_2D_defalut")
        os.system("mv *colz_2D.pdf ROOT_2D_colz")
        os.system("mv *surf3_2D.pdf ROOT_2D_surf3")

    if TH2D_profileX==1:
        twoD_profile_pol_save = "root -l -q /home/fruit_team/ROOT/Project/functions/2Dplots_Saver/TwoD_profileX_pol_fitter.C\("+"'"+'"'+HistROOT_PATH_2D+'"'+"'"+"\)"
        os.system(twoD_profile_pol_save)
#        os.system("rm -rf ROOT_2D_profileX_pols")
        os.system("mkdir ROOT_2D_profileX_pols")
        os.system("mv *profileX_pol_2D.pdf ROOT_2D_profileX_pols")

#os.system("mkdir ROOT_files")
#os.system("mv *.root ROOT_files") 

if PYTHON_HIST != 1:
#    os.system("rm -rf ROOT_files")
    os.system("mkdir ROOT_files")
    os.system("mv *.root ROOT_files")
    os.system("mkdir ROOT_2D_default")
    os.system("mv *_defalut_2D.pdf ROOT_2D_default")
    gBenchmark.Show("All in One")


else:
#    os.system("rm -rf ROOT_files")
    os.system("mkdir ROOT_files")
    os.system("mv *.root ROOT_files")
    os.system("mkdir ROOT_2D_default")
    os.system("mv *_defalut_2D.pdf ROOT_2D_default")
    gBenchmark.Show("All in One")
