import sys,os
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from c0_READ_PATH_FILE import read_file_name
from d0_makelist import MakeList


def getData():
    all_text_path = []
    loadfile = ['.']
    while(loadfile):
        try:
            path = loadfile.pop()
            #print path
            for x in os.listdir(path):
                if os.path.isfile(os.path.join(path,x)):
                    if x[-3:]=="txt":
                        #print path+"/"+x
                        #temp_list = [x,path+"/"+x]
                        all_text_path.append(path+"/"+x)
                else:
                    loadfile.append(os.path.join(path,x))
                    
        except Exception,e:
            pass
            #print str(e) + path
    return all_text_path



def Add_first(texts_path):
    Total_data_list = []
    all_text_path = texts_path
    print("Total involved text data files :", len(all_text_path))
    #print(read_file_name(all_text_path[0]))
    for i in range(len(all_text_path)):
        print(all_text_path[i])
        First_col_write = read_file_name(all_text_path[i])[0]
        #print(First_col_write)
        ROW_LIST = MakeList(read_file_name(all_text_path[i])[2]) 
        for j in range(len(ROW_LIST)):
            if ROW_LIST[j][0] == " ":
                continue
            if ROW_LIST[j][0] == "V1":
                continue
            temp_list = [First_col_write]
            for k in range(len(ROW_LIST[j])):
                temp_list.append(ROW_LIST[j][k])
            Total_data_list.append(temp_list)
    #print(Total_data_list)
    print("Total Entry :", len(Total_data_list))
    return Total_data_list

def Write_into_a_text_file(data_row_list):
    row_list = data_row_list
    Of = open("LA_till_week16.txt", "w+")
    for i in range(len(row_list)):
        for j in range(len(row_list[i])):
            Of.write("%s" %row_list[i][j])
            if(j!=len(row_list[i])-1):
                Of.write(" ")
            if(j==len(row_list[i])-1):
                Of.write("\n")
    Of.close()


def main():
    Texts = getData()
    total_DATA_col_list = Add_first(Texts)
    Write_into_a_text_file(data_row_list=total_DATA_col_list)


if __name__=="__main__":
    main()

