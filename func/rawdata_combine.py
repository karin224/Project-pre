import numpy as np

if __name__=="__main__":
    load_file_path_a="/Desktop/group_study/Project-pre/func/test1.txt"
    load_file_path_b="/Desktop/group_study/Project-pre/func/test2.txt"
    load_file_path_c="/Desktop/group_study/Project-pre/func/test3.txt"

    rawData_a=np.loadtxt(load_file_path_a)
    rawData_b=np.loadtxt(load_file_path_b)

    df_01 = np.array(rawData_a)
    df_02 = np.array(rawData_b)

    package = np.hstack([df_01,df_02])

    saving_file = open(saved_file_path_c, 'w')

    for i in range(len(package)):
        for j in range(len(package[i])):
            saving_file.write(str(package[i][j]+"\t")
        saving_file.write('\r\n')
    saving_file.close()

    print(package)

