import pyautogui as pg
import time

list1 = ["from turtle import *", "bgcolor('black')", "color('red')", "begin_fill()", "pensize(3)", "left(50)", "forward(133)", "circle(50, 200)", "right(140)", "circle(50, 200)", "forward(133)", "delay(3000)", "end_fill()"]

time.sleep(10)

for i in list1:

    pg.write(i, interval=0.15)
    pg.press('enter')
pg.moveTo(627, 95, 2, pg.easeInOutQuad)
pg.click()
# with pg.hold('ctrl') and pg.hold('shift'):
#     pg.press('f10')














