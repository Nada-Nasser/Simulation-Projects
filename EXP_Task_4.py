import random
import numpy as np
from scipy.stats import expon

nCustomers = 0
arrivalTime = []
CompletionTime = []
startTime = 0

TotalWaitingTime = 0
MaxWaitingTime   = 0
nWaits  = 0
nWaitsM = 0

ATM1 = []
ATM2 = []
ATM3 = []

arrivalTime.insert(0 , 0)
CompletionTime.insert(0 , 0)
ATM1.insert(0 , 0)
ATM2.insert(0 , 0)
ATM3.insert(0 , 0)

WaitingTime = 0

#IAT =[]
# generate Inter Arrival Time :-
IAT = expon.rvs(scale=1,loc=0,size=11)
ST1 = 0
ST2 = 0
ST3 = 0

while(nCustomers < 10):
    nCustomers = nCustomers + 1
    # ArrivalTime :
    #IAT = expon.rvs(scale=1,loc=0,size=1)
    arrivalTime.insert(nCustomers , arrivalTime[nCustomers-1] + IAT[nCustomers])
    
    # startTime :
    if(arrivalTime[nCustomers] >= min(ATM1[nCustomers-1] , ATM2[nCustomers-1] ,
                                  ATM3[nCustomers-1])):
        startTime = arrivalTime[nCustomers]
    else:
        startTime = min(ATM1[nCustomers-1] , ATM2[nCustomers-1] , 
                    ATM3[nCustomers-1])
  
    # WaitingTime
    WaitingTime = startTime - arrivalTime[nCustomers]
    TotalWaitingTime = TotalWaitingTime + WaitingTime
    if(WaitingTime > 0):
        nWaits = nWaits + 1
    if(WaitingTime > 1):
        nWaitsM = nWaitsM + 1
    if(WaitingTime > MaxWaitingTime):
        MaxWaitingTime = WaitingTime
    
    # Generate service time(ST) :
    ST = 0
    ATMUsed = min(ATM1[nCustomers-1] , ATM2[nCustomers-1] , ATM3[nCustomers-1])
    if (ATMUsed == ATM1[nCustomers-1]):
        temp = random.uniform(0, 1)
        ST =  2 + temp * ( 4 - 2 )
        ST1 = ST1 + ST
    elif (ATMUsed == ATM2[nCustomers-1]):
        ST = random.triangular(2, 4, 3.3)
        ST2 = ST2 + ST
    elif (ATMUsed == ATM3[nCustomers-1]):
        ST = np.random.normal(3 , 0.5)
        ST3 = ST3 + ST
        
    #CompletionTime :
    CompletionTime.insert(nCustomers , startTime + ST)
    SystemTime = CompletionTime[nCustomers] +  arrivalTime[nCustomers]
    
    #Update the available time for each ATM :
    if (ATMUsed == ATM1[nCustomers-1]): 
        ATM1.insert(nCustomers , CompletionTime[nCustomers])
        ATM2.insert(nCustomers , ATM2[nCustomers-1])
        ATM3.insert(nCustomers , ATM3[nCustomers-1])
    elif (ATMUsed == ATM2[nCustomers-1]):
        ATM2.insert(nCustomers , CompletionTime[nCustomers])    
        ATM1.insert(nCustomers , ATM1[nCustomers-1])        
        ATM3.insert(nCustomers , ATM3[nCustomers-1])
    elif (ATMUsed == ATM3[nCustomers-1]):
        ATM3.insert(nCustomers , CompletionTime[nCustomers])
        ATM1.insert(nCustomers , ATM1[nCustomers-1])
        ATM2.insert(nCustomers , ATM2[nCustomers-1])


print("\nAverage waiting Time :  ", TotalWaitingTime/10)
print("\nThe probabilty of Waiting :  ", nWaits/10)
print("\nThe probabilty of Waiting more than one M :  ", nWaitsM/10)
print("\nthe maximum Waiting Time : ", MaxWaitingTime )
print("\nutilization of the 1st ATM : " , (ST1 / CompletionTime[10-1])*100 , "%")
print("\nutilization of the 2nd ATM : " , (ST2 / CompletionTime[10-1])*100 , "%")
print("\nutilization of the 3rd ATM : " , (ST3 / CompletionTime[10-1])*100 , "%")



