from random import randint
from ctypes import *
import time
import os,sys

user32 = windll.LoadLibrary('user32.dll')
def check():
    t = 0
    while True:
        try:
            str_num = input("guess number(0~100)")
            num = int(str_num)
            break
        except:
            t += 1
            if t > 2:
                print("好玩不")
                time.sleep(1)
                user32.LockWorkStation()
                sys.exit(0)

            print("瞎啊, try again")
    return num

def play():
    random_int = randint(0, 100)

    while True:

        # user_guess = int(input("guess number(0~100)"))
        user_guess = check()
        if user_guess == random_int:
            print(f"congratulations! ({random_int})")
            break

        if user_guess < random_int:
            print("less")
            continue

        if user_guess > random_int:
            print("more")
            continue
    print("try again?")
    user_guess = str(input("y?n"))
    if user_guess == "y":
        play()

    elif user_guess == "n":
        print("bye")

    else:
        print("瞎啊,锁锁")
        time.sleep(1)
        user32.LockWorkStation()

if __name__ == '__main__':
    play()
