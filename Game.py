import pygame
import sys
import time
import queue
from mutagen.mp3 import MP3


#游戏初始化
pygame.init()


#混音器模块初始化
pygame.mixer.init()


#图片类
class Images(object):
    #图片类的属性定义
    def __init__(self):
        self.icon_image=pygame.image.load('./game.ico')
        self.mainBackground = pygame.image.load('./images/login/login_bg.png')
        self.startGame = pygame.image.load('./images/login/start_button.png')
        self.quitGame = pygame.image.load('./images/login/exit_button.png')
        self.selectBackground = pygame.image.load('./images/select/select_bg.png')
        self.itemBackground = pygame.image.load('./images/select/music_item_bg.png')
        self.backHome = pygame.image.load('./images/select/back_button.png')
        self.backSelect = pygame.image.load('./images/game/menu_button.png')
        self.upDecision = pygame.image.load('./images/game/up.png')
        self.downDecision = pygame.image.load('./images/game/down.png')
        self.musicImageBackground = [pygame.image.load('./images/music/musicbgr1.png'),pygame.image.load('./images/music/musicbgr2.png')]
        self.scoreBoard = pygame.image.load('./images/game/scoreboard.png')
        self.perfect = pygame.image.load('./images/game/perfect.png')
        self.great = pygame.image.load('./images/game/great.png')
        self.bad = pygame.image.load('./images/game/bad.png')
        self.miss = pygame.image.load('./images/game/miss.png')
        self.note = [pygame.image.load('./images/game/note_1.png'),pygame.image.load('./images/game/note_2.png'),pygame.image.load('./images/game/note_3.png'),pygame.image.load('./images/game/note_4.png'),pygame.image.load('./images/game/note_5.png'),pygame.image.load('./images/game/note_6.png'),pygame.image.load('./images/game/note_7.png'),pygame.image.load('./images/game/note_8.png'),pygame.image.load('./images/game/note_9.png'),pygame.image.load('./images/game/note_10.png')]
        self.note_p = [pygame.image.load('./images/game/note_p_1.png'),pygame.image.load('./images/game/note_p_2.png'),pygame.image.load('./images/game/note_p_3.png'),pygame.image.load('./images/game/note_p_4.png'),pygame.image.load('./images/game/note_p_5.png'),pygame.image.load('./images/game/note_p_6.png'),pygame.image.load('./images/game/note_p_7.png'),pygame.image.load('./images/game/note_p_8.png'),pygame.image.load('./images/game/note_p_9.png'),pygame.image.load('./images/game/note_p_10.png')]
        self.summaryBackground = pygame.image.load('./images/summary/sum_bg.png')
        self.musicImage = [pygame.image.load('./images/music/music1.png'),pygame.image.load('./images/music/music2.png')]
        self.s = pygame.image.load('./images/summary/s_rank.png')
        self.a = pygame.image.load('./images/summary/a_rank.png')
        self.b = pygame.image.load('./images/summary/b_rank.png')
        self.c = pygame.image.load('./images/summary/c_rank.png')
        self.d = pygame.image.load('./images/summary/d_rank.png')
        self.fc = pygame.image.load('./images/summary/fc_image.png')
        self.nextButton = pygame.image.load('./images/summary/next_button.png')


#字体类
class Fonts(object):
    #字体类的属性定义
    def __init__(self):
        self.itemFont = pygame.font.Font('./font/STXINWEI.TTF',30)


#页面类
class Page(object):
    #展示主页
    def ShowHomePage(self):
        screen.blit(images.mainBackground,(0,0))
        screen.blit(images.startGame,(500,275))
        screen.blit(images.quitGame,(500,400))
        pygame.display.update()
    #展示选曲页面
    def ShowSelectPage(self):
        screen.blit(images.selectBackground,(0,0))
        screen.blit(images.backHome,(500,400))
        tips = fonts.itemFont.render("tips:游玩时输入法应为英文",(255,255,255),(0,0,0))
        screen.blit(tips,(10,500))
        pygame.display.update()
    #展示可供选择的曲子
    def ShowMusic(self):
        cout = 0
        f = open('./data/index.txt',encoding='utf-8',mode='r')
        line = f.readline()
        while line:
            cout += 1
            lineList = line.split(' ')
            if cout == 1:
                screen.blit(images.itemBackground,(50,100))
                text = fonts.itemFont.render(lineList[0],(255,255,255),(0,0,0))
                screen.blit(text,(100,150))
            elif cout == 2:
                screen.blit(images.itemBackground,(500,100))
                text = fonts.itemFont.render(lineList[0],(255,255,255),(0,0,0))
                screen.blit(text,(550,150))
            elif cout == 3:
                screen.blit(images.itemBackground,(50,250))
                text = fonts.itemFont.render(lineList[0],(255,255,255),(0,0,0))
                screen.blit(text,(100,300))
            elif cout == 4:
                screen.blit(images.itemBackground,(500,250))
                text = fonts.itemFont.render(lineList[0],(255,255,255),(0,0,0))
                screen.blit(text,(550,300))
            line = f.readline()
        f.close()
        pygame.display.update()
        return cout
    #展示游戏界面
    def ShowGamePage(self,musicId):
        screen.blit(images.musicImageBackground[musicId-1],(0,0))
        screen.blit(images.scoreBoard,(336,0))
        screen.blit(images.backSelect,(0,0))
        screen.blit(images.upDecision,(66,146+75))
        screen.blit(images.downDecision,(66,326+75))
    #展示结算页面
    def ShowEndPage(self,musicId,cout,fcFlag):
        screen.blit(images.summaryBackground,(0,0))
        screen.blit(images.musicImage[musicId-1],(10,140))
        screen.blit(images.nextButton,(720,460))
        score = fonts.itemFont.render(str(int(round(cout[0],0))),(255,255,255),(0,0,0))#可改颜色！！！！！！！！！！！！！！
        screen.blit(score,(220,430))
        maxCombo = fonts.itemFont.render(str(cout[2]),(255,255,255),(0,0,0))
        screen.blit(maxCombo,(810,290))
        if int(round(cout[0],0)) == 10000:
            screen.blit(images.s,(420,130))
        elif int(round(cout[0],0)) >= 9000:
            screen.blit(images.a,(420,130))
        elif int(round(cout[0],0)) >= 8000:
            screen.blit(images.b,(420,130))
        elif int(round(cout[0],0)) >= 6000:
            screen.blit(images.c,(420,130))
        else:
            screen.blit(images.d,(420,130))
        if fcFlag:
            screen.blit(images.fc,(620,380))
        f = open('./data/index.txt',encoding='utf-8',mode='r')
        lineList = []
        line = f.readline()
        while line:
            lineList.append(line)
            line = f.readline()
        f.close()
        bestScore = fonts.itemFont.render(lineList[musicId-1].split(' ')[1],(255,255,255),(0,0,0))
        screen.blit(bestScore,(220,490))
        pygame.display.update()


#响应类
class Response(object):
    #等待主页响应
    def HomePage(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = event.pos
                    #print(mx,my)历史遗留，用来对坐标
                    if mx>=500 and my>=275 and my <400:
                        return 1
                    if mx>=500 and my>=400:
                        pygame.quit()
                        sys.exit()
    #等待选择页面响应
    def SelectPage(self,musicNum):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my= event.pos
                    #print(mx,my)————历史遗留,用来对坐标
                    if mx>=500 and my>=400:
                        return 0
                    elif musicNum>=1 and mx>=50 and mx<=400 and my>=110 and my<=210:
                        return 101
                    elif musicNum>=2 and mx>=520 and mx<=870 and my>=110 and my<=210:
                        return 102
                    elif musicNum>=3 and mx>=50 and mx<=400 and my>=260 and my<=360:
                        return 103
                    elif musicNum>=4 and mx>=520 and mx<=870 and my>=260 and my<=360:
                        return 104
    #等待结算页面响应
    def EndPage(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my= event.pos
                    if mx>=720 and my>=460:
                        return 1


#音符类
class Note(object):
    #音符类的属性定义
    def __init__(self,style):
        self.image = pygame.image.load('./images/game/note.png')
        self.x=1060
        self.y=180*style
        self.isPerfect = 0  #是否完美
        self.pressedImageNum = 1    #打击效果进度
    #音符移动
    def NoteDown(self):
        self.x-=9
        screen.blit(self.image,(self.x,self.y))
    #类型判断
    def NoteCheck(self,linex,nowNoteList,pressedNoteList,cout,noteNum):
        keyPressed = pygame.key.get_pressed()
        perfectScore = 10000/noteNum
        greatScore = 6000/noteNum
        badScore = 1000/noteNum
        #上方音符
        if self.y==180:
            if keyPressed[pygame.K_f] or keyPressed[pygame.K_e] or keyPressed[pygame.K_w]:  
                #Great判定
                if self.x<=linex-105:
                    pressedNoteList.append(nowNoteList[0])
                    cout[0] += greatScore
                    cout[1] += 1 
                    cout[3] = 2
                    nowNoteList.pop(0)
                #Perfect判定
                elif self.x<=linex-45:
                    self.isPerfect = 1
                    pressedNoteList.append(nowNoteList[0])
                    cout[0] += perfectScore
                    cout[1] += 1
                    cout[3] = 3
                    nowNoteList.pop(0)
                #Great判定
                elif self.x<=linex-15:
                    pressedNoteList.append(nowNoteList[0])
                    cout[0] += greatScore
                    cout[1] += 1
                    cout[3] = 2
                    nowNoteList.pop(0)
                #bad判定
                elif self.x<=linex-3:
                    cout[0] += badScore
                    cout[1] += 1
                    cout[3] = 1
                    nowNoteList.pop(0)    
        #下方音符
        elif self.y==360:
            if keyPressed[pygame.K_j] or keyPressed[pygame.K_i] or keyPressed[pygame.K_o]:
                #Great判定
                if self.x<=linex-105:
                    pressedNoteList.append(nowNoteList[0])
                    cout[0] += greatScore
                    cout[1] += 1 
                    cout[3] = 2
                    nowNoteList.pop(0)
                #Perfect判定
                elif self.x<=linex-45:
                    self.isPerfect = 1
                    pressedNoteList.append(nowNoteList[0])
                    cout[0] += perfectScore
                    cout[1] += 1
                    cout[3] = 3
                    nowNoteList.pop(0)
                #Great判定
                elif self.x<=linex-15:
                    pressedNoteList.append(nowNoteList[0])
                    cout[0] += greatScore
                    cout[1] += 1
                    cout[3] = 2
                    nowNoteList.pop(0)
                #bad判定
                elif self.x<=linex-3:
                    cout[0] += badScore
                    cout[1] += 1
                    cout[3] = 1
                    nowNoteList.pop(0) 
    #打击效果
    def HitEffect(self):
        if self.isPerfect==1:
            screen.blit(images.note_p[self.pressedImageNum-1],(self.x,self.y))
        elif self.isPerfect==0:
            screen.blit(images.note[self.pressedImageNum-1],(self.x,self.y))
        self.pressedImageNum+=1


#游戏类
class Game(object):
    #获取曲谱的音符队列
    def GetNoteQueue(self,musicId):
        noteQueue = queue.Queue()
        f = open('./data/music'+str(musicId)+'.txt',encoding='utf-8',mode='r')
        line = f.readline()
        cout = 0
        while line:
            cout += 1
            lineList = line.strip().split(' ')
            noteQueue.put(lineList)
            line = f.readline()
        return (noteQueue,cout)
    #教程关卡
    def Tutorial(self):
        tipsFlag = [False,False,False]
        tips = [fonts.itemFont.render("请在上方音符落在判断点上时按下f或e或w键",(255,255,255),(255,255,255)),fonts.itemFont.render("请在下方音符落在判断点上时按下j或i或o键",(255,255,255),(255,255,255)),fonts.itemFont.render("接下来再试一次",(255,255,255),(255,255,255))]
        pygame.display.update()
        getNoteQueueReturn = game.GetNoteQueue(1)
        noteQueue =getNoteQueueReturn[0]#获取所选曲谱的音符队列
        noteNum = getNoteQueueReturn[1]#获取队列中音符个数
        nowNoteList = []#存储目前需要显示的音符
        pressedNoteList = []#存储需要打击效果的音符位置
        cout = [0,0,0,-1]#积分板[分数,连击数,最大连击数,上个音符打击类型]
        audio = MP3('./data/music'+str(1)+'.mp3')
        audioLength = audio.info.length
        pygame.mixer.music.load('./data/music'+str(1)+'.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        startTime = time.time()#获取游戏开始时间
        while True:
            #判断音乐是否结束
            if (time.time()-startTime) > audioLength:
                time.sleep(1.5)
                game.Save(1,cout[0])
                page.ShowEndPage(1,cout,noteNum == cout[1])
                return response.EndPage()
            #判断文字是否显示
            if (time.time() - startTime) > 38:
                tipsFlag[2] = False
            elif (time.time() - startTime) > 31:
                tipsFlag[2] = True
            elif (time.time() - startTime) > 23:
                tipsFlag[1] = False
            elif (time.time() - startTime) > 16:
                tipsFlag[1] = True
            elif (time.time() - startTime) > 8:
                tipsFlag[0] = False
            elif (time.time() - startTime) > 1:
                tipsFlag[0] = True
            #判断是否需要将音符从队列加入显示列表
            if not noteQueue.empty():
                if time.time()-startTime>=float(noteQueue.queue[0][1]):
                    newNote = Note(int(noteQueue.get()[0]))
                    nowNoteList.append(newNote)
            #监听输入
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = event.pos
                    if mx > 0 and my > 0 and mx <= 100 and my <= 100:
                        pygame.mixer.quit()
                        pygame.mixer.init()
                        return 1
            if nowNoteList:
                #判断是否有miss
                if nowNoteList[0].x <- 35:
                    nowNoteList.pop(0)
                    cout[1] = 0
                    cout[3] = 0
                #判断音符按下
                else:
                    nowNoteList[0].NoteCheck(100,nowNoteList,pressedNoteList,cout,noteNum)
            #更新maxcombo
            cout[2] = max(cout[2],cout[1])
            #更新显示列表中音符位置
            page.ShowGamePage(1)
            for i in nowNoteList:
                i.NoteDown()
            #更新last combo
            if cout[3] == 0:
                screen.blit(images.miss,(400,40))
            elif cout[3] == 1:
                screen.blit(images.bad,(400,40))
            elif cout[3] == 2:
                screen.blit(images.great,(400,40))
            elif cout[3] == 3:
                screen.blit(images.perfect,(400,40))
            #更新打击效果
            for i in pressedNoteList:
                if i.pressedImageNum == 11:
                    pressedNoteList.remove(i)
                else:
                    i.HitEffect(screen)
            #积分板
            score = fonts.itemFont.render(str(int(round(cout[0],0))),(255,255,255),(255,255,255))
            screen.blit(score,(850,10))
            combo = fonts.itemFont.render(str(cout[1]),(255,255,255),(255,255,255))
            screen.blit(combo,(480,10))
            #显示tips文字
            i = 0
            while i<len(tipsFlag):
                if tipsFlag[i]==True:
                    screen.blit(tips[i],(250,280))
                i+=1
            #刷新屏幕
            pygame.display.update()
            time.sleep(0.0085)
    #游戏主玩法
    def MainGame(self,musicId):
        pygame.display.update()
        getNoteQueueReturn = game.GetNoteQueue(musicId)
        noteQueue =getNoteQueueReturn[0]#获取所选曲谱的音符队列
        noteNum = getNoteQueueReturn[1]#获取队列中音符个数
        nowNoteList = []#存储目前需要显示的音符
        pressedNoteList = []#存储需要打击效果的音符位置
        cout = [0,0,0,-1]#积分板[分数,连击数,最大连击数,上个音符打击类型]
        audio = MP3('./data/music'+str(musicId)+'.mp3')
        audioLength = audio.info.length
        pygame.mixer.music.load('./data/music'+str(musicId)+'.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)
        startTime = time.time()#获取游戏开始时间
        while True:
            #判断音乐是否结束
            if (time.time()-startTime) > audioLength:
                time.sleep(1.5)
                game.Save(musicId,cout[0])
                page.ShowEndPage(musicId,cout,noteNum == cout[1])
                return response.EndPage()
            #判断是否需要将音符从队列加入显示列表
            if not noteQueue.empty():
                if time.time()-startTime>=float(noteQueue.queue[0][1]):
                    newNote = Note(int(noteQueue.get()[0]))
                    nowNoteList.append(newNote)
            #监听输入
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = event.pos
                    if mx > 0 and my > 0 and mx <= 100 and my <= 100:
                        pygame.mixer.quit()
                        pygame.mixer.init()
                        return 1
            if nowNoteList:
                #判断是否有miss
                if nowNoteList[0].x <- 35:
                    nowNoteList.pop(0)
                    cout[1] = 0
                    cout[3] = 0
                #判断音符按下
                else:
                    nowNoteList[0].NoteCheck(100,nowNoteList,pressedNoteList,cout,noteNum)
            #更新maxcombo
            cout[2] = max(cout[2],cout[1])
            #更新显示列表中音符位置
            page.ShowGamePage(musicId)
            for i in nowNoteList:
                i.NoteDown()
            #更新last combo
            if cout[3] == 0:
                screen.blit(images.miss,(400,40))
            elif cout[3] == 1:
                screen.blit(images.bad,(400,40))
            elif cout[3] == 2:
                screen.blit(images.great,(400,40))
            elif cout[3] == 3:
                screen.blit(images.perfect,(400,40))
            #更新打击效果
            for i in pressedNoteList:
                if i.pressedImageNum == 11:
                    pressedNoteList.remove(i)
                else:
                    i.HitEffect()
            #积分板
            score = fonts.itemFont.render(str(int(round(cout[0],0))),(255,255,255),(255,255,255))
            screen.blit(score,(850,10))
            combo = fonts.itemFont.render(str(cout[1]),(255,255,255),(255,255,255))
            screen.blit(combo,(480,10))
            #刷新屏幕
            pygame.display.update()
            time.sleep(0.0085)
    #存档
    def Save(self,musicId,score):
        f = open('./data/index.txt',encoding='utf-8',mode='r')
        lineList = []
        line = f.readline()
        while line:
            lineList.append(line)
            line = f.readline()
        f.close()
        if int(lineList[musicId-1].split(' ')[1]) < score:
            lineList[musicId-1]=lineList[musicId-1].split(' ')[0]+' '+str(int(round(score,0)))+'\n'
            f = open('./data/index.txt',encoding='utf-8',mode='w')
            for line in lineList:
                f.writelines(line)
            f.close()


#创建对象
images = Images()
fonts = Fonts()
page = Page()
response = Response()
game = Game()


#创建窗口
screen = pygame.display.set_mode((960,540))
pygame.display.set_caption('MuseLine')
pygame.display.set_icon(images.icon_image)


#主循环部分
pageFlag = 0
auto = False #自动打歌模式
run = True
while run:
    #进入主页
    if pageFlag==0:
        page.ShowHomePage()
        pageFlag = response.HomePage()
    #进入选曲页面
    elif pageFlag==1:
        page.ShowSelectPage()
        musicNum = page.ShowMusic()
        pageFlag = response.SelectPage(musicNum)
    #进入游戏页面
    else:
        page.ShowGamePage(pageFlag-100)
        if pageFlag == 101:
            pageFlag = game.Tutorial()
        else:
            pageFlag = game.MainGame(pageFlag-100)