import numpy as np
import matplotlib.pyplot as plt

def normfun(x,mu,sig):
    pdf = np.exp(-((x-mu)**2)/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return pdf


file1 = open("Aqi_Beijing_day.txt","r")

log_AQI =[]

for line in file1:
    DATE,AQI,PM2p5,PM10,SO2,CO,NO2,O3_8h,DAYS=line.split()
    try:
#        print(AQI)
        if float(AQI)>0:
         #   print(AQI)
            log_AQI.append(np.log10(float(AQI)))
            continue
    except:
        continue
np_AQI = np.array(log_AQI)

#np.histogram(np_AQI,200)


upper_bound = np_AQI.max()
lower_bound = np_AQI.min()
#bins = 200 # init of bins

x = np.arange(lower_bound,upper_bound,0.01)

#print(len(x))
y = normfun(x,np_AQI.mean(),np_AQI.std())

plt.plot(x,y,color = 'g')

plt.hist(np_AQI,bins=72,normed=1)

plt.show()


#print(np_AQI.min(),np_AQI.max())
