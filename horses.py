import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = []      # empty list to store the values of horse's strength
m = 10000000  # maximum strength
# we store all the values in a list called 'l'
for i in range(n):
    pi = int(input())
    l.append(pi)
   
# we sort that list to improve time's opperation
l.sort()
# And here we calculate the smaller difference between horse's strength
for i in range(n):
    res = abs(l[i]-l[i-1])
    if res<m:
        m=res

print(m)
