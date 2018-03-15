from math import sqrt

# Pythagorean Distance
def pythagorean(v1,v2):
  pSum=sum([pow(v1[i]-v2[i],2) for i in range(len(v1))])
  if pSum==0: return 1
  return 1/sqrt(pSum)

# Manhattan Distance
def manhattan(v1,v2):
  pSum=sum([abs(v1[i]-v2[i]) for i in range(len(v1))])
  if pSum==0: return 1
  return 1/float(pSum)