import random
import os,sys
from d0_makelist_column import MakeList_column
from c0_READ_PATH_FILE import read_file_name
from d0_Date_editor import PICKING_BRANCH_n_SAVING

class MC_simul:
    def __init__(self):
        pass

    def Make_simulation(self, infilename, EventNum=100):
        Filelist = read_file_name(infilename)
        pick_all = input("Do you want to Make All MC? (Y/N)\n")
        pick_all = pick_all.lower()
        print(" * Input file name :",Filelist[2])
        if(pick_all!="y"):
            Make_MC = PICKING_BRANCH_n_SAVING(Filelist[2])        
            print(" * Tempary produce file :",Make_MC[0])
            print(" * Going to make MC for",Make_MC[1])
            INPUT = Make_MC[0]
        else:
            INPUT = Filelist[2]

        data_col_list = MakeList_column(INPUT)
        sorted_col_list = []
        DATA_LIST = []
        DATA_NAME_LIST = []
        for i in range(len(data_col_list)):
            temp_list = []
            for j in range(len(data_col_list[i])):
                if(j==0):
                    DATA_NAME_LIST.append(data_col_list[i][j])
                    continue
                temp_t = float(data_col_list[i][j])
                temp_list.append(temp_t)
            
            temp_list.sort()
            sorted_col_list.append(temp_list)
#        print(sorted_col_list)

        DATA_LIST.append(DATA_NAME_LIST)
        for i in range(EventNum):
            if(i%1000==0):
                print("Now looping", i,"th event")
            temp_list1 = []
            for j in range(len(sorted_col_list)):
                px = random.random()
                Num = len(sorted_col_list[j])
                float_Num = float(Num)
                prob = 1.0/float_Num
               
                th_num = 0; th_flag = 0
                while(th_flag==0):
                    if(px > (th_num * prob)):
#                    if(0 > (th_num * prob)):
#                    if(1 > (th_num * prob)):
                        th_num = th_num +1
                    else:
                        th_flag = 1
                        #th_num = th_num +1
                if(th_num >= len(sorted_col_list[j])):
                    th_num = len(sorted_col_list[j])-1
                th_num = th_num
                Estimate = (px - float(th_num-1)/float(Num))*float(Num)*(sorted_col_list[j][th_num]-sorted_col_list[j][th_num-1]) + sorted_col_list[j][th_num-1]
                temp_list1.append(Estimate)
#                print(th_num, sorted_col_list[j][th_num-1],Estimate, sorted_col_list[j][th_num] )
            DATA_LIST.append(temp_list1)
#        print(DATA_LIST) 

        Write_MC_File = Filelist[3]+Filelist[0]+"_MC.txt"
        self.Write_list = DATA_LIST
        self.Write_file = Write_MC_File
        #print(self.Write_file)

        if(pick_all!="y"):
            remove_command = "rm -rf " + INPUT
            os.system(remove_command)
            print(" * Removing Tempary file", INPUT)
        self.MakeMCFile_UseRowList()


    def MakeMCFile_UseRowList(self):
        OF = open(self.Write_file, "w+")
        for i in range(len(self.Write_list)):
            for j in range(len(self.Write_list[i])):
                if(j != (len(self.Write_list[i])-1)):
                    str_write = str(self.Write_list[i][j])
                    OF.write("%s " %str_write)
                elif(j == (len(self.Write_list[i])-1)):
                    str_write = str(self.Write_list[i][j])
                    OF.write("%s\n" %str_write)
        OF.close()
        print(" * Write MC file :",self.Write_file)


def main():
    input_file = "Aqi_Beijing_Holi.txt"
    mc = MC_simul()
    mc.Make_simulation(infilename = input_file,EventNum=10000)




if __name__=="__main__":
    main()
