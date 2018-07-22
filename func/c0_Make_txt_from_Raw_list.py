import os,sys

def MAKE_TXT(ROW_LIST,output_file_name="TTT.txt"):
    Of = open(output_file_name,"w+")
    for i in range(len(ROW_LIST)):
        for j in range(len(ROW_LIST[i])):
            Of.write("%s" %ROW_LIST[i][j])
            if(j!=len(ROW_LIST[i])-1):
                Of.write(" ")
            if(j==len(ROW_LIST[i])-1):
                Of.write("\n")
    Of.close()


