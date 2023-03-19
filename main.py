b = int(input())
h = [int(a) for a in input().split()]
S = [0]

def calcAverage(mountains):
  asV = 0
  for x in range(int(len(mountains)/2 + .5)):
    D = mountains[len(mountains)-1-x]-mountains[x]
    asV += D
  return int(asV)

for x in range(1, len(h)):
  avgs = []
  for i in range(len(h)-x):
    avg = calcAverage(h[i:i+x+1])
    avgs.append(avg) 
    if (avg == 0):
      break
  S.append(min(avgs))


[print(a, end = " ") for a in S]
print()

