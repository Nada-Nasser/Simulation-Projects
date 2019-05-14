import random

demand = 0
shortest_cost = 0
holding_cost = 0
sales = 0
profit = 0
#To start Ordering 2 PCs per week
avalible = 2
nPCs = 2

strNum = input("Enter The number of Weeks :\n")
nWeeks = int(strNum)

for j in range (2):
    for i in range(nWeeks):
        tempdemand = random.uniform(0,1)
        if  0 <= tempdemand < 0.2:
            demand = 0
        elif 0.2 <= tempdemand < 0.6:
            demand = 1 
        elif 0.6 <= tempdemand < 0.8:
            demand = 2 
        elif 0.8 <= tempdemand < 0.9:
            demand = 3 
        elif 0.9 <= tempdemand < 1:
            demand = 4
        
        if(demand > avalible):
            shortest_cost = (demand - avalible)*50
            holding_cost = 0
            sales = avalible
        elif(demand < avalible):
            shortest_cost = 0
            holding_cost = (avalible - demand)*100
            sales = demand
        else:
            shortest_cost = 0
            holding_cost = 0
            sales = avalible
        
        profit = profit + ((sales*450) - (shortest_cost + holding_cost))
        avalible = avalible + nPCs - sales
        
    average_Profit = profit/nWeeks
    print("Average of your Profit when you Order " , nPCs , " is = " 
          , average_Profit , "\n\n")
    nPCs = nPCs -1
    avalible = nPCs
    profit = 0
    
    
    
    
    
    
    