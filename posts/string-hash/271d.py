import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

s = readin()
goodbadstr = readin()
k = readint()

# determine bad characters
badch = {}
for i in range(26):
    if goodbadstr[i] == "0": badch[chr(i+97)] = 1

# compute hashes
m = 10**17-3
b = 29
hashvals = {}
n = len(s)

for i in range(n):
    badcount = 0
    h = 0
    for j in range(i,n):
        if badch.get(s[j]) == 1: badcount += 1
        if badcount > k: break # too many bad characters
        h = (h*b + ord(s[j])-96) % m # update hash
        hashvals[h] = 1

print(len(list(hashvals.keys())))