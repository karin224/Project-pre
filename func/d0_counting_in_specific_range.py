

def Counting(LIST,RANGE):
    counts = 0    
    for i in range(len(LIST)):
        if i ==0:
            continue
        if( (float(LIST[i])>=float(RANGE[0])) & (float(LIST[i])<float(RANGE[1]))):
            counts = counts+1
    return float(counts)

def main():
    temp_list = ["this",'0','1','2',3,4,5,5,6,6,3.5,7.8,10,2,3,4.5]
    counts = Counting(temp_list,[0,7.5])
    print(counts)


if __name__=="__main__":
    main()
