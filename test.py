import pyautogui as pg
import numpy as np
import cv2
import time

# # pg.hotkey('altleft', '\t')  # to get the browser on the screen
# count = 0
# c = 0
# def clickAllCloseButton():
#     for i in range(10):
#         global count
#         count = count+1
#         blackClose = pg.locateOnScreen('Close.png')
#         # if blackClose == None:
#         #     break
#         if blackClose != None:
#             x, y, width, height = blackClose
#             x = x + int(width*6/7)
#             y = y + int(height/2)
#             pg.moveTo(x, y, 1)
#             pg.click()
#         time.sleep(0.5)
#     while(True):
#         global c
#         c = c+1
#         whiteClose = pg.locateOnScreen('whiteClose.png')
#         if whiteClose == None:
#             break
#         x, y, width, height = whiteClose
#         x = x + int(width/2)
#         y = y + int(height/2)
#         pg.moveTo(x, y, 1)
#         pg.click()
#         time.sleep(0.5)
#
# clickAllCloseButton()
# print(count, c)


# r = None
# while r is None:
#     r = pg.locateOnScreen('Close.png', grayscale = True)
# print(icon_to_click + ' now loaded')






string = 'Thank you for connecting, Glad to connect,'\
        'Congratulations for all that you do and especially for just who you are.'\
        'My best wishes to you for your journeys into the future.'\
        ' Please stay in touch; taking unexpected folks in the road can create spectacular destinations.'

print (string)
