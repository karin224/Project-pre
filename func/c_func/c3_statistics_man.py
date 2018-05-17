import numpy

def most_frequent_binN(filename):
    infile = open(filename,"r")
    point = 0.0
    W = 0
    for line in infile:
        binN,ibin,fbin,entry = line.split()
        if(float(entry)>=point):
            point = float(entry)
            IBIN = ibin
            FBIN = fbin
            BINN = binN

    for line in infile:
        _,_,_,entry = line.split()
        if(entry == point):
            W = W + 1

    if(W>=2):
        print("There are",W," mode points!")
        return None
    infile.close()
    return int(BINN)

def n_frequent_bin(filename,n):
    if n>=1:
        print("Second parameter should be smaller than 1!!")
        return None
    most_f = most_frequent_binN(filename)
    list_file = []
    if most_f == None:
        return None
    else:
        infile = open(filename,"r")
    for line in infile:
        binN,ibin,fbin,entry = line.split()
        list_file.append([int(binN),float(ibin),float(fbin),float(entry)])
    # find n% frequent point from most_frequent point to left side
    l=[x[0] for x in list_file]
    i = 0
    n_fre_point_left = 0
    while (most_f-i-1)>=l[0]:
        if (list_file[most_f-i][3]>(n*list_file[most_f][3]))&(list_file[most_f-i-1][3]<=(n*list_file[most_f][3])):
            n_fre_point_left = list_file[most_f-i-1][2]+(list_file[most_f-i-1][2]-list_file[most_f-i-1][1])*(n*list_file[most_f][3]-list_file[most_f-i-1][3])/(list_file[most_f-i][3]-list_file[most_f-i-1][3])
             # n% point = fbin of lower bound + width of bar*((n% entry-lower bar entry)/(upper bar entry-lower bar entry))
            break
        else:
            i = i+1
    
    i = 0
    n_fre_point_right = 0
    while (most_f+i+1)<len(l):
        if (list_file[most_f+i][3]>(n*list_file[most_f][3]))&(list_file[most_f+i+1][3]<=(n*list_file[most_f][3])):
            n_fre_point_right = list_file[most_f+i+1][2]+(list_file[most_f+i+1][2]-list_file[most_f+i+1][1])*(n*list_file[most_f][3]-list_file[most_f+i+1][3])/(list_file[most_f+i][3]-list_file[most_f+i+1][3])
             # n% point = fbin of lower bound + width of bar*((n% entry-lower bar entry)/(upper bar entry-lower bar entry))
            break
        else:
            i = i+1
    #print(len(l))
    result = []
    result.append(n_fre_point_left)
    result.append(n_fre_point_right)
    return result



