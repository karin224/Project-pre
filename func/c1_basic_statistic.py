#Author : Junho LEE

def bin_num(filename):
    infile = open(filename,"r")
    ii = 0
    for line in infile:
        ii = ii + 1
    infile.close()
    return ii

def most_frequent_bin(filename):
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
    RLIST = []; RLIST.append(float(IBIN)); RLIST.append(float(FBIN))
    LIST = []
    LIST.append(BINN+"th bin"); LIST.append(RLIST); LIST.append(point)
#    print(LIST)
    infile.close()
    return LIST



def c1_median(filename):
    ENTRY = c1_total_ENTRY(filename)
    infile = open(filename,"r")

    Entry = 0.0
    for line in infile:
        point = 0
        binN,ibin,fbin,entry = line.split()
        if(Entry<ENTRY/2):
            point = point + 1
        Entry = Entry + float(entry)
        if(Entry>ENTRY/2):
            point = point + 1
        if(point == 2):
            break
    RANGE = []
    RANGE.append(float(ibin)); RANGE.append(float(fbin))
    MEDIAN = []
    MEDIAN.append(binN+"th bin")
    MEDIAN.append(RANGE)
#    print(MEDIAN)
    infile.close()
    return(MEDIAN)


def c1_data_range(filename):
    infile = open(filename,"r")
    DATA_RANGE = []
    Init = 0
    Final = 1
    count = len(open(filename,'rU').readlines())
    Num = 0
    for line in infile:
        Num = Num + 1
        _,ibin,fbin,entry = line.split()
        if( (Init == 0) &(float(entry) > 0.0)):
            Start_point = ibin
            Init = 1
        if((float(entry) == 0.0) & (Final ==0)):
            End_point = ibin
        if((float(entry) > 0.0)):
            Final = 0
        else:
            Final = 1
        if((Num == count) & (entry !=0)):
            End_point = fbin
    DATA_RANGE.append(float(Start_point))
    DATA_RANGE.append(float(End_point))
 
#    print(DATA_RANGE)
    infile.close()
    return DATA_RANGE




def c1_total_ENTRY(filename):
    infile = open(filename,"r")
    LEntry = []
    Total_Entry = 0
    for line in infile:
        _, _, _, entry = line.split()
        LEntry.append(float(entry))
        Total_Entry = Total_Entry + float(entry)    
#    print(" Total Entry Number =",int(Total_Entry),"!!!!")
    infile.close()
    return Total_Entry




def c1_mean(filename):
    import os
    infile = open(filename,"r")    

    BinN = []
    LIBin = []
    LFBin = []
    LMBin = []     #List of middle Bin
    LEntry = []
    Total_Entry = 0
    for line in infile:
        binN, xaxis0, xaxis1, entry = line.split()
        BinN.append(int(binN))
        LIBin.append(float(xaxis0))
        LFBin.append(float(xaxis1))
        LMBin.append(float(xaxis0)+((float(xaxis1) - float(xaxis0)))/2)
        LEntry.append(float(entry))    
        Total_Entry = Total_Entry + float(entry)

    med = 0
    for i in range(len(LMBin)):
        med = med + LEntry[i]*LMBin[i]
    MEAN = med/Total_Entry
#    print(" Mean Value =",MEAN,"!!!!")
    infile.close()
    return MEAN

def c1_square_sum(filename):
    import os
    infile = open(filename,"r")
    BinN = []
    LIBin = []
    LFBin = []
    LMBin = []     #List of middle Bin
    LEntry = []
    Total_Entry = 0
    for line in infile:
        binN, xaxis0, xaxis1, entry = line.split()
        BinN.append(int(binN))
        LIBin.append(float(xaxis0))
        LFBin.append(float(xaxis1))
        LMBin.append(float(xaxis0)+((float(xaxis1) - float(xaxis0)))/2)
        LEntry.append(float(entry))
        Total_Entry = Total_Entry + float(entry)
    Square_Sum = 0
    for i in range(len(LMBin)):
        if(LEntry[i] == 0.0):
            continue
        else:
            deno = float(LFBin[i]-LIBin[i])/float(LEntry[i])
            for j in range((int(LEntry[i]))):
                deno_m = float(LIBin[i]) + deno*(2*j+1)/2
                Square_Sum = Square_Sum + deno_m*deno_m
    infile.close()
    return Square_Sum


def c1_variance(filename):    # actually, this is variance of a sample from population.
    import os
    infile = open(filename,"r")
    BinN = []
    LIBin = []
    LFBin = []
    LMBin = []     #List of middle Bin
    LEntry = []
    Total_Entry = 0
    for line in infile:
        binN, xaxis0, xaxis1, entry = line.split()
        BinN.append(int(binN))
        LIBin.append(float(xaxis0))
        LFBin.append(float(xaxis1))
        LMBin.append(float(xaxis0)+((float(xaxis1) - float(xaxis0)))/2)
        LEntry.append(float(entry))   
        Total_Entry = Total_Entry + float(entry)

    MEAN = c1_mean(filename)
    med_var = 0
    '''
    for i in range(len(LMBin)):
        for j in range((int(LEntry[i]))):
            med_var = med_var + (LMBin[i] - MEAN)*(LMBin[i] - MEAN)
    '''
    for i in range(len(LMBin)):
        if(LEntry[i] == 0.0):
            continue
        else:
            deno = float(LFBin[i]-LIBin[i])/float(LEntry[i])
            for j in range((int(LEntry[i]))):
                deno_m = float(LIBin[i]) + deno*(2*j+1)/2
                med_var = med_var+(deno_m - MEAN)*(deno_m - MEAN)
    

    VAR = med_var / (Total_Entry-1)

#    print(" Variance Value =",VAR,"!!!!")
    infile.close()
    return VAR




def c1_standard_deviation(filename):
    import os
    import math

    VAR = c1_variance(filename) 
    STD = math.sqrt(VAR)

#    print(" Standard Deviation Value =",STD,"!!!!")
    return STD


def c1_sample_standard_error_of_mean(filename):
    import os
    import math
    STD = c1_standard_deviation(filename)
    TOT = c1_total_ENTRY(filename)
    SSEM = STD/(math.sqrt(TOT))

    return SSEM




