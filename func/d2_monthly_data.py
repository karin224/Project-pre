import sys
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from d0_makelist import MakeList


def make_monthly_data(filename):
    if(filename[0]=="/"):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename   # get the path included filename
    loca=len(filename)
    for i in range (1,len(filename)+1):       # find the "/" location
        if(filename[-i] == "/"):
            loca = i-1
            break

    FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
    filename_No_Txt = FILENAME.replace(".txt","")
    infile = filename

    tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
    iterator = 0
    SAVENAME = filename_No_Txt+"_monthly.txt"
    print(SAVENAME)
    f = open(SAVENAME, "w+")
    OLD_LIST = MakeList(infile)

##################################
#### 2013
    for i in range(len(OLD_LIST)):
        if(i==0):
            f.write('DATE AQI PM2p5 PM10 SO2 CO NO2 O3_8h\n')
            continue;
#        print(OLD_LIST[i][0])
        if((int(OLD_LIST[i][0])>20131200)&(int(OLD_LIST[i][0])<20140100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140100):
#                f.write("201312 %f %f %f %f %f %f %f" %(tempAqi/iterator) (tempAqi/iterator) )
                f.write("201312 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

##################################
#### 2014    
        if((int(OLD_LIST[i][0])>20140100)&(int(OLD_LIST[i][0])<20140200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140200):
                f.write("201401 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140200)&(int(OLD_LIST[i][0])<20140300)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140300):
                f.write("201402 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140300)&(int(OLD_LIST[i][0])<20140400)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140400):
                f.write("201403 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140400)&(int(OLD_LIST[i][0])<20140500)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140500):
                f.write("201404 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140500)&(int(OLD_LIST[i][0])<20140600)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140600):
                f.write("201405 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140600)&(int(OLD_LIST[i][0])<20140700)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140700):
                f.write("201406 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140700)&(int(OLD_LIST[i][0])<20140800)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140800):
                f.write("201407 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140800)&(int(OLD_LIST[i][0])<20140900)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20140900):
                f.write("201408 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20140900)&(int(OLD_LIST[i][0])<20141000)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20141000):
                f.write("201409 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20141000)&(int(OLD_LIST[i][0])<20141100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20141100):
                f.write("201410 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20141100)&(int(OLD_LIST[i][0])<20141200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20141200):
                f.write("201411 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20141200)&(int(OLD_LIST[i][0])<20150100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20150100):
                f.write("201412 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

##################################
#### 2015

        if((int(OLD_LIST[i][0])>20150100)&(int(OLD_LIST[i][0])<20150200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20150200):
                f.write("201501 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150200)&(int(OLD_LIST[i][0])<20150300)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20150300):
                f.write("201502 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150300)&(int(OLD_LIST[i][0])<20150400)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20150400):
                f.write("201503 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150400)&(int(OLD_LIST[i][0])<20150500)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20150500):
                f.write("201504 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150500)&(int(OLD_LIST[i][0])<20150600)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20150600):
                f.write("201505 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150600)&(int(OLD_LIST[i][0])<20150700)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20150700):
                f.write("201506 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150700)&(int(OLD_LIST[i][0])<20150800)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20150800):
                f.write("201507 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150800)&(int(OLD_LIST[i][0])<20150900)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20150900):
                f.write("201508 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20150900)&(int(OLD_LIST[i][0])<20151000)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20151000):
                f.write("201509 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20151000)&(int(OLD_LIST[i][0])<20151100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20151100):
                f.write("201510 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20151100)&(int(OLD_LIST[i][0])<20151200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20151200):
#                print(tempAqi, iterator)
                f.write("201511 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20151200)&(int(OLD_LIST[i][0])<20160100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1    
            if(int(OLD_LIST[i+1][0])>20160100):
                f.write("201512 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")
             
                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0


##################################
#### 2016

        if((int(OLD_LIST[i][0])>20160100)&(int(OLD_LIST[i][0])<20160200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160200):
                f.write("201601 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160200)&(int(OLD_LIST[i][0])<20160300)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160300):
                f.write("201602 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160300)&(int(OLD_LIST[i][0])<20160400)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160400):
                f.write("201603 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160400)&(int(OLD_LIST[i][0])<20160500)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160500):
                f.write("201604 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160500)&(int(OLD_LIST[i][0])<20160600)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160600):
                f.write("201605 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160600)&(int(OLD_LIST[i][0])<20160700)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160700):
                f.write("201606 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160700)&(int(OLD_LIST[i][0])<20160800)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160800):
                f.write("201607 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160800)&(int(OLD_LIST[i][0])<20160900)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20160900):
                f.write("201608 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20160900)&(int(OLD_LIST[i][0])<20161000)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20161000):
                f.write("201609 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20161000)&(int(OLD_LIST[i][0])<20161100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20161100):
                f.write("201610 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20161100)&(int(OLD_LIST[i][0])<20161200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20161200):
                f.write("201611 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20161200)&(int(OLD_LIST[i][0])<20170100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170100):
                f.write("201612 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

##################################
#### 2017

        if((int(OLD_LIST[i][0])>20170100)&(int(OLD_LIST[i][0])<20170200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170200):
                f.write("201701 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170200)&(int(OLD_LIST[i][0])<20170300)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170300):
                f.write("201702 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170300)&(int(OLD_LIST[i][0])<20170400)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170400):
                f.write("201703 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170400)&(int(OLD_LIST[i][0])<20170500)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170500):
                f.write("201704 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170500)&(int(OLD_LIST[i][0])<20170600)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170600):
                f.write("201705 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170600)&(int(OLD_LIST[i][0])<20170700)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170700):
                f.write("201706 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170700)&(int(OLD_LIST[i][0])<20170800)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170800):
                f.write("201707 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170800)&(int(OLD_LIST[i][0])<20170900)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20170900):
                f.write("201708 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20170900)&(int(OLD_LIST[i][0])<20171000)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20171000):
                f.write("201709 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20171000)&(int(OLD_LIST[i][0])<20171100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20171100):
                f.write("201710 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20171100)&(int(OLD_LIST[i][0])<20171200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20171200):
                f.write("201711 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20171200)&(int(OLD_LIST[i][0])<20180100)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20180100):
                f.write("201712 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

##################################
#### 2018

        if((int(OLD_LIST[i][0])>20180100)&(int(OLD_LIST[i][0])<20180200)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20180200):
                f.write("201801 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        if((int(OLD_LIST[i][0])>20180200)&(int(OLD_LIST[i][0])<20180300)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20180300):
                f.write("201802 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        '''
        if((int(OLD_LIST[i][0])>20180300)&(int(OLD_LIST[i][0])<20180400)):
            tempAqi = tempAqi + float(OLD_LIST[i][1])
            pm2p5 = pm2p5 + float(OLD_LIST[i][2])
            pm10 = pm10 + float(OLD_LIST[i][3])
            so2 = so2 + float(OLD_LIST[i][4])
            co = co + float(OLD_LIST[i][5])
            no2 = no2 + float(OLD_LIST[i][6])
            o3_8h = o3_8h + float(OLD_LIST[i][7])
            iterator = iterator + 1
            if(int(OLD_LIST[i+1][0])>20180200):
                f.write("201803 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" %((tempAqi/iterator), (pm2p5/iterator), (pm10/iterator), (so2/iterator), (co/iterator), (no2/iterator), (o3_8h/iterator)))
                f.write("\n")

                tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0,0,0,0,0,0,0
                iterator = 0

        '''





def main():
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/Aqi_Beijing.txt"
    List_month = make_monthly_data(inputfile)


if __name__=="__main__":
    main()

