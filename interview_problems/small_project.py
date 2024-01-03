from time import sleep
def run():
    attempts=1
    points=0
    points_table={}
    name = input("enter your name : ")
    while True:
        for digit in range(1,13):
            try:
                print(digit)
                sleep(0.2)
            except KeyboardInterrupt:
                print(f"Stopped at digit {digit}")
                print(f"points are added {points}")
                sleep(2)
                if digit in [1,5,9,11]:
                    points+=10
                elif digit in [4,7,8,10]:
                    points+=20
                elif digit in [3,2,6,12]:
                    points+=30
                attempts+=1
                if attempts==4:
                    print("You have crossed maximum limit")
                    print(f"{name} has scored {points} points")
                    points_table[name]=points
                    ans=input("Is there any other player, y/n?").lower()
                    if ans=="y":
                        name=input("Enter your name? ")
                        attempts=1
                        points=0
                    else:
                        print("final result:", points_table)
                        return
run()















            


