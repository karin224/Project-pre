import math


def d0_exclude_1_mean(LIST):   # NOTE!!!!  Not in counting first element of the list
    TOT = 0.0
    for i in range(len(LIST)):
        if i==0:
            continue
        TOT = TOT + float(LIST[i])
    return (TOT/float(len(LIST)))


def d0_exclude_1_variance(LIST): # NOTE : Not in counting first element of the list
    MEAN = d0_exclude_1_mean(LIST)
    TEMP = 0.0
    for i in range(len(LIST)):
        if i==0:
            continue
        TEMP = TEMP + (float(LIST[i])-MEAN)*(float(LIST[i])-MEAN)
    return  (TEMP/(float(len(LIST))-2.0))

def d0_exclude_1_STD(LIST): # NOTE : Not in counting first element of the list
    import math
    VAR = d0_exclude_1_variance(LIST)
    STD = math.sqrt(float(VAR))
    return STD
