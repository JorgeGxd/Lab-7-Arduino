import pyfirmata 
import time
PORT = "COM3"
board = pyfirmata.Arduino(PORT)


def onLed():
    for x in range (1,10):
        board.digital[13].write(1)
        time.sleep(0.5)
        board.digital[13].write(0)
        time.sleep(0.5)
        board.digital[8].write(1)
        time.sleep(0.5)
        board.digital[8].write(0)
        time.sleep(0.5)
    

