#all mouse movements and clicks go in here

# dependencies
import pyautogui, math

pyautogui.FAILSAFE = True # move mouse to top right to kill me # TODO del me

class Mouse_Lib():
    def __init__(self):
        self.screen_width = pyautogui.size()[0]
        self.screen_height =  pyautogui.size()[1]
        self.center_of_screen = [pyautogui.size()[0]//2, pyautogui.size()[1]//2]
    def do_circle(self, center, radius): # all args in pixels 
        """move the mouse in a circle (draws diamond)"""
        # common duration
        d = 1
        
        # start position and circumference
        startPos = [center[0]+radius,center[1]]

        # move to the right of center until you are at the radius
        pyautogui.moveTo(startPos[0],startPos[1])
        
        pyautogui.moveRel(radius*-1,radius*-1,d)
        pyautogui.moveRel(radius*-1,radius,d)
        pyautogui.moveRel(radius,radius,d)
        pyautogui.moveRel(radius,radius*-1,d)
    def do_click(self):
        """click the mouse"""
        pyautogui.click()
    def loop_de_loop_click(self):
        """do a figure 8 centered and click in the middle (draws diamonds)"""
        # define common radius
        r = 500
        
        # put at center of screen
        pyautogui.moveTo(self.center_of_screen[0],self.center_of_screen[1])

        # click
        self.do_click()

        # right circle
        right_circle_center = [self.center_of_screen[0] + self.center_of_screen[0]//2,self.center_of_screen[1]]
        self.do_circle(right_circle_center,r)

        # left circle
        left_circle_center = [self.center_of_screen[0]//2,self.center_of_screen[1]]
        self.do_circle(left_circle_center,r)

        # click
        self.do_click()
    def mc_afk_loop(self):
        """make sure raw input is off under mouse settings"""
        # put at center of screen
        pyautogui.moveTo(self.center_of_screen[0],self.center_of_screen[1])

        # click
        self.do_click()

        # left
        pyautogui.moveRel(-700,0,2) 

        # right
        pyautogui.moveRel(700,0,2)
            
if __name__ == "__main__":
    mouse = Mouse_Lib()
    mouse.loop_de_loop_click()
