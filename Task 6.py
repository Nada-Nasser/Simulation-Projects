# coding: utf-8
# Your code here!
import numpy as np
#phase 1: customers go to the cashier

CustArrTime = []
completionTime_cashier = []
completionTime_Soup = []
completionTime_Salad = []
CustArrTime_cashier = []
CustArrTime_salad = []
CustArrTime_soup = []

CustArrTime_cashier.insert(0,0)
CustArrTime_salad.insert(0,0)
CustArrTime_soup.insert(0,0)
completionTime_cashier.insert(0,0)
completionTime_Salad.insert(0,0)
completionTime_Soup.insert(0,0)

availTime_salad = [0,0,0,0]
availTime_soup = [0,0]

startTime = 0
serviceTime = 0
cashierTime = 0
SaladTime = 0
SoupTime = 0
n_Salad_Soup = 0

#phase 1: customers go to the cashier
for i  in range(20000):
  IAT = np.random.normal( 1 , .2)
  CustArrTime_cashier.insert(i ,IAT + CustArrTime_cashier[i - 1])

  if CustArrTime_cashier[i] > completionTime_cashier[i - 1]:
    startTime = CustArrTime_cashier[i];
  else:
    startTime = completionTime_cashier[i - 1]
  
  serviceTime = np.random.normal( 40/60 , 10/60)
  completionTime_cashier.insert(i ,serviceTime + startTime);
  cashierTime = cashierTime + (completionTime_cashier[i] - startTime)

avg_cashier = (cashierTime /20000)
print("average time on the cashier is " ,avg_cashier * 60," seconds")

#phase 2: customers go to the salad bar
for i  in range(20000):
    
    CustArrTime_salad.insert(i, completionTime_cashier[i])
    
    minTime = min(availTime_salad)
    
    if CustArrTime_salad[i] > minTime:
        startTime = CustArrTime_salad[i];
    else:
        startTime = minTime
        
    availIndex = availTime_salad.index(minTime)
    serviceTime = np.random.normal(120/60 , 20/60)
    
    completionTime_Salad.insert(i ,(serviceTime + startTime))
    availTime_salad.insert(availIndex ,completionTime_Salad[i])
    SaladTime = SaladTime + (completionTime_Salad[i] - startTime)

avg_salad = (SaladTime /20000)
print("average time on the salad bar is " ,avg_salad ,"minutes")

#to determine how many people proceed to the soup section
for i  in range(20000):
    if np.random.uniform(0,1) < 0.6:
        CustArrTime_soup.insert(n_Salad_Soup, completionTime_Salad[i])
        n_Salad_Soup = n_Salad_Soup + 1

#phase 3: customers go to the soup section
for i  in range(n_Salad_Soup):
    
        minTime = min(availTime_soup)
        if CustArrTime_soup[i] > minTime:
            startTime = CustArrTime_soup[i];
        else:
            startTime = minTime
        


        serviceTime = np.random.normal(60/60 , 15/60)
        completionTime_Soup.insert(i ,(serviceTime + startTime));
        
        availIndex = availTime_soup.index(minTime)
        availTime_soup.insert(availIndex ,completionTime_Soup[i])

        SoupTime = SoupTime + (completionTime_Soup[i] - startTime)

avg_soup = (SoupTime /n_Salad_Soup)
print("average time on the soup bars is " ,avg_soup ,"minutes")

print("average time on both the salad and the soup bars is" ,avg_soup+ avg_salad+avg_cashier)