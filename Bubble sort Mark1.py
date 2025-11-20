# [program name]
# [your name]
# [date]
# AS Computer Science

import random

# [comment]
def list():
    try:
        blist = [random.randint(1, 100) for x in range(5000)]
        length = len(blist)
        n = len(blist)-1
        Pass = 1
        
        for x in range(0, n):
            for index in range(0, n):
                if (blist[index] > blist[index+1]):
                    temp = blist[index]
                    blist[index] = blist[index+1]
                    blist[index+1] = temp
                    print(f"Pass {Pass} complete")
                    Pass += 1
                    
        print(blist)
        print(f"List is {length} values long")
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
