import pyautogui as pag
from matplotlib import pyplot as plt
import cv2
import numpy as np
from time import sleep
skill_level = 9
template_skill = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\skill.png') #技能圖
template_master = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\master.png') #怪物圖1
template_master1 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\master1.png')#怪物圖2
meth ='cv2.TM_SQDIFF_NORMED' #opencv中找物件的公式
#抓圖片的寬跟長
w = template_skill.shape[1]  
h = template_skill.shape[0]
w_master = template_master.shape[1]
h_master = template_master.shape[0]
w_master1 = template_master1.shape[1]
h_master1 = template_master1.shape[0]
while True :
    sleep(5)
    img2 = pag.screenshot(region=(0,0, 640,480 )) #螢幕的截圖(放在最左上角(x,y,寬,長)
    img2 = np.asarray(img2) #轉nparray
    img = img2.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img,template_skill,method) #找技能的地方在哪裡
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
 
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF_NORMED]:
        loc = np.where(res <= 0.2) #回傳為 y, x 設一個閾值可以率過錯誤的判斷
        top_left = min_loc #不重要 
    loc=tuple([loc[1],loc[0]]) #轉換為x,y
    bottom_right = (loc[0] + w, loc[1] + h)#找到正方形的斜對角
    
    if len(loc[0])!=0: #判斷有沒有找到技能框 == 有沒有進入戰鬥
        cv2.rectangle(img,loc, bottom_right, 255, 2)#左框選的動作
        pag.moveTo(0+loc[0]+(w/2),loc[1]+16*9.5)
        pag.click()
        sleep(1)
        pag.moveTo(0+loc[0]+(w/2),loc[1]+16*8.5)
        pag.click()
        #master 找到第一隻怪物的地方做點擊
        img_master = pag.screenshot(region=(0,0, 640,480 )) #左側，頂部，寬度和高度+
        img_master = np.asarray(img_master)
        res_master = cv2.matchTemplate(img_master,template_master,method)
        min_val_master, max_val_master, min_loc_master, max_loc_master = cv2.minMaxLoc(res_master)
        
        if method in [cv2.TM_SQDIFF_NORMED]:
                top_left_master = min_loc_master # 找到左上的位置
        pag.moveTo(top_left_master[0]+w_master/2,top_left_master[1]+h_master/2)
        pag.click()
        sleep(0.5)
        pag.click()
        #master 找到第二隻怪物的地方做點擊
        sleep(1)
        res_master1 = cv2.matchTemplate(img_master,template_master1,method)
        min_val_master, max_val_master, min_loc_master, max_loc_master = cv2.minMaxLoc(res_master1)

        if method in [cv2.TM_SQDIFF_NORMED]:
                top_left_master = min_loc_master # 找到左上的位置
        pag.moveTo(top_left_master[0]+w_master1/2,top_left_master[1]+h_master1/2)
        pag.click()
        sleep(0.5)
        pag.click()
        print("OK")
    else:
        print("not thing")