import random, time

Ilist = [random.randint(1, 100) for x in range (100000)]
start = time.time()

for i in range (1, len(Ilist)):
    Temp2 = i
    Current = Ilist[Temp2]
    while Temp2>0 and Ilist[Temp2-1]>Current:
        Ilist[Temp2] = Ilist[Temp2-1]
        Temp2-=1
    Ilist[Temp2] = Current


end = time.time()

print(f"The sort took {round(end - start, 3)}s")
print(Ilist)
