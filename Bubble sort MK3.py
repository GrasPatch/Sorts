# [program name]
# [your name]
# [date]
# AS Computer Science

import random

# [comment]
def list():
    try:
        blist = [random.randint(1, 1000) for x in range(10000)]
        length = len(blist)
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
                    
        print(blist)
        print(f"List is {length} values long.")
        print(f"{Swaps} swaps were made. ")
        print(f"{Pass} passes were made.")
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
