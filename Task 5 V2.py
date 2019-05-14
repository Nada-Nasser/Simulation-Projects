import numpy as np

ServerAvailTimeArray = []
SystemSpaceAvailTimeArray = []
ArrivalTime = []
Sales = 0
WaitingCost = 0
Profit = [0 , 0]

ArrivalTime.insert(0 ,0)

c = 0
while(c < 3):
    c = c + 1
    if(c==1):
        ServerAvailTimeArray = [0 , 0]
        SystemSpaceAvailTimeArray = [0 , 0 , 0]
    else:
        ServerAvailTimeArray = [0 ,0,0,0,0,0]
        SystemSpaceAvailTimeArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    nCustomers = 10000
    i = 0
    while( i < nCustomers):
        i = i + 1
        IAT = np.random.normal(1.5 , 0.15)
        ArrivalTime.insert ( i , ArrivalTime[i-1] + IAT)
        
        if(ArrivalTime[i] > 10*60):
            break
        
        StartTime = 0
        #Seize 
        # Calculate The Start_Entrance Time and which space will use
        MinTime = min(SystemSpaceAvailTimeArray)
        if(ArrivalTime[i] > MinTime):
            Start_Entrance = ArrivalTime[i]
        else:
            Start_Entrance = MinTime
        SpaceN = SystemSpaceAvailTimeArray.index(MinTime)
        
        if(Start_Entrance > ArrivalTime[i]):
            continue
        
        Sales = Sales + 22
        
        #Seize 
        # Calculate The Server Start Time and which space will use
        MinTime = min(ServerAvailTimeArray)
        if(ArrivalTime[i] > MinTime):
            StartTime = ArrivalTime[i]
        else:
            StartTime = MinTime
        SreverN = ServerAvailTimeArray.index(MinTime)
        
        WaitingTime = StartTime - ArrivalTime[i]
        WaitingCost = WaitingCost + (10/60)
        
        Service_Time = np.random.normal(1 , 6)
        CompletionTime = StartTime + Service_Time
        
        #Release 
        ServerAvailTimeArray.insert(SreverN , CompletionTime)
        SystemSpaceAvailTimeArray.insert(SpaceN , CompletionTime)
    
    Profit.insert(c , Sales - WaitingCost)
    Sales = 0
    WaitingCost = 0
    
    if(c==1):
        Profit.insert( c ,  Profit[c] - 200 - (20 * 3 * 10))
    else:
        Profit.insert( c ,  Profit[c] - 2000 - (20 * 6 * 10))
        
print(Profit[1])
print(Profit[2])



if Profit[1] > Profit[2]:
	print('\nuse the first configuration')
else:
	print('\nuse the second configuration')
        
    