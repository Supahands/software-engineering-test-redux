from datetime import *
from datetime import timedelta
from random import randint
from random import sample

start = datetime.now()
end = start+timedelta(days=60)

# for _ in range(10):
#  if _ % 2 == 0:
#   value = randint(1, 12)
#  else:
#   value = randint(24, 48) 

# step = timedelta(hours=value)

result = []

while start < end:
    result.append(start.strftime('%Y-%m-%d %H:%M:%S'))
    high_rand = randint(24, 72)
    low_rand = randint(5,18)
    value = randint(low_rand, high_rand) 
    step = timedelta(hours=value)
    start += step

res = sample(result,len(result))

print(res)

Data = res
Data.sort(reverse=True)

DataLen = len(Data) - 1
Table = [[],[],[]]
TableStart = 0
DayVal = 0
x = j = i = 0
for x in range(DataLen):

  b1 = date(int(Data[x][0:4]), int(Data[x][5:7]), int(Data[x][8:10]))
  b2 = date(int(Data[x+1][0:4]), int(Data[x+1][5:7]), int(Data[x+1][8:10]))
  DayCheck = b1 - b2

  if(TableStart == 0):
    TableStart = 1
    DayVal = 1
    Table[0].append(Data[x][0:10])    # START 
  if(DayCheck.days == 1):
    DayVal += 1
  elif(b1 != b2):
    Table[1].append(Data[x][0:10])    # END 
    Table[2].append(DayVal)           # LENGHT 
    TableStart = 0
    DayVal = 0
  if(x == DataLen -1):
    Table[1].append(Data[x][0:10])    # END 
    Table[2].append(DayVal)           # LENGHT 


print("\n\nSTART\t\tEND\t\t\tLENGHT")
for i in range(len(Table[i])):
    for j in range(3):
        print(Table[j][i], end="\t")
    print()
