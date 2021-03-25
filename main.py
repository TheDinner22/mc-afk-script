# main thingy

# dependencies
from lib.mouse import Mouse_Lib
import time
def main():
    """all happens in here"""
    # wait x seconds then do loop de loops
    x = 5
    mouse = Mouse_Lib()
    time.sleep(x)
    while True:
        mouse.mc_afk_loop()
main()