import time
import getch 
from Game import GameState


# ncurses
# file responsible for launching tetris and displaying it on commandline
parsekey = {"a": "LEFT",
        "d": "RIGHT",
        "s": "DOWN"}
def gameLoop(runningG):
    running = True
    starttime = time.time()
    fps = 10
    onceEvery = 1 / fps
    #kthread = KeyboardThread(my_callback)
    while running:
        char = getch.getch()
        print(char)
        #print(chr(27) + "[2J")

        #print(runningG)
        print(1)
        #if char == None:
        time.sleep(onceEvery -((time.time() - starttime) % onceEvery))
        if char in parsekey.keys():
            pass



def main():

    runningG = GameState()
    gameLoop(runningG)



    
    
if __name__ == "__main__":
    main()
