import random
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
#(Not Cam, Cam)

games = [(.5, .7), (.3, .6), (1, 1), (.5, .75), (.3, .55), (.95, 1), (.2, .35),
         (.4, .6), (.9, .95), (.3, .55), (.7, .9), (.99, 1)]
ethan = [(.6, .8), (.35, .6), (.95, .99), (.55, .7), (.25, .45), (.6, .8),
         (.15, .4), (.35, .55), (.4, .5), (.25, .45), (.45, .7), (.5, .85)]
landon = [(.6, .8), (.4, .8), (1, 1), (.7, .85), (.5, .65), (1, 1),
         (.0, .5), (.25, .75), (.6, .9), (.5, .8), (.8, .9), (.9, 1)]

notCamResults = []
camResults = []

EthanNotCamResults = []
EthanCamResults = []

LandonNotCamResults = []
LandonCamResults = []

tries = 10000

for i in range(tries):
  notCamWins = 0
  camWins = 0
  for item in games:
    game = random.randint(0, 100) / 100
    if (game <= item[0]):
      notCamWins += 1
    if (game <= item[1]):
      camWins += 1
  notCamResults.append(notCamWins)
  camResults.append(camWins)

  EthanNotCamWins = 0
  EthanCamWins = 0
  for item in ethan:
    game = random.randint(0, 100) / 100
    if (game <= item[0]):
      EthanNotCamWins += 1
    if (game <= item[1]):
      EthanCamWins += 1
  EthanNotCamResults.append(EthanNotCamWins)
  EthanCamResults.append(EthanCamWins)

  LandonNotCamWins = 0
  LandonCamWins = 0
  for item in landon:
    game = random.randint(0, 100) / 100
    if (game <= item[0]):
      LandonNotCamWins += 1
    if (game <= item[1]):
      LandonCamWins += 1
  LandonNotCamResults.append(LandonNotCamWins)
  LandonCamResults.append(LandonCamWins)

# print(LandonCamResults)
tableData = [['Win Total', 'Without Cam', 'With Cam']]
EthanTableData = [['Win Total', 'Without Cam', 'With Cam']]
LandonTableData = [['Win Total', 'Without Cam', 'With Cam']]

for x in range(12):
  tableData.append([
    x + 1, f'{(notCamResults.count(x+1) / (tries/100))}%',
    f'{(camResults.count(x+1) / (tries/100))}%'
  ])
  EthanTableData.append([
    x + 1, f'{(EthanNotCamResults.count(x+1) / (tries/100))}%',
    f'{(EthanCamResults.count(x+1) / (tries/100))}%'
  ])
  LandonTableData.append([
    x + 1, f'{(LandonNotCamResults.count(x+1) / (tries/100))}%',
    f'{(LandonCamResults.count(x+1) / (tries/100))}%'
  ])

# print(f'Season Simulated {tries} Times\n\n')
# print("Tanner's Results:")
# print(tabulate(tableData))
# print("\n\nLandon's Results:")
# print(tabulate(LandonTableData))

tanner = {'1':camResults.count(1) / (tries/100), '2':camResults.count(2) / (tries/100), '3':camResults.count(3) / (tries/100),
        '4':camResults.count(4) / (tries/100), '5':camResults.count(5) / (tries/100), '6':camResults.count(6) / (tries/100),
        '7':camResults.count(7) / (tries/100),'8':camResults.count(8) / (tries/100),'9':camResults.count(9) / (tries/100),
        '10':camResults.count(10) / (tries/100),'11':camResults.count(11) / (tries/100),'12':camResults.count(12) / (tries/100)}

ethan = {'1':EthanCamResults.count(1) / (tries/100), '2':EthanCamResults.count(2) / (tries/100), '3':EthanCamResults.count(3) / (tries/100),
        '4':EthanCamResults.count(4) / (tries/100), '5':EthanCamResults.count(5) / (tries/100), '6':EthanCamResults.count(6) / (tries/100),
        '7':EthanCamResults.count(7) / (tries/100),'8':EthanCamResults.count(8) / (tries/100),'9':EthanCamResults.count(9) / (tries/100),
        '10':EthanCamResults.count(10) / (tries/100),'11':EthanCamResults.count(11) / (tries/100),'12':EthanCamResults.count(12) / (tries/100)}

landon = {'1':LandonCamResults.count(1) / (tries/100), '2':LandonCamResults.count(2) / (tries/100), '3':LandonCamResults.count(3) / (tries/100),
        '4':LandonCamResults.count(4) / (tries/100), '5':LandonCamResults.count(5) / (tries/100), '6':LandonCamResults.count(6) / (tries/100),
        '7':LandonCamResults.count(7) / (tries/100),'8':LandonCamResults.count(8) / (tries/100),'9':LandonCamResults.count(9) / (tries/100),
        '10':LandonCamResults.count(10) / (tries/100),'11':LandonCamResults.count(11) / (tries/100),'12':LandonCamResults.count(12) / (tries/100)}

N = 12
ind = np.arange(N)
fig = plt.figure(figsize = (10, 5))
width = 0.25
 
# creating the bar plot
ethanBar = plt.bar(ind, list(ethan.values()), color ='blue',
        width = 0.25, label = 'Ethan')
tannerBar = plt.bar(ind + width, list(tanner.values()), color ='red',
        width = 0.25,label = 'Tanner')
landonBar = plt.bar(ind + width * 2, list(landon.values()), color ='green',
        width = 0.25,label = 'Landon')

plt.xticks(ind+width,list(tanner.keys()))
plt.xlabel("Wins")
plt.ylabel("% of Simulations")
plt.title("Utah Football Season Simulator")
plt.legend((tannerBar, ethanBar, landonBar), ('Tanner', 'Ethan', 'Landon'))
plt.show()