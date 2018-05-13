import numpy as np
from ROOT import TFile,TCanvas,TPad,TH1F

file1 = open("Aqi_Beijing_day.txt","r")

x = []
file_log = open("log_Converted_Data.txt","w")
file_sqrt = open("sqrt_Converted_Data.txt","w")

f1 = TFile("mtxt_to_hist.root","recreate")
c1 = TCanvas("c1","txt to hist",200,10,700,900)

#h1f = TH1F("h1f","hist",500,0,max)
log_AQI = []
sqrt_AQI = []

for line in file1:
    DATE,AQI,PM2p5,PM10,SO2,CO,NO2,O3_8h,DAYS=line.split()
    try:
        if AQI!=0:
            log_AQI.append(np.log10(float(AQI)))
            sqrt_AQI.append(np.sqrt(float(AQI)))
#        file_log.write(DATE+" "+str(log_AQI)+" "+PM2p5+" "+PM10+" "+SO2+" "+CO+" "+NO2+" "+O3_8h+" "+DAYS+"\n")
 #       file_sqrt.write(DATE+" "+str(sqrt_AQI)+" "+PM2p5+" "+PM10+" "+SO2+" "+CO+" "+NO2+" "+O3_8h+" "+DAYS+"\n")
        continue
    except:
  #      file_log.write(DATE+" "+AQI+" "+PM2p5+" "+PM10+" "+SO2+" "+CO+" "+NO2+" "+O3_8h+" "+DAYS+"\n")
   #     file_sqrt.write(DATE+" "+AQI+" "+PM2p5+" "+PM10+" "+SO2+" "+CO+" "+NO2+" "+O3_8h+" "+DAYS+"\n")
        continue
np_AQI = np.array(log_AQI)
#print(type(np_AQI.min()))
print(float(np_AQI.min()),float(np_AQI.max()))
h1f = TH1F("h1f","hist_sqrt",200,0,23)
h1f2 = TH1F("h1f2","hist_log",200,0,float(np_AQI.max()))
print(len(sqrt_AQI))
for i in sqrt_AQI:
    h1f.Fill(i)
   

for j in log_AQI:
    h1f2.Fill(j)

h1f.Draw()
h1f2.Draw()
c1.Update()
f1.Write()
f1.Close()

       
file_log.close()
file_sqrt.close()


