class Player:
    def __init__(self, player,player0_skill_level,player1_skill_level,player2_skill_level,player_0_skill_on,player_1_skill_on,player_2_skill_on, monster_num):
        #技能等級
        self.player0_skill_level = player0_skill_level
        self.player1_skill_level = player1_skill_level
        self.player2_skill_level = player2_skill_level
        #開幾個腳色
        self.player=player
        #腳色是否用技能
        self.player_0_skill_on =player_0_skill_on
        self.player_1_skill_on =player_1_skill_on
        self.player_2_skill_on =player_2_skill_on
        #有幾種怪物
        self.monster_num = monster_num
        #走路方向
        self.step1_x=138
        self.step1_y=125
        self.step2_x=510
        self.step2_y=407
        self.step =0  #一個方向走3次   
        self.meth ='cv2.TM_SQDIFF_NORMED'
        Fight = fight.Fight()
        self.get_player_skill()
        self.get_monster()
    def get_player_skill(self):
        if(self.player_0_skill_on==1):
            self.template_player0_skill = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\skill_0.png') #第一個腳色技能圖
            self.player0_skill_w = self.template_player0_skill.shape[1]  
            self.player0_skill_h = self.template_player0_skill.shape[0]
            if(self.player_1_skill_on ==1):
                self.template_player1_skill = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\skill_1.png') #第二個腳色技能圖
                self.player1_skill_w = self.template_player1_skill.shape[1]  
                self.player1_skill_h = self.template_player1_skill.shape[0]
                if(self.player_2_skill_on ==1):
                    self.template_player2_skill = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\skill_2.png') #第三個腳色技能圖
                    self.player2_skill_w = self.template_player2_skill.shape[1]  
                    self.player2_skill_h = self.template_player2_skill.shape[0]
    def get_monster(self):
        if(self.monster_num >0):
            self.template_monster0 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster0.png') #怪物圖0
            self.monster0_w = template_monster0.shape[1]
            self.monster0_h = template_monster0.shape[0]
            if(monster_num > 1):
                self.template_monster1 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster1.png')#怪物圖1
                self.monster1_w = self.template_monster1.shape[1]
                self.monster1_h = self.template_monster1.shape[0]
                if(monster_num > 2):
                    self.template_monster2 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster2.png')#怪物圖2
                    self.monster2_w = self.template_monster2.shape[1]
                    self.monster2_h = self.template_monster2.shape[0]
                    if(monster_num == 3):
                        self.template_monster3 = cv2.imread('C:\\Users\iioyuo\Desktop\Git hub\BlueCG_auto\monster3.png')#怪物圖3
                        self.monster3_w = self.template_monster3.shape[1]
                        self.monster3_h = self.template_monster3.shape[0]
    def start(self):
        while True :
            sleep(2.5)
            play0_screenshot = pag.screenshot(region=(0,0, 640,480 )) #螢幕的截圖(放在最左上角(x,y,寬,長)
            play0_screenshot = np.asarray(play0_screenshot) #轉nparray
            play0_screenshot_copy = play0_screenshot.copy()
            self.method = eval(self.meth)
            play0_skill_res = cv2.matchTemplate(play0_screenshot,self.template_player0_skill,method) #找技能的地方在哪裡
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(play0_skill_res)
            if method in [cv2.TM_SQDIFF_NORMED]:
                play0_skill_loc = np.where(play0_skill_res <= 0.2) #回傳為 y, x 設一個閾值可以率過錯誤的判斷
                play0_skill_top_left = min_loc #不重要 
            play0_skill_loc=tuple([play0_skill_loc[1],play0_skill_loc[0]]) #將y,x轉換為x,y
            play0_skill_bottom_right = (play0_skill_loc[0] + self.player0_skill_w, play0_skill_loc[1] + self.player0_skill_w)#找到正方形的斜對角
            if len(play0_skill_loc[0])!=0:
                Fight.isfight(self.player_0_skill_on,self.player0_skill_level,play0_skill_loc,self.player0_skill_w,self.player0_skill_w)
            
if __name__ == "__main__":
    Set = Player(2,9,8,0,1,1,1,2)
    Set.start()
   






