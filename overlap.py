import numpy as np
import math
import matplotlib.pyplot as plt
'''
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

'''  
   
 
def find_overlap(R, d):
    N_HV = round(2*(R/d))
    Area = 0
    for i in range(1,N_HV):
        for j in range(1,N_HV):
            dij = sqrt((i*d)**2+(j*d)**2)
            Area = Area + 2 * R**2 * math.acos(dij/(2*R))
    return Area, dij
   
 

def cal_all(R,No):
   #R = 60 nm
   #d = 1 nm - 65 nm
   overlap_area = []
   ratio = []
    for i in range(1,No):
        d = i * 1e-9; 
        overlap = find_overlap(R,d)
        overlap_area.append(overlap[0])
        ratio.append(overlap[1])
        
      
    return ratio, overlap_area
  
x, multi_fac = cal_all(62e-9, 65)


plt.plot(x,multi_fac, "o--", color = 'black', linewidth= 2)
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
