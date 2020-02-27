class Fight:
     def __init__(self):
         pass
     def isfight(self,skill_on,skill_level,skill_loc,w,h):
         if(skill_on == 1):  ##第一支腳色是否要使用技能
            pag.moveTo(0+skill_loc[0]+(skill_w/2),0+skill_loc[1]+h-8) #選技能的畫面,選最後一個技能所在的地方
            pag.click()
            sleep(0.5)
            pag.moveTo(0+skill_loc[0]+(skill_w/2),0+loc[1]+16*(skill_level-0.5)) #選定技能後，選最後選等級最高的那個技能
            pag.click()
            sleep(0.5





