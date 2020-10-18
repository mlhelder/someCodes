# -*- coding: utf-8 -*-

T = int(input())
i = 0
for i in range(T):
  _, k = input().split() # N podemos ignorar e K (1 ≤ K ≤ 7)
  valores = list(map(int, input().split())) # Potencia 0 até 30, podem se repetir

  maxPotencia = 30
  maxNum = []
  j = 0
  k = int(k)
  
  for j in range(maxPotencia, -1, -1):
    result = []
    for val in valores:
      if (1<<j) & val:
        result.append(val)
    if k <= len(result):
      #adding to result list
      maxNum.append(1<<j)
      valores = result

  print(sum(maxNum))
