import numpy as np
import math
import matplotlib.pyplot as plt

R = 31E-9

multi_fac = []
y = []
for i in range(1,50):
   
    d = 1E-9 * i
    #c = 8 * R**2 * math.acos(d/(2*R)) + 12 * R**2 * math.acos(( (2* d**2)**(1/2)) / (2*R)  )
    if d <2 *R and d > 1.414 * R:
       N = round(2*R/d)-1
       c = 0
       for j in range(1,N):
           c = c + 2 * R**2 * math.acos(d*j/(2*R)) 

       multi_fac.append(((4*c)/(3.14*R*R))-2)
       b = (d/R) 
       y.append(b)

    if d < 2*R and d < 1.414 *R:
       N = round(2*R/d)-1
       c = 0
       for j in range(1,N):
           c = c + 2 * R**2 * math.acos(d*j/(2*R))
       N_d = round(2*R/1.414*d)-1
       e = 0
       for k in range(1,N_d):
           e = e + 2 * R**2 * math.acos(1.414*d*k/(2*R))
       multi_fac.append(((4*(c+e))/(3.14*R*R)))
       b = (d/R) 
       y.append(b)
       

    
#x =  math.acos( 1/2 * R *(2* d**2)**(1/2) )
    #print (x/(3.14*R*R))


plt.plot(y,multi_fac, "o--", color = 'black', linewidth= 2)
#plt.plot(Z_real,Z_imaginary,'o')
#plt.xscale("log")
#plt.yscale("log")
plt.ylabel('Weight factor (k)',fontsize = 15)
plt.xlabel('d/R',fontsize = 15)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
#plt.legend(["Data","Fit"], loc='upper left')
#plt.title("Weight factor vs step size", fontsize = 15)
plt.show()
