
def min_max_range(LIST):
    MAX = float(LIST[1])
    MIN = float(LIST[1])
    for i in range(len(LIST)):
        if i==0:
            continue
        if(float(LIST[i])>MAX):
            MAX = float(LIST[i])
        if(float(LIST[i])<MIN):
            MIN = float(LIST[i])
    L_lim = MIN - (MAX-MIN)*0.05
    H_lim = MAX + (MAX-MIN)*0.05
    return [MIN, MAX, L_lim, H_lim]

def main():
    Temp_list = ['this','0','1','2',3,4,5,5,6,6,3.5,7.8,10,2,3,4.5]
    out_list = min_max_range(Temp_list)
    print(out_list)

if __name__=="__main__":
    main()

