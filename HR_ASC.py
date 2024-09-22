j = int(input())
w = list(map(int,input().split()))
counters = [1]*100000
for i in w:
    counters[i] += 1

modus = max(counters)
ubah = 0

for i in w:
    if counters[i] != modus:
        ubah += 1
print(ubah)