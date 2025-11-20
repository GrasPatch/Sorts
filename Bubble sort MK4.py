# [program name]
# [your name]
# [date]
# AS Computer Science

import random, time

# [comment]
def list():
    try:
        blist = [random.randint(1, 1000) for x in range(10000)]
        start = time.time()
        
        length = len(blist)
        print(f"List is {length} values long.")
        n = len(blist)-1
        Pass = 1
        swapped = True
        Swaps = 0
        
        while (swapped):
            swapped = False
            for index in range(0, n):
                if (blist[index] > blist[index+1]):
                    Swaps += 1
                    temp = blist[index]
                    blist[index] = blist[index+1]
                    blist[index+1] = temp
                    swapped = True
            Pass += 1
        end = time.time()
        speed = round(end - start, 5)
        print(blist)
        print(f"{Swaps} swaps were made. ")
        print(f"{Pass} passes were made.")
        print(f"Time taken was {speed}s")
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        pass
        list()
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
