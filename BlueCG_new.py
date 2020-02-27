import pyautogui as pag
from matplotlib import pyplot as plt
import cv2
import numpy as np
from time import sleep
#技能等級
player0_skill_level = 9
player1_skill_level = 8
player2_skill_level = 0
#開幾個腳色
player_0=1
player_1=1
player_2=0
#腳色是否用技能
player_0_skill_on =1
player_1_skill_on =1
player_2_skill_on =0
#有幾種怪物
monster0 = 1  
monster1 = 1
monster2 = 0
monster3 = 0
#走路方向
step1_x=138
step1_y=125
step2_x=510
step2_y=407
step =0  #一個方向走3次
#抓技能圖片的寬跟長
if(player_0_skill_on == 1):
    template_player0_skill = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\skill_0.png') #第一個腳色技能圖
    player0_skill_w = template_player0_skill.shape[1]  
    player0_skill_h = template_player0_skill.shape[0]
    if(player_1_skill_on == 1):
        template_player1_skill = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\skill_1.png') #第二個腳色技能圖
        player1_skill_w = template_player1_skill.shape[1]  
        player1_skill_h = template_player1_skill.shape[0]
        if(player_2_skill_on == 1):
            template_player2_skill = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\skill_2.png') #第三個腳色技能圖
            player2_skill_w = template_player2_skill.shape[1]  
            player2_skill_h = template_player2_skill.shape[0]
#抓怪物圖片的寬跟長
if(monster0 == 1):
    template_monster0 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster0.png') #怪物圖0
    monster0_w = template_monster0.shape[1]
    monster0_h = template_monster0.shape[0]
    if(monster1 == 1):
        template_monster1 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster1.png')#怪物圖1
        monster1_w = template_monster1.shape[1]
        monster1_h = template_monster1.shape[0]
        if(monster2 == 1):
            template_monster2 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster2.png')#怪物圖2
            monster2_w = template_monster2.shape[1]
            monster2_h = template_monster2.shape[0]
            if(monster3 == 1):
                template_monster3 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster3.png')#怪物圖3
                monster3_w = template_monster3.shape[1]
                monster3_h = template_monster3.shape[0]
meth ='cv2.TM_SQDIFF_NORMED' #opencv中找物件的公式


while True :
    sleep(2.5)
    play0_screenshot = pag.screenshot(region=(0,0, 640,480 )) #螢幕的截圖(放在最左上角(x,y,寬,長)
    play0_screenshot = np.asarray(play0_screenshot) #轉nparray
    play0_screenshot_copy = play0_screenshot.copy()
    method = eval(meth)
    play0_skill_res = cv2.matchTemplate(play0_screenshot,template_player0_skill,method) #找技能的地方在哪裡
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(play0_skill_res)
    # If the method is TM_SQDIFF_NORMED take minimum
    if method in [cv2.TM_SQDIFF_NORMED]:
        play0_skill_loc = np.where(play0_skill_res <= 0.2) #回傳為 y, x 設一個閾值可以率過錯誤的判斷
        play0_skill_top_left = min_loc #不重要 
    play0_skill_loc=tuple([play0_skill_loc[1],play0_skill_loc[0]]) #將y,x轉換為x,y
    play0_skill_bottom_right = (play0_skill_loc[0] + player0_skill_w, play0_skill_loc[1] + player0_skill_w)#找到正方形的斜對角
    
    if len(play0_skill_loc[0])!=0: #判斷有沒有找到技能框(有沒有進入戰鬥)
        if(player_0_skill_on == 1):  ##第一支腳色是否要使用技能
            cv2.rectangle(play0_screenshot,play0_skill_loc, play0_skill_bottom_right, 255, 2)#左框選的動作
            pag.moveTo(0+play0_skill_loc[0]+(player0_skill_w/2),0+play0_skill_loc[1]+player0_skill_h-8) #選技能的畫面,選最後一個技能所在的地方
            pag.click()
            sleep(0.5)
            pag.moveTo(0+play0_skill_loc[0]+(player0_skill_w/2),0+play0_skill_loc[1]+16*(player0_skill_level-0.5)) #選定技能後，選最後選等級最高的那個技能
            pag.click()
        #monster 找到第一隻怪物的地方做點擊
        if(monster0 == 1):
            player0_monster_screenshot = pag.screenshot(region=(0,0, 376,340 )) #左側，頂部，寬度和高度+
            player0_monster_screenshot = np.asarray(player0_monster_screenshot)
            player0_monster0_res = cv2.matchTemplate(player0_monster_screenshot,template_monster0,method)

            min_val_monster, max_val_monster, min_loc_monster, max_loc_monster = cv2.minMaxLoc(player0_monster0_res)
            if method in [cv2.TM_SQDIFF_NORMED]:
                    player0_monster0_top_left_ = min_loc_monster # 找到左上的位置
            pag.moveTo(player0_monster0_top_left_[0]+monster0_w/2,player0_monster0_top_left_[1]+monster0_h/2)
            pag.click()
            sleep(0.3)
            pag.click()
            sleep(0.3)
        #monster 找到第二隻怪物的地方做點擊
        if(monster1 == 1):
            player0_monster1_res = cv2.matchTemplate(player0_monster_screenshot,template_monster1,method)
            min_val_monster, max_val_monster, min_loc_monster, max_loc_monster = cv2.minMaxLoc(player0_monster1_res)
            if method in [cv2.TM_SQDIFF_NORMED]:
                    player0_monster1_top_left_ = min_loc_monster # 找到左上的位置
            pag.moveTo(player0_monster1_top_left_[0]+monster1_w/2,player0_monster1_top_left_[1]+monster1_h/2)
            pag.click()
            sleep(0.3)
            pag.click()
            sleep(0.3)

        #############第二支腳色############
        if(player_1==1):
            if(player_1_skill_on == 1): #第二支腳色是否要使用技能
                play1_screenshot = pag.screenshot(region=(640,0, 640,480 )) #螢幕的截圖(放在最左上角(x,y,寬,長)
                play1_screenshot = np.asarray(play1_screenshot) #轉nparray
                play1_skill_res = cv2.matchTemplate(play1_screenshot,template_player1_skill,method) #找技能的地方在哪裡
                min_val_monster2, max_val_monster2, min_loc_monster2, max_loc_monster2 = cv2.minMaxLoc(play1_skill_res)
                play1_skill_loc = np.where(play1_skill_loc <= 0.2) #回傳為 y, x 設一個閾值可以率過錯誤的判斷
                play1_skill_loc=tuple([play1_skill_loc[1],play1_skill_loc[0]]) #轉換為x,y
                pag.moveTo(640+play1_skill_loc[0]+(player1_skill_w/2),play1_skill_loc[1]+player1_skill_h-8)
                sleep(0.3)
                pag.click()
                sleep(0.3)
                pag.moveTo(640+play1_skill_loc[0]+(player1_skill_w/2),play1_skill_loc[1]+16*(player1_skill_level-0.5))
                pag.click()
            #monster 找到第一隻怪物的地方做點擊
            if(monster0 == 1):
                player1_monster_screenshot = pag.screenshot(region=(640,0, 376,340 )) #螢幕的截圖(放在最左上角(x,y,寬,長)
                player1_monster_screenshot = np.asarray(player1_monster_screenshot) #轉nparray
                player1_monster0_res = cv2.matchTemplate(player1_monster_screenshot,template_monster0,method) #找技能的地方在哪裡
                min_val_monster, max_val_monster, min_loc_monster, max_loc_monster = cv2.minMaxLoc(player1_monster0_res)
                if method in [cv2.TM_SQDIFF_NORMED]:
                    player1_monster0_top_left = min_loc_monster 
                pag.moveTo(640+player1_monster0_top_left[0]+monster0_w/2,player1_monster0_top_left[1]+monster0_h/2)
                pag.click()
                sleep(0.5)
                pag.click()
                sleep(1)
            #monster 找到第二隻怪物的地方做點擊
            if(monster1 == 1):      
                player1_monster1_res = cv2.matchTemplate(player1_monster_screenshot,template_monster1,method)
                min_val_monster, max_val_monster, min_loc_monster, max_loc_monster = cv2.minMaxLoc(player1_monster1_res)
                if method in [cv2.TM_SQDIFF_NORMED]:
                        player1_monster1_top_left = min_loc_monster 
                pag.moveTo(640+player1_monster1_top_left[0]+monster1_w/2,player1_monster1_top_left[1]+monster1_h/2)
                pag.click()
                sleep(0.5)
                pag.click()
        if(player_2==1):
            print('no player2')
    else:
        if (step <3):
            pag.moveTo(step1_x,step1_y)
            pag.click()
        else:
            pag.moveTo(step2_x,step2_y)
            pag.click()
            if(step == 5):
                step =0
        step =step+1
        print("not thing")