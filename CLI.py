import time
from Game import GameState
from getkey import getkey, keys
# ncurses
# file responsible for launching tetris and displaying it on commandline
parsekey = {"a": "LEFT",
        "d": "RIGHT",
        "s": "DOWN"}

def gameLoop(runningG):
    running = True
    starttime = time.time()
    fps = 30
    onceEvery = 1 / fps
    direction = ""
    #kthread = KeyboardThread(my_callback)
    key = getkey()
    while running:
        print(runningG.field)
        if key in parsekey.keys():
            direction = parsekey[key]
        else:
            direction = None
        key = ""
        #print(key)
        print(chr(27) + "[2J")
        print(runningG)
        if direction:
            runningG.moveCurrentPiece(direction)

        time.sleep(onceEvery -((time.time() - starttime) % onceEvery))



def main():

    runningG = GameState()
    gameLoop(runningG)



    
    
if __name__ == "__main__":
    main()
