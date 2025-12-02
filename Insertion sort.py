import random, time

#Creates the list and calculates the length
Ilist = [random.randint(1, 10000) for x in range (10000)]
len_Ilist = len(Ilist)
print(f"List is {len_Ilist} items long")
start = time.time()

#Lets it be compared
for index in range (1, len_Ilist):
    
    current = Ilist[index]
    index2 = index

    #Calculates whether current data item needs to be sorted
    while (index2 > 0 and Ilist[index2-1] > current):

        Ilist[index2] = Ilist[index2-1]
        index2 = index2 - 1

    Ilist[index2] = current

#Outputs sorted list and how long the sort took
end = time.time()
speed = round(end - start, 5)
print(f"Time taken was {speed}s")
print (Ilist)
