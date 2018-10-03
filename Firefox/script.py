import pyautogui as pg
import numpy as np
import cv2
import time
import random

total_mess_count = 0
old_connection_count = 0
send_count = 0
no_of_pages = 3

message = 'Thank you for connecting, Glad to connect, Congratulations for all that you do and especially for just who you are. My best wishes to you for your journeys into the future. Please stay in touch; taking unexpected folks in the road can create spectacular destinations. Best Regards, Ali.'


def isNew():
    # message window parameters
    window_tuple = (725, 500, 300, 150)
    # getting a screenshot of the chat window
    window_image = pg.screenshot(region=window_tuple)
    # converting to array
    window_array = np.array(window_image.getdata(), dtype='uint8').reshape(window_image.size[0],
                                                                           window_image.size[1], 3)
    # converting color to grayscale
    gray = cv2.cvtColor(window_array, cv2.COLOR_BGR2GRAY)
    gray = gray / 255
    # checking if the window is full white
    if(gray.sum() == 45000.0):
        return True
    else:
        return False


def clickAllCloseButton():
    black = 0
    white = 0
    while(True):
        whiteClose = pg.locateOnScreen('whiteClose.png')
        if whiteClose == None:
            break
        x, y, width, height = whiteClose
        x = x + int(width/2)
        y = y + int(height/2)
        pg.moveTo(x, y, 0.25)
        pg.click()
        white = white + 1
        time.sleep(0.1)
    while(True):
        blackCloseBlank = pg.locateOnScreen('blackClose.png')
        if blackCloseBlank == None:
            break
        x, y, width, height = blackCloseBlank
        x = x + int(width/1.08)
        y = y + int(height/2)
        pg.moveTo(x, y, 0.25)
        pg.click()
        black = black + 1
        time.sleep(0.1)
    while(True):
        blackCloseShort = pg.locateOnScreen('blackCloseShort.png')
        if blackCloseShort == None:
            break
        x, y, width, height = blackCloseShort
        x = x + int(width/1.083)
        y = y + int(height/2)
        pg.moveTo(x, y, 0.25)
        pg.click()
        black = black + 1
        time.sleep(0.1)
    while(True):
        blackCloseLong = pg.locateOnScreen('blackCloseLong.png')
        if blackCloseLong == None:
            break
        x, y, width, height = blackCloseLong
        x = x + int(width/1.05)
        y = y + int(height/2)
        pg.moveTo(x, y, 0.25)
        pg.click()
        black = black + 1
        time.sleep(0.1)
    if black == 0:
        pg.moveTo(1024, 388)
        pg.click()
    # print the no. of black close and white close encountered
    print("black ", black, " white ", white)


def clickSend():
    timer = 0
    # endless attempts for the send button
    while (True):
        sendButton = pg.locateOnScreen('sendButton.png')
        if sendButton == None:
            timer = timer + 1
            time.sleep(0.25)
            if(timer > 4):
                # links hide the send button
                x = random.randint(0, pg.size()[0])
                y = random.randint(0, pg.size()[1])
                pg.moveTo(x, y)
                pg.press('space')
                count = 0
            continue
        else:
            x, y, width, height = sendButton
            x = x + int(width/2)
            y = y + int(height/2)
            pg.moveTo(x, y, 0.25)
            pg.click()
            break
    return


def writeMessage():
    # pg.typewrite(message, interval=0.01)
    pg.hotkey('ctrl', 'v')


pg.hotkey('altleft', '\t')  # to get the browser on the screen
time.sleep(1)
for i in range(no_of_pages):
    clickAllCloseButton()
    list_of_message_button = pg.locateAllOnScreen('message.png')
    for button in list_of_message_button:
        left, top, width, height = button
        xbutton, ybutton = left + int(width/2), top + int(height/2)
        pg.moveTo(xbutton, ybutton, 0.5)
        pg.click()
        total_mess_count = total_mess_count + 1
        time.sleep(2)
        found = isNew()
        if(found):
            writeMessage()
            clickSend()
            send_count = send_count + 1
        if(not found)
            old_count = old_count + 1
        clickAllCloseButton()
    pg.press('pagedown')
    time.sleep(1.5)
    print(total_mess_count, "total message button clicked")
    print(old_count, "old connection found")
    print(send_count, "send button clicked")
