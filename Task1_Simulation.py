import random
import numpy as np
import matplotlib.pyplot as plt

c1 = []
c2 = []
x = []
profit = []
losscounter  = 0

strNum = input("how many trials do you want to generate\n")
num = int(strNum)

for i in range(num):
    tempC1 = random.uniform(0,1)
    if  0 <= tempC1 < 0.1:
        c1.insert(i , 43)
    elif 0.1 <= tempC1 < 0.3:
        c1.insert(i , 44)
    elif 0.3 <= tempC1 < 0.7:
        c1.insert(i , 45)
    elif 0.7 <= tempC1 < 0.9:
        c1.insert(i , 46)
    elif 0.9 <= tempC1 < 1:
        c1.insert(i , 47)

    temp_C2 = random.uniform(0, 1)
    c2.insert(i , 80 + temp_C2 * ( 100-80 ) )

    temp_X = np.random.normal(15000 , 4500)
    x.insert (i , temp_X)

    temp_profit = (249 - tempC1 - temp_C2) * temp_X - 1000000
    profit.insert(i , temp_profit)

    if profit[i] <= 0 :
      losscounter = losscounter + 1

maxProfit =  max(profit)
minProfit = min(profit)
probability_of_loss = losscounter / num

print("the probability of loss is ", probability_of_loss)
print("the maximum profit is : ",maxProfit)
print("the minimum profit is : ",minProfit)
plt.figure(1)
plt.hist(c1 , bins = "auto")
plt.show()

plt.figure(2)
plt.hist(c2 , bins = "auto")
plt.show()

plt.figure(3)
plt.hist(profit , bins = "auto")
plt.show()
