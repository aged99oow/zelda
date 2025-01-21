#
# MiniZelda.py 2025/1/22
#
import pyxel
import mzfont
Y_ALIGN, ENEMY_Y_ALIGN = 20, -2
MAP_SIZE_X, MAP_SIZE_Y = 15, 11  
CENTER_X, CENTER_Y = 16*7, 16*5
PERSON_X, PERSON_Y = 7, 4  # Princess, Oldman, etc
NEWITEM_X1, NEWITEM_X2, NEWITEM_X3, NEWITEM_Y = 16*5, 16*7, 16*9, 16*6
NO_DIR, UP, DOWN, LEFT, RIGHT, A_BUTTON, B_BUTTON, X_BUTTON, Y_BUTTON = 0,1,2,3,4,5,6,7,8
REV_DIR = {NO_DIR:NO_DIR, UP:DOWN, DOWN:UP, LEFT:RIGHT, RIGHT:LEFT}
ROT_DIR = {UP:(UP,RIGHT,LEFT,DOWN), RIGHT:(RIGHT,DOWN,UP,LEFT), DOWN:(DOWN,LEFT,RIGHT,UP), LEFT:(LEFT,UP,DOWN,RIGHT)}
# Player Return Value
RET_NONE, RET_GAMEOVER, RET_RELIFE, RET_SHOOT, RET_USEWEAPON, RET_USEITEM, RET_MOVED, RET_CAVEIN, RET_CAVEOUT = 0,11,12,13,14,15,16,17,18
RET_UPROCK, RET_LEFTROCK, RET_RIGHTROCK, RET_SCROLL, RET_GETITEM, RET_SAVEPRINCESS = 19,20,21,22,23,24
# Enemy Retrun Value
RET_ATTACK, RET_DAMAGED, RET_KILLED, RET_SCREENOUT, RET_DISAPPEAR, RET_PLAYER_HIT, RET_DEL, RET_BEAM, RET_DELBOMB = 31,32,33,34,35,36,37,38,39
PLAYER_DAMAGE_WAIT, GAMEOVER_WAIT = 20, 110
MAP_LIST = ((0,0),(1,0),(1,0),(2,0),(1,0),(2,0),(3,0),(4,0), 
            (0,1),(1,1),(2,1),(3,1), 
            (0,2),(1,2),(2,2),(3,2),
            (0,3),(1,3),(2,3),(3,3),
            (0,4),(1,4),(2,4),(3,4),
            (0,5),(1,5),(2,5),(3,5),
            (0,6),(1,6),(2,6),(3,6), (0,7),(1,7),(2,7),(3,7))
FIRST_MAP,GETITEM_MAP,DODONGO_MAP,TESTITART_MAP,DIGDOGGER_MAP,GOHMA_MAP,GLEEOK_MAP,PRINCESS_MAP = 0,1,2,3,4,5,6,7
CAVE1_MAP,CAVE2_MAP,CAVE3_MAP,CAVE4_MAP = 8,9,10,11
BSECRET1_MAP,BSECRET2_MAP,BSECRET3_MAP,BSECRET4_MAP = 12,13,14,15
FSECRET1_MAP,FSECRET2_MAP,FSECRET3_MAP,FSECRET4_MAP = 16,17,18,19 
PSECRET1_MAP,PSECRET2_MAP,PSECRET3_MAP,PSECRET4_MAP = 20,21,22,23
RANDOM1_MAP,RANDOM2_MAP,RANDOM3_MAP,RANDOM4_MAP = 24,25,26,27 
RSECRET1_MAP,RSECRET2_MAP,RSECRET3_MAP,RSECRET4_MAP, RREVEAL1_MAP,RREVEAL2_MAP,RREVEAL3_MAP,RREVEAL4_MAP = 28,29,30,31,32,33,34,35
ENTER_DIR = {FIRST_MAP:(DOWN, LEFT, RIGHT), 
             CAVE1_MAP:(LEFT, RIGHT),CAVE2_MAP:(DOWN, LEFT, RIGHT),CAVE3_MAP:(UP, LEFT, RIGHT),CAVE4_MAP:(UP, DOWN, RIGHT), 
             BSECRET1_MAP:(UP, DOWN, RIGHT),BSECRET2_MAP:(LEFT, RIGHT),BSECRET3_MAP:(UP, LEFT),BSECRET4_MAP:(DOWN, LEFT, RIGHT), 
             FSECRET1_MAP:(UP, DOWN, RIGHT),FSECRET2_MAP:(DOWN, LEFT, RIGHT),FSECRET3_MAP:(UP, LEFT),FSECRET4_MAP:(UP, LEFT, RIGHT), 
             PSECRET1_MAP:(UP, DOWN, LEFT),PSECRET2_MAP:(UP, DOWN, LEFT, RIGHT),PSECRET3_MAP:(LEFT, RIGHT),PSECRET4_MAP:(UP, DOWN, RIGHT),
             RSECRET1_MAP:(UP, LEFT, RIGHT),RSECRET2_MAP:(UP, DOWN, RIGHT),RSECRET3_MAP:(UP, DOWN, LEFT),RSECRET4_MAP:(DOWN, RIGHT),
             RREVEAL1_MAP:(UP, LEFT, RIGHT),RREVEAL2_MAP:(UP, DOWN, RIGHT),RREVEAL3_MAP:(UP, DOWN, LEFT, RIGHT),RREVEAL4_MAP:(DOWN, RIGHT)}
BSECRET_MAP = (BSECRET1_MAP, BSECRET2_MAP, BSECRET3_MAP, BSECRET4_MAP)
FSECRET_MAP = (FSECRET1_MAP, FSECRET2_MAP, FSECRET3_MAP, FSECRET4_MAP)
PSECRET_MAP = (PSECRET1_MAP, PSECRET2_MAP, PSECRET3_MAP, PSECRET4_MAP)
RANDOM_MAP = (RANDOM1_MAP, RANDOM2_MAP, RANDOM3_MAP, RANDOM4_MAP)
RSECRET_MAP = (RSECRET1_MAP, RSECRET2_MAP, RSECRET3_MAP, RSECRET4_MAP)
SECRET_XY = {BSECRET1_MAP:(12,1),BSECRET2_MAP:(4,6),BSECRET3_MAP:(3,1),BSECRET4_MAP:(11,1), 
             FSECRET1_MAP:(10,5),FSECRET2_MAP:(5,5),FSECRET3_MAP:(3,4),FSECRET4_MAP:(11,5),
             PSECRET1_MAP:(3,5),PSECRET2_MAP:(11,5),PSECRET3_MAP:(7,7),PSECRET4_MAP:( 9,6)}
NOENEMY_MAP = (FIRST_MAP, GETITEM_MAP, PRINCESS_MAP)
CAVE_CHARA = ((28,20),(28,24), (30,20),(30,22),(30,24))
MOVABLE_CHARA = ((0,0),(1,0),(0,1),(1,1),(112/8,160/8),(112/8,176/8),(112/8,192/8),  # 砂漠
                 (28,20),(28,24), (30,20),(30,22),(30,24))  # CAVE_CHARA
MP_NONE, MP_OBST = 0, 1
SC_OPENING, SC_GAMEOVER, SC_RETRYMENU, SC_SCROLL, SC_CAVEIN, SC_CAVEOUT, SC_DRYUP, SC_OVERWORLD, SC_GETITEM = 1,2,3,4,5,6,7,8,9
SC_DODONGO, SC_TESTITART, SC_DIGDOGGER, SC_GOHMA, SC_GLEEOK, SC_PRINCESS, SC_SAVEPRINCESS = 10,11,12,13,14,15,16
ST_NONE, ST_INIT, ST_UPROCK, ST_LEFTROCK, ST_RIGHTROCK, ST_END = 0,1,2,3,4,5
M_TREASURE, M_SECRET, M_FLUTE, M_GANON, M_PAUSE = 101, 102, 103, 104, 105
# Weapon,Item,2Items,Boss
I_NONE, W_SWORD, W_WHITE_SWORD, W_MAGICAL_SWORD, W_MASTER_SWORD = 0,1,2,3,4
I_BOOMERANG, I_MAGICAL_BOOMERANG, I_BOMB, I_ARROW, I_SILVER_ARROW, I_BOW = 5,6,7,8,9,10
I_BLUE_CANDLE, I_RED_CANDLE, I_RECORDER, I_MAGICAL_ROD, I_FOOD, I_LETTER = 11,12,13,14,15,16
I_LIFE_POTION, I_2ND_POTION, I_BLUE_RING, I_RED_RING, I_POWER_BRACELET, I_BIBLE, I_MAGICAL_SHIELD = 17,18,19,20,21,22,23 
I_HEART_CONTAINER, I_MOREBOMB = 24,25
M2_BOW_ARROW, M2_BOW_SILVER_ARROW, I2_2NDPOTION_HEARTCONTAINER, I2_LIFEPOTION_2NDPOTION = 201,202,203,204 
S3_SHOP1, S3_SHOP2, R_GETRUPEE100, R_GETRUPEE30, R_PAYRUPEE, R_PAIDRUPEE = 401,402,403,404,405,406
B_DODONGO, B_TESTITART, B_DIGDOGGER, B_GOHMA, B_GLEEOK = 501,502,503,504,505
# Drop Item, Enumy
D_RUPEE, D_5RUPEES, D_HEART, D_BOMB = 601,602,603,604
OCTOROK, BLUEOCTOROK, MOBLIN, BLUEMOBLIN, TEKTITE, BLUETEKTITE, LYNEL, BLUELYNEL = 0,1,2,3,4,5,6,7
ENEMYLIST = (OCTOROK, BLUEOCTOROK, MOBLIN, BLUEMOBLIN, TEKTITE, BLUETEKTITE, LYNEL, BLUELYNEL)
OCTOROKROCK, MOBLINARROW, LYNELSWORD = 701,702,703
# Object
O_FLAME, O_OLDMAN1, O_OLDMAN2, O_OLDWOMAN, O_MOBLIN, O_MERCHANT = 801,802,803,804,805,806
ITEM2PERSON = {I2_LIFEPOTION_2NDPOTION:O_OLDWOMAN, R_GETRUPEE100:O_MOBLIN, R_GETRUPEE30:O_MOBLIN,
               S3_SHOP1:O_MERCHANT, S3_SHOP2:O_MERCHANT, I_MOREBOMB:O_OLDMAN2}  # default:O_OLDMAN1
MAX_LIFE = 6*8
FIRST_GET_RUPEE = 200
PAL1 = (0,0,2,2,2,0,14,14,8,8,10,14, 8, 8,14,14)
PAL2 = (0,0,2,2,2,0, 8, 8,2,2,10, 8, 2, 2, 8, 8)
PAL3 = (0,0,2,0,0,0, 2, 2,0,0,10, 2, 0, 0, 2, 2)

class App:
    def newmap_dataclear(self):
        self.sword = None
        self.swordbeam = None
        self.boomerang = None
        self.bomb = None
        self.arrow = None
        self.candle = None
        self.rod = None
        self.food = None
        self.wind = None
        self.once_candle = True
        self.once_recorder = True
        self.pl.appearitem = 0
        self.drop = []
        self.flame = []
        self.person = []

    def restart(self, asis=False):
        Map.setmap(True)
        if asis:
            maxhp, maxbomb, bomb, rupee = self.pl.maxhp, self.pl.maxbomb, self.pl.bomb, self.pl.rupee
            self.pl = Player(CENTER_X, CENTER_Y)
            self.pl.maxhp, self.pl.hp, self.pl.maxbomb, self.pl.bomb, self.pl.rupee = maxhp, maxhp, maxbomb, bomb, rupee
        else:
            self.pl = Player(CENTER_X, CENTER_Y)
            self.annihi = 0
            #self.annihi = 75  # ___DEBUG
        self.newmap_dataclear()
        self.enemy = []
        self.enemypjtl = []
        self.dodongo = None
        self.testitart = None
        self.digdogger = None
        self.gohma = None
        self.scene = SC_OPENING
        self.status = ST_INIT
        self.opening_cnt = MAP_SIZE_X*4
        self.gameover_cnt = 0
        self.selectmenue = 0
        self.moverock_cnt = 0
        self.dryup_cnt = 0
        self.smaller_cnt = 0
        self.prevmap_enemy, self.nowmap_enemy = None, None
        self.prevmap_reveal1, self.prevmap_reveal2, self.nowmap_reveal1, self.nowmap_reveal2 = [], [], [], []

    def newgame(self):
        Item.inititem()
        self.restart()
        self.pause = False

    def __init__(self):
        pyxel.init(MAP_SIZE_X*16, Y_ALIGN+MAP_SIZE_Y*16, title='Mini Zelda 1.1')
        pyxel.load('assets/MiniZelda.pyxres')
        #pyxel.mouse(True)
        self.newgame()
        pyxel.run(self.update, self.draw)

    def buttonup(self):
        ret = []
        if pyxel.btnr(pyxel.KEY_SHIFT) or pyxel.btnr(pyxel.KEY_X) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_A):
            ret.append(A_BUTTON)
        if pyxel.btnr(pyxel.KEY_CTRL) or pyxel.btnr(pyxel.KEY_Z) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_B):
            ret.append(B_BUTTON)
        if pyxel.btnr(pyxel.KEY_TAB) or pyxel.btnr(pyxel.KEY_C) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_X):
            ret.append(X_BUTTON)
        if pyxel.btnr(pyxel.KEY_SPACE) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_Y):
            ret.append(Y_BUTTON)
        if pyxel.btnr(pyxel.KEY_UP) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            ret.append(UP)
        if pyxel.btnr(pyxel.KEY_DOWN) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            ret.append(DOWN)
        if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            ret.append(LEFT)
        if pyxel.btnr(pyxel.KEY_RIGHT) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            ret.append(RIGHT)
        return ret

    def player_damaged(self, dirc, mult=1):  # プレイヤーがダメージを受けた
        self.pl.damaged_cnt = PLAYER_DAMAGE_WAIT
        if self.pl.updown_hp(-mult if I_RED_RING in Item.item else -2*mult if I_BLUE_RING in Item.item else -4*mult):  # HPが残っていれば弾き飛ばされる
            for i in range(3):
                ret, dx, dy = self.pl.playermove(self.pl.x, self.pl.y, ROT_DIR[dirc][i], True)
                if ret==RET_MOVED:
                    Player.dmg_dir = ROT_DIR[dirc][i]  # 弾き飛ばされる方向
                    break
            else:
                Player.dmg_dir = ROT_DIR[dirc][3]

    def bgm(self, scene=0):
        if scene==SC_OVERWORLD:
            if pyxel.play_pos(0)==None and Item.item:
                pyxel.playm(0, loop=True)  # Overworld
        elif scene==M_TREASURE:
            pyxel.stop()
            pyxel.playm(1)  # Treasure
        elif scene==M_SECRET:
            pyxel.stop()
            pyxel.playm(2)  # Secret
        elif scene==M_FLUTE:
            pyxel.stop()
            pyxel.playm(3)  # Flute
        elif scene==M_GANON:
            pyxel.stop()
            pyxel.playm(4)  # Ganon Appears
        elif scene==M_PAUSE:
            pyxel.stop()
            pyxel.playm(5)  # Pause
        else:
            pyxel.stop()

    def pyxelchoice(self, seq):
        return seq[pyxel.rndi(1,len(seq))-1]

    def setnewenemy(self):  # 敵を新配置
        if self.annihi<5:
            elist = (OCTOROK,)
        elif self.annihi<15 or pyxel.rndi(1,8)==1:
            elist = (OCTOROK,BLUEOCTOROK)
        elif self.annihi<25 or pyxel.rndi(1,8)==1:
            elist = (BLUEOCTOROK,MOBLIN)
        elif self.annihi<35 or pyxel.rndi(1,8)==1:
            elist = (MOBLIN,BLUEMOBLIN)
        elif self.annihi<45 or pyxel.rndi(1,8)==1:
            elist = (BLUEMOBLIN,TEKTITE)
        elif self.annihi<55 or pyxel.rndi(1,8)==1:
            elist = (TEKTITE,BLUETEKTITE)
        elif self.annihi<65 or pyxel.rndi(1,8)==1:
            elist = (BLUETEKTITE,LYNEL)
        elif self.annihi<75 or pyxel.rndi(1,8)==1:
            elist = (LYNEL,BLUELYNEL)
        else:
            elist = (self.pyxelchoice(ENEMYLIST), self.pyxelchoice(ENEMYLIST))
        #elist = (LYNEL,BLUELYNEL)  # ___DEBUG
        newenemy = []
        for _ in range(5):
            x, y = pyxel.rndi(2,MAP_SIZE_X-3), pyxel.rndi(2,MAP_SIZE_Y-3)
            if Map.zmap[x][y]==MP_NONE:
                newenemy.append([x, y, self.pyxelchoice(elist)])
        return newenemy

    def tilemapget(self, mxy):
        return pyxel.tilemaps[0].pget(MAP_LIST[mxy[0]][0]*32+mxy[1]*2, MAP_LIST[mxy[0]][1]*24+mxy[2]*2)

    def tilemapset(self, mxy, uv):
        if uv in ((0,0),(0,1),(1,0),(1,1)):
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2  , MAP_LIST[mxy[0]][1]*24+mxy[2]*2  ,uv)
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2+1, MAP_LIST[mxy[0]][1]*24+mxy[2]*2  ,uv)
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2  , MAP_LIST[mxy[0]][1]*24+mxy[2]*2+1,uv)
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2+1, MAP_LIST[mxy[0]][1]*24+mxy[2]*2+1,uv)
        else:
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2  , MAP_LIST[mxy[0]][1]*24+mxy[2]*2  ,(uv[0],  uv[1]  ))
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2+1, MAP_LIST[mxy[0]][1]*24+mxy[2]*2  ,(uv[0]+1,uv[1]  ))
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2  , MAP_LIST[mxy[0]][1]*24+mxy[2]*2+1,(uv[0],  uv[1]+1))
            pyxel.tilemaps[0].pset(MAP_LIST[mxy[0]][0]*32+mxy[1]*2+1, MAP_LIST[mxy[0]][1]*24+mxy[2]*2+1,(uv[0]+1,uv[1]+1))

    def repair_prevmap(self): 
        if self.prevmap_reveal1:
            self.tilemapset(self.prevmap_reveal1[0], self.prevmap_reveal1[1])
        if self.prevmap_reveal2:
            self.tilemapset(self.prevmap_reveal2[0], self.prevmap_reveal2[1])

    def repair_nowmap(self): 
        if self.nowmap_reveal1:
            self.tilemapset(self.nowmap_reveal1[0], self.nowmap_reveal1[1])
        if self.nowmap_reveal2:
            self.tilemapset(self.nowmap_reveal2[0], self.nowmap_reveal2[1])
    
    def save_prevmapenemy(self):  # 前マップの敵の種類・位置を記録／前マップの敵の消去／前マップの敵の武器を消去
        self.prevmap_enemy = []  # 前マップの敵の種類・位置を記録／前マップの敵の消去
        for i in reversed(range(len(self.enemy))):
            self.prevmap_enemy.append(self.enemy[i].getxyname())
            del self.enemy[i]
        for i in reversed(range(len(self.enemypjtl))):  # 前マップの敵の武器を消去
            del self.enemypjtl[i]

    def move_rock1st(self, ret_dirc):
        self.nowmap_reveal1 = [(Map.now_map,Map.cave_x,Map.cave_y), self.tilemapget((Map.now_map,Map.cave_x,Map.cave_y))]
        self.tilemapset((Map.now_map,Map.cave_x,Map.cave_y), (30,22))  # 階段(茶)
        if ret_dirc==RET_UPROCK:
            self.nowmap_reveal2 = [(Map.now_map,Map.cave_x,Map.cave_y-1), self.tilemapget((Map.now_map,Map.cave_x,Map.cave_y-1))]
            self.status = ST_UPROCK
        elif ret_dirc==RET_LEFTROCK:
            self.nowmap_reveal2 = [(Map.now_map,Map.cave_x-1,Map.cave_y), self.tilemapget((Map.now_map,Map.cave_x-1,Map.cave_y))]
            self.status = ST_LEFTROCK
        elif ret_dirc==RET_RIGHTROCK:
            self.nowmap_reveal2 = [(Map.now_map,Map.cave_x+1,Map.cave_y), self.tilemapget((Map.now_map,Map.cave_x+1,Map.cave_y))]
            self.status = ST_RIGHTROCK
        self.bgm(M_SECRET)  # Secret
        self.moverock_cnt = 16

    def move_rock2nd(self, st_dirc):
        self.moverock_cnt -= 1
        if self.moverock_cnt==0:
            Map.zmap[Map.cave_x][Map.cave_y] = MP_NONE
            if st_dirc==ST_UPROCK:
                Map.zmap[Map.cave_x][Map.cave_y-1] = MP_OBST
                self.tilemapset((Map.now_map,Map.cave_x,Map.cave_y-1), self.nowmap_reveal1[1])  # 岩(茶)
            elif st_dirc==ST_LEFTROCK:
                Map.zmap[Map.cave_x-1][Map.cave_y] = MP_OBST
                self.tilemapset((Map.now_map,Map.cave_x-1,Map.cave_y), self.nowmap_reveal1[1])  # 岩(茶)
            elif st_dirc==ST_RIGHTROCK:
                Map.zmap[Map.cave_x+1][Map.cave_y] = MP_OBST
                self.tilemapset((Map.now_map,Map.cave_x+1,Map.cave_y), self.nowmap_reveal1[1])  # 岩(茶)
            self.status = ST_NONE

    def appear_bombsecret(self):  # 爆弾で洞窟出現
        Map.zmap[Map.cave_x][Map.cave_y] = MP_NONE
        self.nowmap_reveal1 = [(Map.now_map,Map.cave_x,Map.cave_y), self.tilemapget((Map.now_map,Map.cave_x,Map.cave_y))]
        self.tilemapset((Map.now_map,Map.cave_x,Map.cave_y), (28,20))  # 洞窟入口
        self.bgm(M_SECRET)  # Secret

    def appear_firesecret(self):  # 炎で洞窟出現
        Map.zmap[Map.cave_x][Map.cave_y] = MP_NONE
        self.nowmap_reveal1 = [(Map.now_map,Map.cave_x,Map.cave_y), self.tilemapget((Map.now_map,Map.cave_x,Map.cave_y))]
        self.tilemapset((Map.now_map,Map.cave_x,Map.cave_y), (30,20))  # 階段(緑)
        self.bgm(M_SECRET)  # Secret

    # I_BOOMERANG, I_BOW, W_SWORD, I_LETTER, I_ARROW, I_MAGICAL_BOOMERANG, I_POWER_BRACELET, I_RECORDER 
    # W_WHITE_SWORD, I_MAGICAL_ROD, I_BLUE_RING, I_SILVER_ARROW, I_BIBLE, I_MOREBOMB
    def boss_dropitem(self, rate=10):
        if I_BOOMERANG not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_BOOMERANG
        elif I_BOW not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_BOW
        elif W_SWORD not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = W_SWORD
        elif I_LETTER not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_LETTER
        elif I_ARROW not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_ARROW
        elif I_BOOMERANG in Item.item and I_MAGICAL_BOOMERANG not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_MAGICAL_BOOMERANG
        elif I_POWER_BRACELET not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_POWER_BRACELET
        elif I_RECORDER not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_RECORDER
        elif W_SWORD in Item.item and W_WHITE_SWORD not in Item.item and self.pl.maxhp>=32 and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = W_WHITE_SWORD
        elif I_MAGICAL_ROD not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_MAGICAL_ROD
        elif I_BLUE_RING not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_BLUE_RING
        elif I_ARROW in Item.item and I_SILVER_ARROW not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_SILVER_ARROW
        elif I_MAGICAL_ROD in Item.item and I_BIBLE not in Item.item and pyxel.rndi(1,rate)==1:
            self.pl.appearitem = I_BIBLE
        else:
            self.pl.appearitem = I_MOREBOMB

    def update(self):
        if self.scene==SC_OPENING:  # オープニング
            if self.opening_cnt>1:
                self.opening_cnt -= 1
                if self.opening_cnt==1:
                    self.bgm(SC_OVERWORLD)
                    self.scene = SC_OVERWORLD
                    self.status = ST_INIT
            return
        elif self.scene==SC_GAMEOVER:  # ゲームオーバー
            if self.gameover_cnt>1:
                self.gameover_cnt -= 1
                if self.gameover_cnt==1:
                    self.repair_prevmap()
                    self.repair_nowmap()
                    self.scene = SC_RETRYMENU
            return
        elif self.scene==SC_SAVEPRINCESS:  # ゲームクリア
            return
        elif self.scene==SC_RETRYMENU:  # リトライメニュー
            btnup = self.buttonup()
            if UP in btnup and self.selectmenue>0:
                self.selectmenue -= 1
            elif DOWN in btnup and self.selectmenue<2:
                self.selectmenue += 1
            elif A_BUTTON in btnup or B_BUTTON in btnup:
                if self.selectmenue==0:
                    self.restart(True)
                elif self.selectmenue==1:
                    pyxel.quit()
                elif self.selectmenue==2:
                    self.newgame()
            return
        elif self.scene==SC_SCROLL:  # マップスクロール中
            if Map.scrolling():  # True:スクロール終了
                if Map.now_map==PRINCESS_MAP:
                    self.scene = SC_PRINCESS
                    self.status = ST_INIT
                else:
                    if Map.backscroll:  # 前マップ
                        self.nowmap_reveal1, self.prevmap_reveal1 = self.prevmap_reveal1, self.nowmap_reveal1  # 秘密の部屋を復元/記録
                        self.nowmap_reveal2, self.prevmap_reveal2 = self.prevmap_reveal2, self.nowmap_reveal2
                        self.nowmap_enemy = self.prevmap_enemy  # 敵の種類・位置を復元
                    else:  # 新マップ
                        if self.prevmap_reveal1:
                            self.tilemapset(self.prevmap_reveal1[0], self.prevmap_reveal1[1])
                        if self.prevmap_reveal2:
                            self.tilemapset(self.prevmap_reveal2[0], self.prevmap_reveal2[1])
                        self.nowmap_reveal1, self.prevmap_reveal1 = [], self.nowmap_reveal1  # 秘密の部屋を記録
                        self.nowmap_reveal2, self.prevmap_reveal2 = [], self.nowmap_reveal2
                        #self.nowmap_enemy = []
                        self.nowmap_enemy = None
                        if Map.thismap_item==B_DODONGO:
                            self.dodongo = None
                        elif Map.thismap_item==B_TESTITART:
                            self.testitart = None
                        elif Map.thismap_item==B_DIGDOGGER:
                            self.digdogger = None
                        elif Map.thismap_item==B_GOHMA:
                            self.gohma = None
                    self.save_prevmapenemy()  # 前マップの敵の種類・位置を記録／前マップの敵の消去／前マップの敵の武器を消去
                    self.bgm(SC_OVERWORLD)
                    if self.pl.windwarp==1:  # スクロール終了時にワープ中なら
                        self.wind = Wind(0, CENTER_Y)  # 新マップで再度風
                        self.pl.windwarp = 2  # 新マップでワープ中
                    self.scene = SC_OVERWORLD
                    self.status = ST_INIT
            return
        elif self.scene==SC_CAVEIN:  # 洞窟入る
            if self.pl.cavein():  # True:洞窟入終了
                self.save_prevmapenemy()  # 前マップの敵の種類・位置を記録／前マップの敵の消去／前マップの敵の武器を消去
                if Map.now_map==GETITEM_MAP:
                    self.bgm(SC_GETITEM)
                    self.scene = SC_GETITEM
                    self.status = ST_INIT
                elif Map.now_map==DODONGO_MAP:
                    self.scene = SC_DODONGO
                    if self.dodongo==[]:
                        self.status = ST_END
                    else:
                        self.bgm(M_GANON)
                        self.status = ST_INIT
                elif Map.now_map==TESTITART_MAP:
                    self.scene = SC_TESTITART
                    if self.testitart==[]:
                        self.status = ST_END
                    else:
                        self.bgm(M_GANON)
                        self.status = ST_INIT
                elif Map.now_map==DIGDOGGER_MAP:
                    self.scene = SC_DIGDOGGER
                    if self.digdogger==[]:
                        self.status = ST_END
                    else:
                        self.bgm(M_GANON)
                        self.status = ST_INIT
                elif Map.now_map==GOHMA_MAP:
                    self.scene = SC_GOHMA
                    if self.gohma==[]:
                        self.status = ST_END
                    else:
                        self.bgm(M_GANON)
                        self.status = ST_INIT
                elif Map.now_map==GLEEOK_MAP:
                    self.bgm(M_GANON)
                    self.scene = SC_GLEEOK
                    self.status = ST_INIT
            return
        elif self.scene==SC_CAVEOUT:  # 洞窟出る
            if self.pl.caveout():  # True:洞窟出終了
                self.nowmap_enemy = self.prevmap_enemy  # 敵の種類・位置を復元
                self.bgm(SC_OVERWORLD)
                self.scene = SC_OVERWORLD
                self.status = ST_INIT
            return
        elif self.scene==SC_DRYUP:  # 泉乾く
            self.dryup_cnt -= 1
            if self.dryup_cnt in (31,5):
                for i in range(16):
                    pyxel.pal(i,PAL1[i])
            if self.dryup_cnt in (26,10):
                for i in range(16):
                    pyxel.pal(i,PAL2[i])
            if self.dryup_cnt in (21,15):
                for i in range(16):
                    pyxel.pal(i,PAL3[i])
            if self.dryup_cnt==16:
                Map.now_map = Map.now_map+4
                Map.setmap()
            elif self.dryup_cnt==0:
                pyxel.pal()
                self.scene = SC_OVERWORLD
            return
        if X_BUTTON in self.buttonup():  # アイテム変更
            Item.changeitem()
        if Y_BUTTON in self.buttonup():  # 一時停止
            self.bgm()
            if self.pause:
                if self.scene==SC_OVERWORLD:
                    self.bgm(SC_OVERWORLD)
                self.pause = False
            else:
                self.bgm(M_PAUSE)
                self.pause = True
        if self.pause:
            return
        if self.sword is not None:
            ret = self.sword.update()  # ソード
            if ret==RET_DEL:
                self.sword = None
                if self.swordbeam is None and self.pl.hp>self.pl.maxhp-4:
                    self.swordbeam = SwordBeam(self.pl.x, self.pl.y, self.pl.dirc)
        if self.swordbeam is not None:
            ret = self.swordbeam.update()  # ソードビーム
            if ret==RET_DEL:
                self.swordbeam = None
        if self.boomerang is not None:
            ret = self.boomerang.update(self.pl.x, self.pl.y)  # ブーメラン
            if ret==RET_DEL:
                self.boomerang = None
        if self.bomb is not None:
            ret = self.bomb.update()  # 爆弾
            if ret==RET_DEL:
                self.bomb = None
        if self.arrow is not None:
            ret = self.arrow.update()  # 矢
            if ret==RET_DEL:
                self.arrow = None
        if self.candle is not None:
            ret = self.candle.update()  # ロウソク
            if ret==RET_DEL:
                self.candle = None
        if self.rod is not None:
            ret = self.rod.update()  # ロッド
            if ret==RET_DEL:
                self.rod = None
        if self.food is not None:
            ret = self.food.update()  # 餌
            if ret==RET_DEL:
                self.food = None
        if self.wind is not None:
            ret = self.wind.update()  # 風
            if self.pl.windwarp==2 and self.wind.x>=CENTER_X+16:  # 新マップで着
                self.pl.x, self.pl.y = self.wind.x-16, self.wind.y
                Map.scrl_dir = NO_DIR
                self.pl.windwarp = 0
            if ret==RET_DEL:  # 旧マップから消える
                self.wind = None
                if self.pl.windwarp==1:
                    Map.setscroll(RIGHT, FIRST_MAP)
                    self.newmap_dataclear()
                    Map.thismap_item = B_GLEEOK
                    self.scene = SC_SCROLL
                    return
        ret = self.pl.update()  # プレイヤー
        if ret==RET_SAVEPRINCESS:
            self.scene = SC_SAVEPRINCESS
            return
        elif ret==RET_GAMEOVER:
            self.gameover_cnt = 90  # WIPE
            self.scene = SC_GAMEOVER
            return
        elif ret==RET_RELIFE:
            self.bgm(M_TREASURE)  # Treasure
            return
        elif ret==RET_SCROLL:
            self.newmap_dataclear()
            self.scene = SC_SCROLL
            return
        elif ret==RET_CAVEIN:
            self.newmap_dataclear()
            self.bgm()
            self.scene = SC_CAVEIN
            return
        elif ret==RET_CAVEOUT:
            self.newmap_dataclear()
            self.scene = SC_CAVEOUT
            return
        elif ret==RET_GETITEM:
            self.bgm(M_TREASURE)  # Treasure
            if not Map.thismap_item==R_PAIDRUPEE:
                self.person = []
                Map.zmap[PERSON_X][PERSON_Y] = MP_NONE
        elif ret in (RET_UPROCK, RET_LEFTROCK, RET_RIGHTROCK):
            self.move_rock1st(ret)
        elif ret==RET_USEWEAPON:
            if self.sword is None:
                self.sword = Sword(self.pl.x, self.pl.y, self.pl.dirc)
        elif ret==RET_USEITEM:
            if Item.selected_item in (I_BOOMERANG, I_MAGICAL_BOOMERANG) and self.boomerang is None:
                self.boomerang = Boomerang(self.pl.x, self.pl.y, self.pl.dirc, (Item.selected_item==I_MAGICAL_BOOMERANG))
            elif Item.selected_item==I_BOMB and self.bomb is None and self.pl.bomb>0:
                self.pl.updown_bomb(-1)
                self.bomb = Bomb(self.pl.x, self.pl.y, self.pl.dirc)
            elif Item.selected_item in (M2_BOW_ARROW, M2_BOW_SILVER_ARROW) and self.arrow is None and self.pl.rupee>0:
                self.pl.updown_rupee(-1)
                self.arrow = Arrow(self.pl.x, self.pl.y, self.pl.dirc, (Item.selected_item==M2_BOW_SILVER_ARROW))
            elif Item.selected_item==I_BLUE_CANDLE and self.candle is None and self.once_candle:
                self.once_candle = False
                self.candle = Candle(self.pl.x, self.pl.y, self.pl.dirc)
            elif Item.selected_item==I_RED_CANDLE and self.candle is None:
                self.candle = Candle(self.pl.x, self.pl.y, self.pl.dirc)
            elif Item.selected_item==I_MAGICAL_ROD and self.rod is None:
                self.rod = Rod(self.pl.x, self.pl.y, self.pl.dirc, (I_BIBLE in Item.item))
            elif Item.selected_item==I_FOOD and self.food is None:
                self.food = Food(self.pl.x, self.pl.y, self.pl.dirc)
            elif Item.selected_item==I_RECORDER and self.wind is None and self.once_recorder:
                self.once_recorder = False
                self.bgm(M_FLUTE)  # Flute
                if Map.now_map in RSECRET_MAP:
                    self.dryup_cnt = 32
                    self.scene = SC_DRYUP
                elif self.scene==SC_DIGDOGGER:
                    self.smaller_cnt = 32
                else:
                    self.wind = Wind(self.pl.x, self.pl.y)
        if self.scene==SC_OVERWORLD:
            if self.status==ST_INIT:
                if Map.now_map not in NOENEMY_MAP:
                    #if not self.nowmap_enemy:
                    if self.nowmap_enemy is None:
                        self.nowmap_enemy = self.setnewenemy()  # 敵を新配置
                    for x,y,e in self.nowmap_enemy:  # 敵の種類・位置を復元
                        if e==OCTOROK:
                            self.enemy.append(Octorok(x*16, y*16, 1, 200))
                        elif e==BLUEOCTOROK:
                            self.enemy.append(BlueOctorok(x*16, y*16, 2, 180))
                        elif e==MOBLIN:
                            self.enemy.append(Moblin(x*16, y*16, 2, 120))
                        elif e==BLUEMOBLIN:
                            self.enemy.append(BlueMoblin(x*16, y*16, 3, 100))
                        elif e==TEKTITE:
                            self.enemy.append(Tektite(x*16, y*16))
                        elif e==BLUETEKTITE:
                            self.enemy.append(Tektite(x*16, y*16, True))
                        elif e==LYNEL:
                            self.enemy.append(Lynel(x*16, y*16, hp=4, prj=120, hispd=0, atk_pt=2))
                        elif e==BLUELYNEL:
                            self.enemy.append(BlueLynel(x*16, y*16, hp=6, prj=100, hispd=0, atk_pt=4))
                self.status = ST_NONE
            elif self.status in (ST_UPROCK, ST_LEFTROCK, ST_RIGHTROCK):
                self.move_rock2nd(self.status)
            for i in reversed(range(len(self.drop))):  # ルピー／ハート／爆弾
                ret1 = self.drop[i].update()
                if ret1==RET_PLAYER_HIT:
                    if self.drop[i].name==D_RUPEE:
                        self.pl.updown_rupee(1)
                    elif self.drop[i].name==D_5RUPEES:
                        self.pl.updown_rupee(5)
                    elif self.drop[i].name==D_HEART:
                        self.pl.updown_hp(8)
                    elif self.drop[i].name==D_BOMB:
                        self.pl.updown_bomb(4)
                    del self.drop[i]
                elif ret1==RET_DISAPPEAR:
                    del self.drop[i]
            for i in reversed(range(len(self.enemypjtl))):  # 敵の武器
                ret1, dirc = self.enemypjtl[i].update(self.pl.dirc)
                if ret1==RET_KILLED:
                    del self.enemypjtl[i]
                elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                    self.player_damaged(dirc, mult=self.enemypjtl[i].atk_pt)
                    del self.enemypjtl[i]
            for i in reversed(range(len(self.enemy))):  # 敵
                if self.food is None:
                    ret1, dirc = self.enemy[i].update()
                else:
                    ret1, dirc = self.enemy[i].update(self.food.x, self.food.y)
                if ret1==RET_KILLED:  # ドロップアイテム ___DEBUG
                    if pyxel.rndi(1,7)==1:
                        self.drop.append(Rupee(self.enemy[i].x+4, self.enemy[i].y))
                    elif pyxel.rndi(1,6)==1:
                        self.drop.append(FiveRupees(self.enemy[i].x+4, self.enemy[i].y))
                    elif pyxel.rndi(1,5)==1:
                        self.drop.append(Heart(self.enemy[i].x+4, self.enemy[i].y+4))
                    elif pyxel.rndi(1,8)==1 and I_BOMB in Item.item:
                        self.drop.append(DropBomb(self.enemy[i].x+4, self.enemy[i].y))
                    del self.enemy[i]
                    if len(self.enemy)==0:
                        self.annihi += 1
                        # Annihilation : BOOMERANG(9/10), BOW(18//20), SWORD(27/30), LETTER(36/40), MAGICAL_BOOMERANG(49/50)
                        #                POWER_BRACELET(55/60), RECORDER(64/70), WHITE_SWORD(77/80), MAGICAL_ROD(83/90)
                        #                BLUE_RING(92/100), SILVER_ARROW(101/110), BIBLE(113/120)
                        if self.annihi%7==0 and I_BOOMERANG not in Item.item:
                            self.pl.appearitem = I_BOOMERANG
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%11==0 and I_BOW not in Item.item:
                            self.pl.appearitem = I_BOW
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%17==0 and W_SWORD not in Item.item:
                            self.pl.appearitem = W_SWORD
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%23==0 and I_LETTER not in Item.item:
                            self.pl.appearitem = I_LETTER
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%31==0 and I_BOOMERANG in Item.item and I_MAGICAL_BOOMERANG not in Item.item:
                            self.pl.appearitem = I_MAGICAL_BOOMERANG
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%41==0 and I_POWER_BRACELET not in Item.item:
                            self.pl.appearitem = I_POWER_BRACELET
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%47==0 and I_RECORDER not in Item.item:
                            self.pl.appearitem = I_RECORDER
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%59==0 and W_SWORD in Item.item and W_WHITE_SWORD not in Item.item and self.pl.maxhp>=32:
                            self.pl.appearitem = W_WHITE_SWORD
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%67==0 and I_MAGICAL_ROD not in Item.item:
                            self.pl.appearitem = I_MAGICAL_ROD
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%73==0 and I_BLUE_RING not in Item.item:
                            self.pl.appearitem = I_BLUE_RING
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%83==0 and I_ARROW in Item.item and I_SILVER_ARROW not in Item.item:
                            self.pl.appearitem = I_SILVER_ARROW
                            self.bgm(M_SECRET)  # Secret
                        elif self.annihi%97==0 and I_MAGICAL_ROD in Item.item and I_BIBLE not in Item.item:
                            self.pl.appearitem = I_BIBLE
                            self.bgm(M_SECRET)  # Secret
                elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                    self.player_damaged(dirc, mult=self.enemy[i].atk_pt)
                elif ret1==RET_SHOOT and self.food is None:  # 肉使用中は敵武器不使用
                    if self.enemy[i].name in (OCTOROK, BLUEOCTOROK):
                        self.enemypjtl.append(OctorokRock(self.enemy[i].x, self.enemy[i].y, self.enemy[i].dirc))
                    elif self.enemy[i].name in (MOBLIN, BLUEMOBLIN):
                        self.enemypjtl.append(MoblinArrow(self.enemy[i].x, self.enemy[i].y, self.enemy[i].dirc))
                    elif self.enemy[i].name in (LYNEL, BLUELYNEL):
                        self.enemypjtl.append(LynelSword(self.enemy[i].x, self.enemy[i].y, self.enemy[i].dirc, atk_pt=4))
            if Map.now_map in BSECRET_MAP and not self.nowmap_reveal1 and self.bomb is not None:
                if self.bomb.hit(Map.cave_x*16, Map.cave_y*16, 16, 16):
                    self.appear_bombsecret()  # 爆弾で洞窟出現
            if Map.now_map in FSECRET_MAP and not self.nowmap_reveal1:
                if (self.candle is not None and self.candle.hit(Map.cave_x*16, Map.cave_y*16, 16, 16)) or \
                        (self.rod is not None and self.rod.flame_cnt and self.rod.hit(Map.cave_x*16, Map.cave_y*16, 16, 16)):
                    self.appear_firesecret()  # 炎で洞窟出現
        elif self.scene==SC_GETITEM:
            if self.status==ST_INIT:
                self.flame = []  # 炎
                self.flame.append(Object(16*4, 16*4, 100, O_FLAME))
                self.flame.append(Object(16*10, 16*4, 100, O_FLAME))
                if Map.thismap_item:
                    self.person = []  # 人
                    self.person.append(Object(PERSON_X*16, PERSON_Y*16, 100, ITEM2PERSON.get(Map.thismap_item, O_OLDMAN1)))
                    Map.zmap[PERSON_X][PERSON_Y] = MP_OBST
                self.status = ST_NONE
            elif self.status==ST_NONE:
                for i in reversed(range(len(self.flame))):  # 炎
                    ret1, dirc = self.flame[i].update(self.pl.x, self.pl.y)
                    if ret1==RET_KILLED:
                        del self.flame[i]
                    elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                        self.player_damaged(dirc)
                if Map.thismap_item:
                    for i in reversed(range(len(self.person))):  # 人
                        ret1, dirc = self.person[i].update(self.pl.x, self.pl.y)
                        if ret1==RET_DAMAGED and self.person[i].hp<80:
                            self.person[i].beamon()  # 人からビーム
                            for j in reversed(range(len(self.flame))):
                                self.flame[j].beamon()  # 炎からビーム
                        if ret1==RET_KILLED:
                            del self.person[i]
                            Map.zmap[PERSON_X][PERSON_Y] = MP_NONE
                            if not self.person:
                                self.status = ST_END
                        elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                            self.player_damaged(dirc)
            elif self.status==ST_END:
                self.flame = []  # 炎
                Map.thismap_item = 0
        elif self.scene==SC_PRINCESS:
            if self.status==ST_INIT:
                self.flame = []
                self.flame.append(Object(16*5, 16*7, 1, O_FLAME))  # 左
                self.flame.append(Object(16*9, 16*7, 1, O_FLAME))  # 右
                self.flame.append(Object(16*7, 16*6, 100, O_FLAME))  # 中
                self.status = ST_NONE
            elif self.status==ST_NONE:
                for i in reversed(range(len(self.flame))):  # 炎
                    ret1, dirc = self.flame[i].update(self.pl.x, self.pl.y)
                    if ret1==RET_KILLED:
                        del self.flame[i]
                        if len(self.flame)==1:
                            self.flame[0].hp = 1
                        elif not self.flame:
                            self.status = ST_END
                    elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                        self.player_damaged(dirc)
            elif self.status==ST_END:
                pass
        elif self.scene==SC_DODONGO:
            if self.status==ST_INIT:
                self.dodongo = []
                for i in range(3):
                    self.dodongo.append(Dodongo(16*(4+i*3), 16*5))
                self.status = ST_NONE
            elif self.status==ST_NONE:
                for i in reversed(range(len(self.dodongo))):
                    ret1, dirc = self.dodongo[i].update(self.pl.x, self.pl.y)
                    if ret1==RET_KILLED:
                        del self.dodongo[i]
                        if not self.dodongo:
                            self.boss_dropitem(30)
                            self.bgm(M_SECRET)  # Secret
                            self.status = ST_END
                    elif ret1==RET_DELBOMB:
                        self.bomb = None
                    elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                        self.player_damaged(dirc, mult=2)
            elif self.status==ST_END:
                pass
        elif self.scene==SC_TESTITART:
            if self.status==ST_INIT:
                self.testitart = []
                for i in range(2):
                    self.testitart.append(Testitart(16*(5+i*4), 16*5, 7))  # 16*(3+i*4)
                self.status = ST_NONE
            elif self.status==ST_NONE:
                for i in reversed(range(len(self.testitart))):
                    ret1, dirc = self.testitart[i].update(self.pl.x, self.pl.y)
                    if ret1==RET_KILLED:
                        del self.testitart[i]
                        if not self.testitart:
                            self.boss_dropitem(10)
                            self.bgm(M_SECRET)  # Secret
                            self.status = ST_END
                    elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                        self.player_damaged(dirc, mult=2)
            elif self.status==ST_END:
                pass
        elif self.scene==SC_DIGDOGGER:
            if self.status==ST_INIT:
                self.digdogger = []
                for i in range(2):
                    self.digdogger.append(Digdogger(16*(5+i*4), 16*5, 5))  # 16*(3+i*4)
                self.smaller_cnt = 0
                self.status = ST_NONE
            elif self.status==ST_NONE:
                if self.smaller_cnt>1:
                    self.smaller_cnt -= 1
                else:
                    for i in reversed(range(len(self.digdogger))):
                        ret1, dirc = self.digdogger[i].update(self.pl.x, self.pl.y, True if self.smaller_cnt==1 else False)
                        if ret1==RET_KILLED:
                            del self.digdogger[i]
                            if not self.digdogger:
                                self.boss_dropitem(10)
                                self.bgm(M_SECRET)  # Secret
                                self.status = ST_END
                        elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                            self.player_damaged(dirc, mult=2)
            elif self.status==ST_END:
                pass
        elif self.scene==SC_GOHMA:
            if self.status==ST_INIT:
                self.gohma = []
                self.gohma.append(Gohma(16*7, 16*1, 5))
                self.gohma.append(Gohma(16*7, 16*4, 5))
                self.status = ST_NONE
            elif self.status==ST_NONE:
                for i in reversed(range(len(self.gohma))):
                    ret1, dirc = self.gohma[i].update(self.pl.x, self.pl.y)
                    if ret1==RET_KILLED:
                        del self.gohma[i]
                        if not self.gohma:
                            self.boss_dropitem(10)
                            self.bgm(M_SECRET)  # Secret
                            self.status = ST_END
                    elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                        self.player_damaged(dirc, mult=2)
            elif self.status==ST_END:
                pass
        elif self.scene==SC_GLEEOK:
            if self.status==ST_INIT:
                self.gleeok = Gleeok(16*6+12, 8)
                self.status = ST_NONE
            elif self.status==ST_NONE:
                ret1, dirc = self.gleeok.update(self.pl.x, self.pl.y)
                if ret1==RET_KILLED:
                    del self.gleeok
                    self.status = ST_END
                elif ret1==RET_ATTACK and self.pl.damaged_cnt==0:
                    self.player_damaged(dirc, mult=4)
            elif self.status==ST_END:
                pass

    def draw(self):
        pyxel.cls(0)
        Draw.ownrupee(2, 1, self.pl.rupee)  # ルピー
        Draw.ownbomb(30, 1, self.pl.maxbomb, self.pl.bomb)  # 爆弾
        Draw.ownheart(2, 11, self.pl.maxhp, self.pl.hp)  # ハート
        Item.draw()  # アイテム
        if self.scene==SC_SCROLL:
            Map.draw_scroll()  # スクロール
            return
        elif self.scene==SC_RETRYMENU:  # メニュー
            mzfont.text(80, Y_ALIGN+64, 'ツヅケル    -CONTINUE-', 7)
            mzfont.text(80, Y_ALIGN+80, 'オワル      -QUIT-', 7)
            mzfont.text(80, Y_ALIGN+96, 'ヤリナオス  -RETRY-', 7)
            Draw.heart(70, 64+16*self.selectmenue)
            return
        Map.draw()  # マップ
        if self.scene==SC_OPENING:
            pyxel.rect(0, Y_ALIGN, self.opening_cnt*2, MAP_SIZE_Y*16, 0)
            pyxel.rect(MAP_SIZE_X*16-self.opening_cnt*2, Y_ALIGN, self.opening_cnt*2, MAP_SIZE_Y*16, 0)
        elif self.scene==SC_GAMEOVER:
            n = MAP_SIZE_X*4+1
            if self.gameover_cnt<n:
                m = n-self.gameover_cnt
                pyxel.rect(0, Y_ALIGN, m*2, MAP_SIZE_Y*16, 0)
                pyxel.rect(MAP_SIZE_X*16-m*2, Y_ALIGN, m*2, MAP_SIZE_Y*16, 0)
            for x in (-1,0,1):
                for y in (-1,0,1):
                    pyxel.text(102+x, Y_ALIGN+84+y, 'GAME OVER', 0)
            pyxel.text(102, Y_ALIGN+84, 'GAME OVER', 10)
        elif self.scene==SC_OVERWORLD:
            for e in self.enemy:
                e.draw()  # 敵
            for e in self.enemypjtl:
                e.draw()  # 敵の武器
            for e in self.drop:
                e.draw()  # ルピー／ハート／爆弾
            if self.status==ST_UPROCK:
                Draw.rock(Map.cave_x*16, (Map.cave_y-1)*16+self.moverock_cnt)  # 岩(上へ) 
            elif self.status==ST_LEFTROCK:
                Draw.rock((Map.cave_x-1)*16+self.moverock_cnt, Map.cave_y*16)  # 岩(左へ)
            elif self.status==ST_RIGHTROCK:
                Draw.rock((Map.cave_x+1)*16-self.moverock_cnt, Map.cave_y*16)  # 岩(右へ)
        elif self.scene==SC_GETITEM:
            if self.status==ST_NONE:
                for i in reversed(range(len(self.flame))):
                    self.flame[i].draw()
                for i in reversed(range(len(self.person))):
                    self.person[i].draw()
                if Map.thismap_item==W_SWORD:  # ヒトリデハキケンジャ コレヲ サズケヨウ
                    mzfont.text(120, Y_ALIGN+36, 'ヒトリデハキケンジャ')
                    mzfont.text(120, Y_ALIGN+48, 'コレヲ  サズケヨウ')
                    Draw.item(NEWITEM_X2+4, NEWITEM_Y, W_SWORD)
                elif Map.thismap_item==I2_LIFEPOTION_2NDPOTION:  # クスリヲカッテユキナサイ
                    if I_LETTER in Item.item:
                        mzfont.text(120, Y_ALIGN+36, 'クスリヲ')
                        mzfont.text(120, Y_ALIGN+48, 'カッテユキナサイ')
                        Draw.item(NEWITEM_X1+4, NEWITEM_Y, I_LIFE_POTION)
                        Draw.item(NEWITEM_X3+4, NEWITEM_Y, I_2ND_POTION)
                        Draw.rupee(52, 114, pyxel.frame_count//4%2)
                        mzfont.text(64, Y_ALIGN+118, '×  ４０            ６８')
                elif Map.thismap_item in (R_GETRUPEE100, R_GETRUPEE30):  # ミンナニナイショダヨ
                    mzfont.text(120, Y_ALIGN+36, 'ミンナニ')
                    mzfont.text(120, Y_ALIGN+48, 'ナイショダヨ')
                    Draw.rupee(NEWITEM_X2+4, NEWITEM_Y, pyxel.frame_count//4%2)
                    mzfont.text(108, Y_ALIGN+118, '１００' if Map.thismap_item==R_GETRUPEE100 else ' ３０')
                elif Map.thismap_item==R_PAYRUPEE:  # ドアノシュウリダイヲモラウゾ
                    mzfont.text(120, Y_ALIGN+36, 'ドアノシュウリダイヲ')
                    mzfont.text(120, Y_ALIGN+48, 'モラウゾ')
                    Draw.rupee(NEWITEM_X2+4, NEWITEM_Y, pyxel.frame_count//4%2)
                    mzfont.text(108, Y_ALIGN+118, '－３０')
                elif Map.thismap_item==R_PAIDRUPEE:  # モウコワサナイデクレヨ
                    mzfont.text(120, Y_ALIGN+36, 'モウ')
                    mzfont.text(120, Y_ALIGN+48, 'コワサナイデクレヨ')
                elif Map.thismap_item==S3_SHOP1:  # ナンカコウテクレヤ
                    mzfont.text(120, Y_ALIGN+36, 'ナンカコウテクレヤ')
                    Draw.item(NEWITEM_X1+4, NEWITEM_Y, I_BLUE_CANDLE)
                    Draw.item(NEWITEM_X2+4, NEWITEM_Y, I_BOMB)
                    Draw.item(NEWITEM_X3+6, NEWITEM_Y, I_ARROW)
                    Draw.rupee(52, 114, pyxel.frame_count//4%2)
                    mzfont.text(64, Y_ALIGN+118, '×  ６０    ２０    ８０')
                elif Map.thismap_item==S3_SHOP2:  # コレハネウチモノデッセ
                    mzfont.text(120, Y_ALIGN+36, 'コレハ')
                    mzfont.text(120, Y_ALIGN+48, 'ネウチモノデッセ')
                    Draw.item(NEWITEM_X1+6, NEWITEM_Y, I_MAGICAL_ROD)  # I_MAGICAL_SHIELD)
                    Draw.item(NEWITEM_X2+4, NEWITEM_Y, I_BLUE_RING)
                    Draw.item(NEWITEM_X3, NEWITEM_Y, I_HEART_CONTAINER)  # I_FOOD
                    Draw.rupee(52, 114, pyxel.frame_count//4%2)
                    mzfont.text(64, Y_ALIGN+118, '×  ９０   ２５０   ６０')
                elif Map.thismap_item==I_MOREBOMB:  # バクダンヲモットモチタイジャロウ
                    mzfont.text(120, Y_ALIGN+36, 'バクダンヲ  モット')
                    mzfont.text(120, Y_ALIGN+48, 'モチタイジャロウ')
                    Draw.item(NEWITEM_X2, NEWITEM_Y, I_MOREBOMB)
                    Draw.rupee(52, 114, pyxel.frame_count//4%2)
                    mzfont.text(64, Y_ALIGN+118, '×         １００')
                elif Map.thismap_item==I2_2NDPOTION_HEARTCONTAINER:  # スキナホウヲサズケヨウ
                    mzfont.text(120, Y_ALIGN+36, 'スキナホウヲ')
                    mzfont.text(120, Y_ALIGN+48, 'サズケヨウ')
                    Draw.item(NEWITEM_X1+4, NEWITEM_Y, I_2ND_POTION)
                    Draw.item(NEWITEM_X3, NEWITEM_Y, I_HEART_CONTAINER)
                elif Map.thismap_item in (W_WHITE_SWORD, W_MAGICAL_SWORD, I_RED_RING):  # ツカイコナセルナラコレヲサズケヨウ
                    mzfont.text(120, Y_ALIGN+36, 'ツカイコナセルナラ')
                    mzfont.text(120, Y_ALIGN+48, 'コレヲ  サズケヨウ')
                    Draw.item(NEWITEM_X2+4, NEWITEM_Y, Map.thismap_item)
                elif Map.thismap_item==I_LETTER:  # コレヲオバアサンニミセテゴラン
                    mzfont.text(120, Y_ALIGN+36, 'コレヲ  オバアサンニ')
                    mzfont.text(120, Y_ALIGN+48, 'ミセテゴラン')
                    Draw.item(NEWITEM_X2+4, NEWITEM_Y, I_LETTER)
                elif Map.thismap_item:  # コレヲサズケヨウ
                    mzfont.text(120, Y_ALIGN+36, 'コレヲ  サズケヨウ')
                    Draw.item(NEWITEM_X2+4, NEWITEM_Y, Map.thismap_item)
        elif self.scene==SC_PRINCESS:
            if self.status==ST_NONE:
                for i in reversed(range(len(self.flame))):
                    self.flame[i].draw()
            Draw.princess(PERSON_X*16, PERSON_Y*16, 0)
        elif self.scene==SC_SAVEPRINCESS:
            Draw.princess(PERSON_X*16-8, PERSON_Y*16, 0)
            mzfont.text(42, Y_ALIGN+ 36, '　アリガトウ　アナタハ　エイユウデス')
            mzfont.text(42, Y_ALIGN+132, '　　 コウシテ　ヘイワガ　モドッタ')
            mzfont.text(42, Y_ALIGN+148, 'コレデ　コノ　モノガタリハ　オワリデス')
        elif self.scene==SC_DODONGO:
            if self.status==ST_NONE:
                for i in reversed(range(len(self.dodongo))):
                    self.dodongo[i].draw()
        elif self.scene==SC_TESTITART:
            if self.status==ST_NONE:
                for i in reversed(range(len(self.testitart))):
                    self.testitart[i].draw()
        elif self.scene==SC_DIGDOGGER:
            if self.status==ST_NONE:
                for i in reversed(range(len(self.digdogger))):
                    if self.smaller_cnt in (0,1):
                        self.digdogger[i].draw(self.smaller_cnt)
                    else:
                        self.digdogger[i].draw(self.smaller_cnt//2%3)
        elif self.scene==SC_GOHMA:
            if self.status==ST_NONE:
                for i in reversed(range(len(self.gohma))):
                    self.gohma[i].draw()
        elif self.scene==SC_GLEEOK:
            if self.status==ST_NONE:
                self.gleeok.draw()
        if self.sword is not None:
            self.sword.draw(self.pl.x, self.pl.y, self.pl.dirc)  # ソード
        if self.swordbeam is not None:
            self.swordbeam.draw()  # ソードビーム
        if self.boomerang is not None:
            self.boomerang.draw()  # ブーメラン
        if self.bomb is not None:
            self.bomb.draw()  # 爆弾
        if self.arrow is not None:
            self.arrow.draw()  # 矢
        if self.candle is not None:
            self.candle.draw()  # ロウソク
        if self.rod is not None:
            self.rod.draw(self.pl.x, self.pl.y)  # ロッド
        if self.food is not None:
            self.food.draw()  # 餌
        if self.wind is not None:
            self.wind.draw()  # 風
        self.pl.draw()  # プレイヤー
        if self.pause:
            for x in (-1,0,1):
                for y in (-1,0,1):
                    pyxel.text(110+x, Y_ALIGN+84+y, 'PAUSE', 0)
            pyxel.text(110, Y_ALIGN+84, 'PAUSE', 10)

class Map:
    @classmethod
    def setmap(cls, init=False):
        if init:
            cls.scrl_cnt, cls.scrl_dir = 0, NO_DIR
            cls.backscroll = False
            cls.now_map = FIRST_MAP
            #cls.now_map = RSECRET1_MAP # ___DEBUG
            cls.new_map = 0
            cls.old1_map = 0
            cls.old2_map = 0
            cls.thismap_item = 0 if W_SWORD in Item.item else W_SWORD
            #cls.thismap_item = B_GLEEOK  # ___DEBUG
            #cls.thismap_item = W_MAGICAL_SWORD # ___DEBUG
            cls.prevmap_item = 0
        cls.cave_x, cls.cave_y = -1, -1
        Map.zmap = [[MP_NONE]*MAP_SIZE_Y for i in range(MAP_SIZE_X)]
        for x in range(MAP_SIZE_X):
            for y in range(MAP_SIZE_Y):
                tm = pyxel.tilemaps[0].pget(MAP_LIST[cls.now_map][0]*32+x*2, MAP_LIST[cls.now_map][1]*24+y*2)
                if (cls.now_map in BSECRET_MAP or cls.now_map in FSECRET_MAP or cls.now_map in PSECRET_MAP) and \
                        x==SECRET_XY[cls.now_map][0] and y==SECRET_XY[cls.now_map][1]:
                    cls.cave_x, cls.cave_y = x, y
                if tm in MOVABLE_CHARA:
                    if tm in CAVE_CHARA:
                        cls.cave_x, cls.cave_y = x, y
                else:
                    Map.zmap[x][y] = MP_OBST

    @classmethod
    def cavein(cls):
        cls.old2_map = cls.old1_map
        cls.old1_map = cls.now_map
        if cls.thismap_item==B_DODONGO:
            cls.now_map = DODONGO_MAP
        elif cls.thismap_item==B_TESTITART:
            cls.now_map = TESTITART_MAP
        elif cls.thismap_item==B_DIGDOGGER:
            cls.now_map = DIGDOGGER_MAP
        elif cls.thismap_item==B_GOHMA:
            cls.now_map = GOHMA_MAP
        elif cls.thismap_item==B_GLEEOK:
            cls.now_map = GLEEOK_MAP
        else:
            cls.now_map = GETITEM_MAP
        cls.setmap()

    @classmethod
    def caveout(cls):
        if cls.now_map==PRINCESS_MAP:
            cls.now_map = cls.old2_map
            cls.scrl_dir = NO_DIR
        else:
            cls.now_map = cls.old1_map
            cls.old1_map = cls.old2_map
        cls.setmap()

    @classmethod
    def enabelnewmap(cls, nmap, dirc):
        return cls.now_map!=nmap and cls.old1_map!=nmap and dirc in ENTER_DIR[nmap]

    @classmethod
    def setscroll(cls, dirc, new_map=-1):
        cls.backscroll = False
        if not new_map==-1:
            cls.new_map = new_map  # FIRST_MAP/PRINCESS_MAP
        elif cls.scrl_dir==REV_DIR[dirc]:
            cls.backscroll = True
            cls.new_map = cls.old1_map
            cls.old1_map = cls.old2_map
            cls.thismap_item, cls.prevmap_item = cls.prevmap_item, cls.thismap_item
            if cls.thismap_item in Item.item:
                cls.thismap_item = 0
        else:  # 新マップ
            if pyxel.rndi(1,16)==1 and cls.enabelnewmap(FIRST_MAP, dirc):
                cls.new_map = FIRST_MAP
            elif pyxel.rndi(1,9)==1 and cls.enabelnewmap(CAVE1_MAP, dirc):
                cls.new_map = CAVE1_MAP
            elif pyxel.rndi(1,8)==1 and cls.enabelnewmap(CAVE2_MAP, dirc):
                cls.new_map = CAVE2_MAP
            elif pyxel.rndi(1,7)==1 and cls.enabelnewmap(CAVE3_MAP, dirc):
                cls.new_map = CAVE3_MAP
            elif pyxel.rndi(1,6)==1 and cls.enabelnewmap(CAVE4_MAP, dirc):
                cls.new_map = CAVE4_MAP
            elif pyxel.rndi(1,17)==1 and cls.enabelnewmap(BSECRET1_MAP, dirc):
                cls.new_map = BSECRET1_MAP
            elif pyxel.rndi(1,16)==1 and cls.enabelnewmap(BSECRET2_MAP, dirc):
                cls.new_map = BSECRET2_MAP
            elif pyxel.rndi(1,15)==1 and cls.enabelnewmap(BSECRET3_MAP, dirc):
                cls.new_map = BSECRET3_MAP
            elif pyxel.rndi(1,14)==1 and cls.enabelnewmap(BSECRET4_MAP, dirc):
                cls.new_map = BSECRET4_MAP
            elif pyxel.rndi(1,13)==1 and cls.enabelnewmap(FSECRET1_MAP, dirc):
                cls.new_map = FSECRET1_MAP
            elif pyxel.rndi(1,12)==1 and cls.enabelnewmap(FSECRET2_MAP, dirc):
                cls.new_map = FSECRET2_MAP
            elif pyxel.rndi(1,11)==1 and cls.enabelnewmap(FSECRET3_MAP, dirc):
                cls.new_map = FSECRET3_MAP
            elif pyxel.rndi(1,10)==1 and cls.enabelnewmap(FSECRET4_MAP, dirc):
                cls.new_map = FSECRET4_MAP
            elif pyxel.rndi(1,9)==1 and cls.enabelnewmap(PSECRET1_MAP, dirc):
                cls.new_map = PSECRET1_MAP
            elif pyxel.rndi(1,8)==1 and cls.enabelnewmap(PSECRET2_MAP, dirc):
                cls.new_map = PSECRET2_MAP
            elif pyxel.rndi(1,7)==1 and cls.enabelnewmap(PSECRET3_MAP, dirc):
                cls.new_map = PSECRET3_MAP
            elif pyxel.rndi(1,6)==1 and cls.enabelnewmap(PSECRET4_MAP, dirc):
                cls.new_map = PSECRET4_MAP
            elif pyxel.rndi(1,5)==1 and cls.enabelnewmap(RSECRET1_MAP, dirc):
                cls.new_map = RSECRET1_MAP
            elif pyxel.rndi(1,4)==1 and cls.enabelnewmap(RSECRET2_MAP, dirc):
                cls.new_map = RSECRET2_MAP
            elif pyxel.rndi(1,3)==1 and cls.enabelnewmap(RSECRET3_MAP, dirc):
                cls.new_map = RSECRET3_MAP
            elif pyxel.rndi(1,2)==1 and cls.enabelnewmap(RSECRET4_MAP, dirc):
                cls.new_map = RSECRET4_MAP
            else:
                cls.new_map = RANDOM_MAP[pyxel.rndi(0, len(RANDOM_MAP)-1)]
            # 新アイテム
            cls.prevmap_item = cls.thismap_item
            cls.thismap_item = I_NONE
            # FIRST : SWORD, BOSS
            if cls.new_map==FIRST_MAP:
                if W_SWORD not in Item.item and pyxel.rndi(1,3)==1:
                    cls.thismap_item = W_SWORD
                elif pyxel.rndi(1,5)==1:
                    cls.thismap_item = B_DODONGO
                elif pyxel.rndi(1,4)==1:
                    cls.thismap_item = B_TESTITART
                elif pyxel.rndi(1,3)==1:
                    cls.thismap_item = B_DIGDOGGER
                elif pyxel.rndi(1,2)==1:
                    cls.thismap_item = B_GOHMA
                else:
                    cls.thismap_item = B_GLEEOK
            # CAVE : LETTER, MAGICAL_BOOMERANG, RED_CANDLE, WHITE_SWORD, MAGICAL_SWORD, RED_RING, LIFEPOTION_2NDPOTION, SHOP1(BLUE_CANDLE, BOMB, ARROW)
            elif cls.new_map in (CAVE1_MAP, CAVE2_MAP, CAVE3_MAP, CAVE4_MAP):
                if pyxel.rndi(1,12)==1 and I_LETTER not in Item.item:
                    cls.thismap_item = I_LETTER
                elif pyxel.rndi(1,11)==1 and I_BOOMERANG in Item.item and I_MAGICAL_BOOMERANG not in Item.item:
                    cls.thismap_item = I_MAGICAL_BOOMERANG
                elif pyxel.rndi(1,10)==1 and I_BLUE_CANDLE in Item.item and I_RED_CANDLE not in Item.item:
                    cls.thismap_item = I_RED_CANDLE
                elif pyxel.rndi(1,9)==1 and W_SWORD in Item.item and W_WHITE_SWORD not in Item.item:
                    cls.thismap_item = W_WHITE_SWORD
                elif pyxel.rndi(1,8)==1 and W_SWORD in Item.item and W_WHITE_SWORD in Item.item and W_MAGICAL_SWORD not in Item.item:
                    cls.thismap_item = W_MAGICAL_SWORD
                elif pyxel.rndi(1,7)==1 and I_BLUE_RING in Item.item and I_RED_RING not in Item.item:
                    cls.thismap_item = I_RED_RING
                elif pyxel.rndi(1,3)==1:
                    cls.thismap_item = I2_LIFEPOTION_2NDPOTION
                else:
                    cls.thismap_item = S3_SHOP1
            # BSECRET, FSECRET : MAGICAL_ROD, BIBLE, SILVER_ARROW, RECORDER, POWER_BRACELET, MOREBOMB, 2NDPOTION_HEARTCONTAINE, 
            #                    SHOP2(MAGICAL_ROD, BLUE_RING, HEART_CONTAINER), GET_RUPEE, PAY_RUPEE
            elif cls.new_map in (BSECRET1_MAP, BSECRET2_MAP, BSECRET3_MAP, BSECRET4_MAP, FSECRET1_MAP, FSECRET2_MAP, FSECRET3_MAP, FSECRET4_MAP):
                if pyxel.rndi(1,12)==1:
                    cls.thismap_item = B_DODONGO
                elif pyxel.rndi(1,11)==1:
                    cls.thismap_item = B_TESTITART
                elif pyxel.rndi(1,10)==1:
                    cls.thismap_item = B_DIGDOGGER
                elif pyxel.rndi(1,9)==1:
                    cls.thismap_item = B_GOHMA
                elif pyxel.rndi(1,13)==1 and I_MAGICAL_ROD not in Item.item:
                    cls.thismap_item = I_MAGICAL_ROD
                elif pyxel.rndi(1,12)==1 and I_MAGICAL_ROD in Item.item and I_BIBLE not in Item.item:
                    cls.thismap_item = I_BIBLE
                elif pyxel.rndi(1,11)==1 and I_ARROW in Item.item and I_SILVER_ARROW not in Item.item:
                    cls.thismap_item = I_SILVER_ARROW
                elif pyxel.rndi(1,10)==1 and I_RECORDER not in Item.item:
                    cls.thismap_item = I_RECORDER
                elif pyxel.rndi(1,9)==1 and I_POWER_BRACELET not in Item.item:
                    cls.thismap_item = I_POWER_BRACELET
                elif pyxel.rndi(1,8)==1 and I_BOMB in Item.item:
                    cls.thismap_item = I_MOREBOMB
                elif pyxel.rndi(1,7)==1:
                    cls.thismap_item = I2_2NDPOTION_HEARTCONTAINER
                elif pyxel.rndi(1,6)<=3:
                    cls.thismap_item = S3_SHOP2
                elif pyxel.rndi(1,3)==1:
                    cls.thismap_item = R_GETRUPEE100
                elif pyxel.rndi(1,2)==1:
                    cls.thismap_item = R_GETRUPEE30
                else:
                    cls.thismap_item = R_PAYRUPEE
            # PSECRET : 2NDPOTION_HEARTCONTAINER, WHITE_SWORD, MAGICAL_SWORD, RED_RING, SILVER_ARROW, GET_RUPEE, PAY_RUPEE
            elif cls.new_map in (PSECRET1_MAP, PSECRET2_MAP, PSECRET3_MAP, PSECRET4_MAP, RSECRET1_MAP, RSECRET2_MAP, RSECRET3_MAP, RSECRET4_MAP):
                if pyxel.rndi(1,12)==1:
                    cls.thismap_item = B_DODONGO
                elif pyxel.rndi(1,11)==1:
                    cls.thismap_item = B_TESTITART
                elif pyxel.rndi(1,10)==1:
                    cls.thismap_item = B_DIGDOGGER
                elif pyxel.rndi(1,9)==1:
                    cls.thismap_item = B_GOHMA
                elif pyxel.rndi(1,8)==1:
                    cls.thismap_item = I2_2NDPOTION_HEARTCONTAINER
                elif pyxel.rndi(1,7)==1 and W_SWORD in Item.item and W_WHITE_SWORD not in Item.item:
                    cls.thismap_item = W_WHITE_SWORD
                elif pyxel.rndi(1,6)==1 and W_SWORD in Item.item and W_WHITE_SWORD in Item.item and W_MAGICAL_SWORD not in Item.item:
                    cls.thismap_item = W_MAGICAL_SWORD
                elif pyxel.rndi(1,5)==1 and I_BLUE_RING in Item.item and I_RED_RING not in Item.item:
                    cls.thismap_item = I_RED_RING
                elif pyxel.rndi(1,4)==1 and I_ARROW in Item.item and I_SILVER_ARROW not in Item.item:
                    cls.thismap_item = I_SILVER_ARROW
                elif pyxel.rndi(1,3)==1:
                    cls.thismap_item = R_GETRUPEE100
                elif pyxel.rndi(1,2)==1:
                    cls.thismap_item = R_GETRUPEE30
                else:
                    cls.thismap_item = R_PAYRUPEE
        cls.scrl_dir = dirc
        if dirc in (UP, DOWN):
            cls.scrl_cnt = MAP_SIZE_Y*2
        else:  # LEFT, RIGHT
            cls.scrl_cnt = MAP_SIZE_X*2
        return False, -1, -1

    @classmethod
    def scrolling(cls):
        if cls.scrl_cnt:
            cls.scrl_cnt -= 1
        if cls.scrl_cnt==0:
            cls.old2_map = cls.old1_map
            cls.old1_map = cls.now_map
            cls.now_map = cls.new_map
            cls.setmap()
            return True
        return False

    @classmethod
    def draw(cls):
        pyxel.bltm(0, Y_ALIGN, 0, MAP_LIST[cls.now_map][0]*16*16, MAP_LIST[cls.now_map][1]*12*16, 16*16, 11*16)
    
    @classmethod
    def draw_scroll(cls):
        if cls.scrl_dir==UP:
            pyxel.bltm(0, Y_ALIGN, 0, MAP_LIST[cls.new_map][0]*16*16, MAP_LIST[cls.new_map][1]*12*16+cls.scrl_cnt*8, 16*16, (MAP_SIZE_Y*2-cls.scrl_cnt)*8)
            pyxel.bltm(0, Y_ALIGN+(MAP_SIZE_Y*2-cls.scrl_cnt)*8, 0, MAP_LIST[cls.now_map][0]*16*16, MAP_LIST[cls.now_map][1]*12*16, 16*16, cls.scrl_cnt*8)
        elif cls.scrl_dir==DOWN:
            pyxel.bltm(0, Y_ALIGN, 0, MAP_LIST[cls.now_map][0]*16*16, MAP_LIST[cls.now_map][1]*12*16+(MAP_SIZE_Y*2-cls.scrl_cnt)*8, 16*16, cls.scrl_cnt*8)
            pyxel.bltm(0, Y_ALIGN+cls.scrl_cnt*8, 0, MAP_LIST[cls.new_map][0]*16*16, MAP_LIST[cls.new_map][1]*12*16, 16*16, (MAP_SIZE_Y*2-cls.scrl_cnt)*8)
        elif cls.scrl_dir==LEFT:
            pyxel.bltm(0, Y_ALIGN, 0, MAP_LIST[cls.new_map][0]*16*16+cls.scrl_cnt*8, MAP_LIST[cls.new_map][1]*12*16, (MAP_SIZE_X*2-cls.scrl_cnt)*8, 11*16)
            pyxel.bltm(0+(MAP_SIZE_X*2-cls.scrl_cnt)*8, Y_ALIGN, 0, MAP_LIST[cls.now_map][0]*16*16, MAP_LIST[cls.now_map][1]*12*16, cls.scrl_cnt*8, 11*16)
        else:  # RIGHT
            pyxel.bltm(0, Y_ALIGN, 0, MAP_LIST[cls.now_map][0]*16*16+(MAP_SIZE_X*2-cls.scrl_cnt)*8, MAP_LIST[cls.now_map][1]*12*16, cls.scrl_cnt*8, 11*16)
            pyxel.bltm(0+cls.scrl_cnt*8, Y_ALIGN, 0, MAP_LIST[cls.new_map][0]*16*16, MAP_LIST[cls.new_map][1]*12*16, (MAP_SIZE_X*2-cls.scrl_cnt)*8, 11*16)

class Item:
    @classmethod
    def inititem(cls):
        # W_SWORD, I_BOOMERANG, I_BOMB, I_BOW, I_ARROW, I_SILVER_ARROW, I_BLUE_CANDLE, I_RED_CANDLE, I_MAGICAL_ROD, 
        # I_FOOD, I_RECORDER, I_LETTER, I_LIFE_POTION, I_2ND_POTION, I_BLUE_RING, I_RED_RING, I_BIBLE, I_POWER_BRACELET
        cls.item = []
        #cls.item = [W_WHITE_SWORD, I_BOMB, I_BOW, I_SILVER_ARROW, I_RECORDER, I_LETTER, I_LIFE_POTION, I_BLUE_RING]  # ___DEBUG
        cls.a_item = []
        cls.selected_item = 0
        cls.item_pos = 0
        cls.set_aitem()

    @classmethod
    def set_aitem(cls):
        cls.a_item = []
        if I_MAGICAL_BOOMERANG in cls.item:
            cls.a_item.append(I_MAGICAL_BOOMERANG)
        elif I_BOOMERANG in cls.item:
            cls.a_item.append(I_BOOMERANG)
        if I_BOMB in cls.item:
            cls.a_item.append(I_BOMB)
        if I_BOW in cls.item:
            if I_SILVER_ARROW in cls.item:
                cls.a_item.append(M2_BOW_SILVER_ARROW)
            elif I_ARROW in cls.item:
                cls.a_item.append(M2_BOW_ARROW)
            else:
                cls.a_item.append(I_BOW)
        else:
            if I_SILVER_ARROW in cls.item:
                cls.a_item.append(I_SILVER_ARROW)
            elif I_ARROW in cls.item:
                cls.a_item.append(I_ARROW)
        if I_RED_CANDLE in cls.item:
            cls.a_item.append(I_RED_CANDLE)
        elif I_BLUE_CANDLE in cls.item:
            cls.a_item.append(I_BLUE_CANDLE)
        if I_MAGICAL_ROD in cls.item:
            cls.a_item.append(I_MAGICAL_ROD)
        if I_RECORDER in cls.item:
            cls.a_item.append(I_RECORDER)
        if I_FOOD in cls.item:
            cls.a_item.append(I_FOOD)
        cls.selectitem()

    @classmethod
    def add(cls, additem):
        if additem==I_HEART_CONTAINER:
            pass
        elif additem==I_MOREBOMB:
            pass
        elif additem==I_LIFE_POTION:
            if I_LIFE_POTION in cls.item:
                cls.item.append(I_2ND_POTION)
            else:
                cls.item.append(I_LIFE_POTION)
        elif additem==I_2ND_POTION:
            if I_LIFE_POTION not in cls.item:
                cls.item.append(I_LIFE_POTION)
            cls.item.append(I_2ND_POTION)
        elif additem not in cls.item:
            cls.item.append(additem)
        cls.set_aitem()

    @classmethod
    def selectitem(cls):
        if cls.a_item:
            cls.selected_item = cls.a_item[cls.item_pos]

    @classmethod
    def changeitem(cls):
        cls.item_pos += 1
        if cls.item_pos>=len(cls.a_item):
            cls.item_pos = 0
        cls.selectitem()

    @classmethod
    def relife(cls):
        if I_2ND_POTION in cls.item:
            cls.item.remove(I_2ND_POTION)
            if I_LIFE_POTION not in cls.item:
                cls.item.append(I_LIFE_POTION)
            return I_2ND_POTION
        elif I_LIFE_POTION in cls.item:
            cls.item.remove(I_LIFE_POTION)
            return I_LIFE_POTION
        return 0

    @classmethod
    def draw(cls):
        bx = 54
        pyxel.blt(bx, 2, 0, 240, 64, 16, 16, 1)  # B-Cursor
        if W_MAGICAL_SWORD in cls.item:
            pyxel.blt(bx+5, 2, 0, 16, 64, 8, 16, 1)
        elif W_WHITE_SWORD in cls.item:
            pyxel.blt(bx+5, 2, 0, 8, 64, 8, 16, 1)
        elif W_SWORD in cls.item:
            pyxel.blt(bx+5, 2, 0, 0, 64, 8, 16, 1)
        ax = 74
        pyxel.blt(ax+16*cls.item_pos, 2, 0, 224, 64, 16, 16, 1)  # A-Cursor
        if I_MAGICAL_BOOMERANG in cls.item:
            pyxel.blt(ax+5, 2, 0, 32, 64, 8, 16, 1)
            ax += 16
        elif I_BOOMERANG in cls.item:
            pyxel.blt(ax+5, 2, 0, 24, 64, 8, 16, 1)
            ax += 16
        if I_BOMB in cls.item:
            pyxel.blt(ax+4, 3, 0, 40, 64, 8, 16, 1)
            ax += 16
        arw = False
        if I_SILVER_ARROW in cls.item:
            pyxel.blt(ax+3, 2, 0, 56, 64, 5, 16, 1)
            arw = True
        elif  I_ARROW in cls.item:
            pyxel.blt(ax+3, 2, 0, 48, 64, 5, 16, 1)
            arw = True
        if I_BOW in cls.item:
            pyxel.blt(ax+8, 2, 0, 64, 64, 8, 16, 1)
            arw = True
        if arw:
            ax += 16
        if I_RED_CANDLE in cls.item:
            pyxel.blt(ax+4, 2, 0, 80, 64, 8, 16, 1)
            ax += 16
        elif I_BLUE_CANDLE in cls.item:
            pyxel.blt(ax+4, 2, 0, 72, 64, 8, 16, 1)
            ax += 16
        if I_MAGICAL_ROD in cls.item:
            pyxel.blt(ax+6, 2, 0, 92, 64, 4, 16, 1)
            ax += 16
        if I_RECORDER in cls.item:
            pyxel.blt(ax+7, 2, 0, 88, 64, 4, 16, 1)
            ax += 16
        if I_FOOD in cls.item:
            pyxel.blt(ax+4, 2, 0, 96, 64, 8, 16, 1)
            ax += 16
        cx = 200
        if I_2ND_POTION in cls.item:
            pyxel.blt(cx, 2, 0, 120, 64, 8, 16, 1)
            cx += 10
        elif I_LIFE_POTION in cls.item:
            pyxel.blt(cx, 2, 0, 112, 64, 8, 16, 1)
            cx += 10
        elif I_LETTER in cls.item:
            pyxel.blt(cx, 2, 0, 104, 64, 8, 16, 1)
            cx += 10
        if I_RED_RING in cls.item:
            pyxel.blt(cx, 2, 0, 136, 64, 8, 16, 1)
            cx += 10
        elif I_BLUE_RING in cls.item:
            pyxel.blt(cx, 2, 0, 128, 64, 8, 16, 1)
            cx += 10
        if I_POWER_BRACELET in cls.item:
            pyxel.blt(cx, 2, 0, 144, 64, 8, 16, 1)
            cx += 10
        if I_BIBLE in cls.item:
            pyxel.blt(cx, 2, 0, 152, 64, 8, 16, 1)

class BaseMove:
    def canmove(self, x, y, dirc, dst=2, rng=0):  # 16x16
        ix, iy = x, y
        if dirc==UP:
            x = (x//8)*8 if x%8<4 else (x//8+1)*8  # 8n倍に
            if y-dst>=16*rng and Map.zmap[x//16][(y-dst)//16]==MP_NONE and Map.zmap[(x+15)//16][(y-dst)//16]==MP_NONE:
                y -= dst
                return True, x, y
        elif dirc==DOWN:
            x = (x//8)*8 if x%8<4 else (x//8+1)*8  # 8n倍に
            if y+15+dst<(MAP_SIZE_Y-rng)*16 and Map.zmap[x//16][(y+15+dst)//16]==MP_NONE and Map.zmap[(x+15)//16][(y+15+dst)//16]==MP_NONE:
                y += dst
                return True, x, y
        elif dirc==LEFT:
            y = (y//8)*8 if y%8<4 else (y//8+1)*8  # 8n倍に
            if x-dst>=16*rng and Map.zmap[(x-dst)//16][y//16]==MP_NONE and Map.zmap[(x-dst)//16][(y+15)//16]==MP_NONE:
                x -= dst
                return True, x, y
        elif dirc==RIGHT:
            y = (y//8)*8 if y%8<4 else (y//8+1)*8  # 8n倍に
            if x+15+dst<(MAP_SIZE_X-rng)*16 and Map.zmap[(x+15+dst)//16][y//16]==MP_NONE and Map.zmap[(x+15+dst)//16][(y+15)//16]==MP_NONE:
                x += dst
                return True, x, y
        return False, ix, iy

    def canshoot(self, x, y, w, h, dirc, dst=4, rng=0):
        if dirc==UP:
            if y-dst>=16*rng and Map.zmap[x//16][(y-dst)//16]==MP_NONE and Map.zmap[(x+w-1)//16][(y-dst)//16]==MP_NONE:
                y -= dst
                return True, x, y
        elif dirc==DOWN:
            if y+h-1+dst<(MAP_SIZE_Y-rng)*16 and Map.zmap[x//16][(y+h-1+dst)//16]==MP_NONE and Map.zmap[(x+w-1)//16][(y+h-1+dst)//16]==MP_NONE:
                y += dst
                return True, x, y
        elif dirc==LEFT:
            if x-dst>=16*rng and Map.zmap[(x-dst)//16][y//16]==MP_NONE and Map.zmap[(x-dst)//16][(y+h-1)//16]==MP_NONE:
                x -= dst
                return True, x, y
        elif dirc==RIGHT:
            if x+w-1+dst<(MAP_SIZE_X-rng)*16 and Map.zmap[(x+w-1+dst)//16][y//16]==MP_NONE and Map.zmap[(x+w-1+dst)//16][(y+h-1)//16]==MP_NONE:
                x += dst
                return True, x, y
        return False, x, y

    def movefree(self, x, y, w, h, dirc, dst=4, rng=0):
        if dirc==UP:
            if y-dst>=16*rng:
                y -= dst
                return True, x, y
        elif dirc==DOWN:
            if y+h-1+dst<(MAP_SIZE_Y-rng)*16:
                y += dst
                return True, x, y
        elif dirc==LEFT:
            if x-dst>=16*rng:
                x -= dst
                return True, x, y
        elif dirc==RIGHT:
            if x+w-1+dst<(MAP_SIZE_X-rng)*16:
                x += dst
                return True, x, y
        return False, x, y

class Sword():
    atk_x, atk_y, atk_w, atk_h, atk_dir, atk_dmg = 0, 0, 0, 0, NO_DIR, 0
    def __init__(self, x, y, dirc):
        self.x, self.y = x, y
        self.dirc = dirc
        if W_MAGICAL_SWORD in Item.item:
            Sword.atk_dmg = 4
        elif W_WHITE_SWORD in Item.item:
            Sword.atk_dmg = 2
        else:
            Sword.atk_dmg = 1
        self.cnt = 8
        Player.atk_posture_cnt = 8
        self.set_atk_range()
    
    def __del__(self):
        self.set_atk_range()

    @classmethod
    def hit(cls, x, y, w, h):
        if Sword.atk_x-w<x<Sword.atk_x+Sword.atk_w and Sword.atk_y-h<y<Sword.atk_y+Sword.atk_h:
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR):
        Sword.atk_x, Sword.atk_y, Sword.atk_w, Sword.atk_h, Sword.atk_dir = x, y, w, h, dirc
    
    def update(self):
        self.cnt -= 1
        if self.cnt==0:
            self.set_atk_range()
            return RET_DEL
        if self.dirc==UP:
            self.set_atk_range(self.x+3, self.y-12, 7, 12, self.dirc)
        elif self.dirc==DOWN:
            self.set_atk_range(self.x+5, self.y+16, 7, 12, self.dirc)
        elif self.dirc==LEFT:
            self.set_atk_range(self.x-12, self.y+6, 12, 7, self.dirc)
        elif self.dirc==RIGHT:
            self.set_atk_range(self.x+16, self.y+6, 12, 7, self.dirc)
        return RET_NONE

    def draw(self, player_x, player_y, player_dirc):
        Draw.sword(player_x, player_y, player_dirc, swd=self.cnt)

class SwordBeam(BaseMove):
    atk_x, atk_y, atk_w, atk_h, atk_dir, atk_dmg, hitted = 0, 0, 0, 0, NO_DIR, 0, True
    def __init__(self, x, y, dirc):
        if dirc==UP:
            self.x, self.y = x+3, y-16
        elif dirc==DOWN:
            self.x, self.y = x+5, y+16
        elif dirc==LEFT:
            self.x, self.y = x-16, y+6
        elif dirc==RIGHT:
            self.x, self.y = x+16, y+6
        self.dirc = dirc
        if W_MAGICAL_SWORD in Item.item:
            SwordBeam.atk_dmg = 4
        elif W_WHITE_SWORD in Item.item:
            SwordBeam.atk_dmg = 2
        else:
            SwordBeam.atk_dmg = 1
        self.cnt = 0
        self.refl = 0
        self.set_atk_range()
        SwordBeam.hitted = False

    def __del__(self):
        self.set_atk_range()
        SwordBeam.hitted = True

    @classmethod
    def hit(cls, x, y, w, h):
        if SwordBeam.atk_x-w<x<SwordBeam.atk_x+SwordBeam.atk_w and SwordBeam.atk_y-h<y<SwordBeam.atk_y+SwordBeam.atk_h:
            SwordBeam.hitted = True
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR):
        SwordBeam.atk_x, SwordBeam.atk_y, SwordBeam.atk_w, SwordBeam.atk_h, SwordBeam.atk_dir = x, y, w, h, dirc

    def update(self):
        self.cnt += 1
        if self.refl:
            self.refl -= 1
            if self.refl==0:
                return RET_DEL
        else:
            if self.dirc in (UP, DOWN):
                ret, self.x, self.y = self.movefree(self.x, self.y, 7, 16, self.dirc, 4)
                self.set_atk_range(self.x, self.y, 7, 16, self.dirc)
            elif self.dirc in (LEFT, RIGHT):
                ret, self.x, self.y = self.movefree(self.x, self.y, 16, 7, self.dirc, 4)
                self.set_atk_range(self.x, self.y, 16, 7, self.dirc)
            if not ret or SwordBeam.hitted:
                self.set_atk_range()
                if self.dirc==DOWN:
                    self.y += 7
                elif self.dirc==RIGHT:
                    self.x += 8
                self.refl = 12
        return RET_NONE

    def draw(self):
        if self.refl:
            Draw.sword_reflection(self.x, self.y, 30-self.refl*2, self.cnt%4)
        else:
            Draw.sword(self.x, self.y, self.dirc, tp=self.cnt%4+1)

class Boomerang(BaseMove):
    atk_x, atk_y, atk_w, atk_h, atk_dir, hitted = 0, 0, 0, 0, NO_DIR, True
    def __init__(self, x, y, dirc, magical=False):
        if dirc==UP:
            self.x, self.y = x+4, y-4
        elif dirc==DOWN:
            self.x, self.y = x+4, y+16
        elif dirc==LEFT:
            self.x, self.y = x-4, y+4
        elif dirc==RIGHT:
            self.x, self.y = x+16, y+4
        self.dirc = dirc
        self.magical = magical
        self.cnt = 0
        Player.atk_posture_cnt = 4
        self.set_atk_range()
        Boomerang.hitted = False

    def __del__(self):
        self.set_atk_range()
        Boomerang.hitted = True

    @classmethod
    def hit(cls, x, y, w, h):
        if Boomerang.atk_x-w<x<Boomerang.atk_x+Boomerang.atk_w and Boomerang.atk_y-h<y<Boomerang.atk_y+Boomerang.atk_h:
            Boomerang.hitted = True
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR):
        Boomerang.atk_x, Boomerang.atk_y, Boomerang.atk_w, Boomerang.atk_h, Boomerang.atk_dir = x, y, w, h, dirc

    def update(self, player_x, player_y):
        self.cnt += 1
        dxy = (5 if self.magical else 4)
        if self.cnt<=(24 if self.magical else 16):
            ret, self.x, self.y = self.movefree(self.x, self.y, 8, 8, self.dirc, dxy)
            if not ret or Boomerang.hitted:
                self.cnt = 100
        elif self.cnt<=(28 if self.magical else 20):
            pass
        else:
            dx = player_x+4-self.x
            dy = player_y+4-self.y
            if self.dirc in (UP, DOWN):
                self.y += pyxel.sgn(dy)*dxy
                if dx*pyxel.sgn(dx)*2>=dy*pyxel.sgn(dy):
                    self.x += pyxel.sgn(dx)*dxy
            if self.dirc in (LEFT, RIGHT):
                self.x += pyxel.sgn(dx)*dxy
                if dy*pyxel.sgn(dy)*2>=dx*pyxel.sgn(dx):
                    self.y += pyxel.sgn(dy)*dxy
            if Boomerang.hit(player_x, player_y, 16, 16):
                self.set_atk_range()
                return RET_DEL
        self.set_atk_range(self.x, self.y, 8, 8, self.dirc)
        return RET_NONE

    def draw(self):
        Draw.boomerang(self.x, self.y, self.cnt, self.magical)

class Bomb(BaseMove):
    atk_x, atk_y, atk_w, atk_h, atk_dir,putbomb = 0, 0, 0, 0, NO_DIR, False
    def __init__(self, x, y, dirc):
        if dirc==UP:
            self.x, self.y = x+4, y-16
        elif dirc==DOWN:
            self.x, self.y = x+4, y+16
        elif dirc==LEFT:
            self.x, self.y = x-12, y
        elif dirc==RIGHT:
            self.x, self.y = x+20, y
        self.dirc = dirc
        self.cnt = 46
        Player.atk_posture_cnt = 4
        self.SMOKE_PTN = (((-1,-2),(2,0),(1,2)), ((1,-2),(-2,0),(-1,2)))
        self.ptn = pyxel.rndi(0,1)
        self.set_atk_range(self.x, self.y, 8, 16, putb=True)

    def __del__(self):
        self.set_atk_range()

    @classmethod
    def hit(cls, x, y, w, h):
        if not Bomb.putbomb and Bomb.atk_x-w<x<Bomb.atk_x+Bomb.atk_w and Bomb.atk_y-h<y<Bomb.atk_y+Bomb.atk_h:
            return True
        return False

    @classmethod
    def bombhit(cls, x, y, w, h):
        if Bomb.putbomb and Bomb.atk_x-w<x<Bomb.atk_x+Bomb.atk_w and Bomb.atk_y-h<y<Bomb.atk_y+Bomb.atk_h:
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR,  putb=False):
        Bomb.atk_x, Bomb.atk_y, Bomb.atk_w, Bomb.atk_h, Bomb.atk_dir, Bomb.putbomb = x, y, w, h, dirc, putb

    def update(self):
        self.cnt -= 1
        if self.cnt==16:
            self.set_atk_range(self.x-12, self.y-12, 40, 40)
        elif self.cnt==0:
            self.set_atk_range()
            return RET_DEL
        return RET_NONE

    def draw(self):
        if self.cnt<=16:
            Draw.smoke(self.x-4, self.y, self.cnt)
            for dx,dy in self.SMOKE_PTN[self.ptn]:
                Draw.smoke(self.x-4+dx*8, self.y+dy*8, self.cnt)
        else:
            Draw.bomb(self.x, self.y)

class Arrow(BaseMove):
    atk_x, atk_y, atk_w, atk_h, atk_dir, atk_dmg, hitted = 0, 0, 0, 0, NO_DIR, 0, True
    def __init__(self, x, y, dirc, silver=False):
        if dirc==UP:
            self.x, self.y = x+6, y-16
        elif dirc==DOWN:
            self.x, self.y = x+5, y+16
        elif dirc==LEFT:
            self.x, self.y = x-16, y+7
        elif dirc==RIGHT:
            self.x, self.y = x+16, y+7
        self.dirc = dirc
        self.silver = silver
        if silver:
            Arrow.atk_dmg = 4
        else:
            Arrow.atk_dmg = 2
        Player.atk_posture_cnt = 4
        self.refl = 0
        self.set_atk_range()
        Arrow.hitted = False

    def __del__(self):
        self.set_atk_range()
        Arrow.hitted = True

    @classmethod
    def hit(cls, x, y, w, h):
        if Arrow.atk_x-w<x<Arrow.atk_x+Arrow.atk_w and Arrow.atk_y-h<y<Arrow.atk_y+Arrow.atk_h:
            Arrow.hitted = True
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR):
        Arrow.atk_x, Arrow.atk_y, Arrow.atk_w, Arrow.atk_h, Arrow.atk_dir = x, y, w, h, dirc

    def update(self):
        if self.refl:
            self.refl -= 1
            if self.refl==0:
                return RET_DEL
        else:
            if self.dirc in (UP, DOWN):
                ret, self.x, self.y = self.movefree(self.x, self.y, 5, 16, self.dirc, 5)
                self.set_atk_range(self.x, self.y, 5, 16, self.dirc)
            elif self.dirc in (LEFT, RIGHT):
                ret, self.x, self.y = self.movefree(self.x, self.y, 16, 5, self.dirc, 5)
                self.set_atk_range(self.x, self.y, 16, 5, self.dirc)
            if not ret or Arrow.hitted:
                self.set_atk_range()
                if self.dirc==LEFT:
                    self.y -= 1
                elif self.dirc==RIGHT:
                    self.x += 8
                    self.y -= 1
                elif self.dirc==UP:
                    self.x += -1
                elif self.dirc==DOWN:
                    self.x += -1
                    self.y += 5
                self.refl = 8
        return RET_NONE

    def draw(self):
        if self.refl:
            Draw.arrow_reflection(self.x, self.y)
        else:
            Draw.arrow(self.x, self.y, self.dirc, self.silver)

class Rod(BaseMove):
    atk_x, atk_y, atk_w, atk_h, atk_dir, atk_dmg, hitted = 0, 0, 0, 0, NO_DIR, 2, True
    def __init__(self, x, y, dirc, bible=False):
        if dirc==UP:
            self.x, self.y = x, y-20 
        elif dirc==DOWN:
            self.x, self.y = x, y+20
        elif dirc==LEFT:
            self.x, self.y = x-20, y
        elif dirc==RIGHT:
            self.x, self.y = x+20, y
        self.dirc = dirc
        self.bible = bible
        self.cnt = 0
        self.flame_cnt = 0
        Player.atk_posture_cnt = 8
        self.set_atk_range()
        Rod.hitted = False

    def __del__(self):
        self.set_atk_range()
        Rod.hitted = True

    @classmethod
    def hit(cls, x, y, w, h):
        if Rod.atk_x-w<x<Rod.atk_x+Rod.atk_w and Rod.atk_y-h<y<Rod.atk_y+Rod.atk_h:
            Rod.hitted = True
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR):
        Rod.atk_x, Rod.atk_y, Rod.atk_w, Rod.atk_h, Rod.atk_dir = x, y, w, h, dirc

    def update(self):
        self.cnt += 1
        if self.flame_cnt and self.bible:
            self.flame_cnt -= 1
            if self.flame_cnt==0:
                self.set_atk_range()
                return RET_DEL
        else:
            ret, self.x, self.y = self.movefree(self.x, self.y, 16, 16, self.dirc, 5)
            if not ret or Rod.hitted:
                if self.bible:
                    self.flame_cnt = 16
                else:
                    self.set_atk_range()
                    return RET_DEL
        self.set_atk_range(self.x, self.y, 16, 16, self.dirc)
        return RET_NONE

    def draw(self, rx, ry):
        if self.flame_cnt:
            Draw.flame(self.x, self.y, self.cnt//4%2)
        else:
            if self.cnt<=8:
                if self.dirc==UP:
                    rx, ry = rx+5, ry-11 
                elif self.dirc==DOWN:
                    rx, ry = rx+7, ry+11
                elif self.dirc==LEFT:
                    rx, ry = rx-11, ry+8
                elif self.dirc==RIGHT:
                    rx, ry = rx+11, ry+8
                Draw.rod(rx, ry, self.dirc)
            Draw.rodbeam(self.x, self.y, self.dirc, self.cnt)

class Candle(BaseMove):
    atk_x, atk_y, atk_w, atk_h, atk_dir, atk_dmg = 0, 0, 0, 0, NO_DIR, 1
    def __init__(self, x, y, dirc):
        if dirc==UP:
            self.x, self.y = x, y-16
        elif dirc==DOWN:
            self.x, self.y = x, y+16
        elif dirc==LEFT:
            self.x, self.y = x-16, y
        elif dirc==RIGHT:
            self.x, self.y = x+16, y
        self.dirc = dirc
        self.cnt = 32
        Player.atk_posture_cnt = 4
        self.set_atk_range()

    def __del__(self):
        self.set_atk_range()

    @classmethod
    def hit(cls, x, y, w, h):
        if Candle.atk_x-w<x<Candle.atk_x+Candle.atk_w and Candle.atk_y-h<y<Candle.atk_y+Candle.atk_h:
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR):
        Candle.atk_x, Candle.atk_y, Candle.atk_w, Candle.atk_h, Candle.atk_dir = x, y, w, h, dirc

    def update(self):
        self.cnt -= 1
        if self.cnt>16:
            ret, self.x, self.y = self.movefree(self.x, self.y, 16, 16, self.dirc, 1)
            if not ret:
                self.cnt=16
        if self.cnt==0:
            self.set_atk_range()
            return RET_DEL
        self.set_atk_range(self.x, self.y, 16, 16, self.dirc)
        return RET_NONE

    def draw(self):
        Draw.flame(self.x, self.y, self.cnt//4%2)

class Food(BaseMove):
    atk_x, atk_y, atk_w, atk_h, atk_dir = 0, 0, 0, 0, NO_DIR
    def __init__(self, x, y, dirc):
        if dirc==UP:
            self.x, self.y = x+4, y-16
        elif dirc==DOWN:
            self.x, self.y = x+4, y+16
        elif dirc==LEFT:
            self.x, self.y = x-12, y
        elif dirc==RIGHT:
            self.x, self.y = x+20, y
        self.dirc = dirc
        self.cnt = 600
        Player.atk_posture_cnt = 4
        self.set_atk_range()

    def __del__(self):
        self.set_atk_range()

    @classmethod
    def hit(cls, x, y, w, h):
        if Food.atk_x-w<x<Food.atk_x+Food.atk_w and Food.atk_y-h<y<Food.atk_y+Food.atk_h:
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=NO_DIR):
        Food.atk_x, Food.atk_y, Food.atk_w, Food.atk_h, Food.atk_dir = x, y, w, h, dirc

    def update(self):
        self.cnt -= 1
        if self.cnt==0:
            self.set_atk_range()
            return RET_DEL
        return RET_NONE

    def draw(self):
        Draw.food(self.x, self.y)

class Wind(BaseMove):
    atk_x, atk_y, atk_w, atk_h = 0, 0, 0, 0
    def __init__(self, x, y):
        self.x, self.y = 0, y
        self.smoke_cnt = 16
        self.cnt = 0
        self.set_atk_range()

    def __del__(self):
        self.set_atk_range()

    @classmethod
    def hit(cls, x, y, w, h):
        if Wind.atk_x-w<x<Wind.atk_x+Wind.atk_w and Wind.atk_y-h<y<Wind.atk_y+Wind.atk_h:
            return True
        return False

    def set_atk_range(self, x=0, y=0, w=0, h=0):
        Wind.atk_x, Wind.atk_y, Wind.atk_w, Wind.atk_h = x, y, w, h

    def update(self):
        if self.smoke_cnt:
            self.smoke_cnt -= 1
        else:
            self.cnt += 1
            ret, self.x, self.y = self.movefree(self.x, self.y, 16, 16, RIGHT, 4)
            if not ret:
                self.set_atk_range()
                return RET_DEL
            self.set_atk_range(self.x, self.y, 16, 16)
            return RET_NONE

    def draw(self):
        if self.smoke_cnt:
            Draw.smoke(self.x, self.y, self.smoke_cnt)
        else:
            Draw.wind(self.x, self.y, self.cnt)

class Player:
    atk_x, atk_y, atk_w, atk_h, atk_dir, atk_posture_cnt = 0, 0, 0, 0, DOWN, 0
    dmg_x, dmg_y, dmg_w, dmg_h, dmg_dir = 0, 0, 0, 0, DOWN
    def __init__(self, x, y):
        self.x, self.y, self.dirc = x, y, DOWN
        self.maxhp, self.hp, self.maxbomb, self.bomb, self.rupee = 24, 24, 0, 0, 0
        #self.maxhp, self.hp, self.maxbomb, self.bomb, self.rupee = 40, 40, 32, 32, 500  # ___DEBUG
        self.damaged_cnt = 0
        self.walk_cnt = 0
        self.hold_a, self.hold_b = False, False
        self.cavein_cnt, self.caveout_cnt = 0, 0
        self.getitem_cnt = 0
        self.saveprincess = 0
        self.gameover_cnt = 0
        self.appearitem = 0
        self.pushrock_cnt = 0
        self.windwarp = 0
        self.relife_cnt = 0

    def updown_hp(self, pt):
        self.hp += pt
        if self.hp>self.maxhp:
            self.hp = self.maxhp
        elif self.hp<=0:
            self.hp = 0
            pyxel.stop()
            self.gameover_cnt = GAMEOVER_WAIT  # roll+flash
            return False
        return True

    def updown_rupee(self, pt):
        self.rupee += pt
        if self.rupee<0:
            self.rupee = 0

    def updown_bomb(self, pt):
        self.bomb += pt
        if self.bomb>self.maxbomb:
            self.bomb = self.maxbomb
        elif self.bomb<0:
            self.bomb = 0

    @classmethod
    def hit(cls, x, y, w, h):
        return Player.dmg_x-w<x<Player.dmg_x+Player.dmg_w and Player.dmg_y-h<y<Player.dmg_y+Player.dmg_h

    def set_dmg_range(self, x, y):
        Player.dmg_x, Player.dmg_y, Player.dmg_w, Player.dmg_h = x+2, y+2, 12, 12
    
    def set_atk_range(self, x=0, y=0, w=0, h=0, dirc=DOWN):
        Player.atk_x, Player.atk_y, Player.atk_w, Player.atk_h, Player.atk_dir = x, y, w, h, dirc
    
    def playermove(self, x, y, dirc, dmg=False, dst=2):
        ix, iy = x, y
        if dirc==UP:
            x = (x//8)*8 if x%8<4 else (x//8+1)*8  # 8n倍に
            if y-dst<0 and not dmg:
                if Map.now_map==GLEEOK_MAP:
                    Map.setscroll(UP, PRINCESS_MAP)
                else:
                    Map.setscroll(UP)
                y = (MAP_SIZE_Y-1)*16
                return RET_SCROLL, x, y
            if y-dst>=0 and ((y-8)%16 or (Map.zmap[x//16][(y-dst)//16]==MP_NONE and Map.zmap[(x+15)//16][(y-dst)//16]==MP_NONE)):  # 障害物なし
                y -= dst
                return RET_MOVED, x, y
            elif y-dst>=0 and (y-8)%16==0 and x==Map.cave_x*16 and (y-dst)//16==Map.cave_y and Map.now_map in PSECRET_MAP and I_POWER_BRACELET in Item.item:
                self.pushrock_cnt += 1
                if self.pushrock_cnt==32:
                    return RET_UPROCK, ix, iy
        elif dirc==DOWN:
            x = (x//8)*8 if x%8<4 else (x//8+1)*8  # 8n倍に
            if y+dst>(MAP_SIZE_Y-1)*16 and not dmg:
                if Map.now_map in (GETITEM_MAP, DODONGO_MAP, TESTITART_MAP, DIGDOGGER_MAP, GOHMA_MAP, GLEEOK_MAP, PRINCESS_MAP):  # CAVE_OUT
                    if Map.now_map==GETITEM_MAP and Map.thismap_item==R_PAYRUPEE:
                        Map.thismap_item=R_PAIDRUPEE
                        self.updown_rupee(-30)
                    Map.caveout()
                    self.caveout_cnt = 16
                    return RET_CAVEOUT, Map.cave_x*16, Map.cave_y*16+16
                else:
                    Map.setscroll(DOWN)
                    y = 0
                    return RET_SCROLL, x, y
            if y+dst<=(MAP_SIZE_Y-1)*16 and (y%16 or (Map.zmap[x//16][(y+16+dst)//16]==MP_NONE and Map.zmap[(x+15)//16][(y+16+dst)//16]==MP_NONE)):  # 障害物なし
                y += dst
                return RET_MOVED, x, y
        elif dirc==LEFT:
            y = (y//8)*8 if y%8<4 else (y//8+1)*8  # 8n倍に
            if x-dst<0 and not dmg:
                Map.setscroll(LEFT)
                x = (MAP_SIZE_X-1)*16
                return RET_SCROLL, x, y
            if x-dst>=0 and (x%16 or Map.zmap[(x-dst)//16][(y+15)//16]==MP_NONE):  # 障害物なし
                x -= dst
                return RET_MOVED, x, y
            elif x-dst>=0 and x%16==0 and (x-dst)//16==Map.cave_x and y==Map.cave_y*16 and Map.now_map in PSECRET_MAP and I_POWER_BRACELET in Item.item:
                self.pushrock_cnt += 1
                if self.pushrock_cnt==32:
                    return RET_LEFTROCK, ix, iy
        elif dirc==RIGHT:
            y = (y//8)*8 if y%8<4 else (y//8+1)*8  # 8n倍に
            if x+dst>(MAP_SIZE_X-1)*16 and not dmg:
                Map.setscroll(RIGHT)
                x = 0
                return RET_SCROLL, x, y
            if x+dst<=(MAP_SIZE_X-1)*16 and (x%16 or Map.zmap[(x+16+dst)//16][(y+15)//16]==MP_NONE):  # 障害物なし
                x += dst
                return RET_MOVED, x, y
            elif x+dst<=(MAP_SIZE_X-1)*16 and x%16==0 and (x+16+dst)//16==Map.cave_x and y==Map.cave_y*16 and Map.now_map in PSECRET_MAP and I_POWER_BRACELET in Item.item:
                self.pushrock_cnt += 1
                if self.pushrock_cnt==32:
                    return RET_RIGHTROCK, ix, iy
        return RET_NONE, ix, iy

    def cavein(self):
        self.cavein_cnt -= 1
        if self.cavein_cnt==0:
            Map.cavein()
            self.x, self.y = CENTER_X, (MAP_SIZE_Y-1)*16  # 112, 160
            return True
        return False

    def caveout(self):
        self.caveout_cnt -= 1
        if self.caveout_cnt==0:
            return True
        return False

    def buttondown(self):
        ret = []
        if pyxel.btn(pyxel.KEY_SHIFT) or pyxel.btn(pyxel.KEY_X) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
            ret.append(A_BUTTON)
        if pyxel.btn(pyxel.KEY_CTRL) or pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_B):
            ret.append(B_BUTTON)
        if pyxel.btn(pyxel.KEY_TAB) or pyxel.btn(pyxel.KEY_C) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_X):
            ret.append(X_BUTTON)
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y):
            ret.append(Y_BUTTON)
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            ret.append(UP)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            ret.append(DOWN)
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            ret.append(LEFT)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            ret.append(RIGHT)
        return ret

    def update(self):
        if self.gameover_cnt:  # ゲームオーバー中
            self.gameover_cnt -= 1
            if self.gameover_cnt==1:
                itm = Item.relife() 
                if itm>0:  # 復活
                    self.hp = self.maxhp
                    self.gameover_cnt = 0
                    self.relife_cnt = 50
                    self.newitem = itm
                    return RET_RELIFE
                else:
                    return RET_GAMEOVER
            return RET_NONE
        if self.relife_cnt:  # 復活中
            self.relife_cnt -= 1
            if self.relife_cnt==0:
                self.damaged_cnt = 0
            return RET_NONE
        if Player.atk_posture_cnt:  # 攻撃中
            Player.atk_posture_cnt -= 1
        btndown = self.buttondown()
        if B_BUTTON in btndown and self.x!=0 and self.x!=(MAP_SIZE_X-1)*16 and self.y!=0 and self.y!=(MAP_SIZE_Y-1)*16:
            if not self.hold_a and Player.atk_posture_cnt==0 and (W_SWORD in Item.item or W_WHITE_SWORD in Item.item or W_MAGICAL_SWORD in Item.item):
                self.hold_a = True
                return RET_USEWEAPON
        else:
            self.hold_a = False
        if A_BUTTON in btndown and self.x!=0 and self.x!=(MAP_SIZE_X-1)*16 and self.y!=0 and self.y!=(MAP_SIZE_Y-1)*16:
            if not self.hold_b and Player.atk_posture_cnt==0:
                self.hold_b = True
                return RET_USEITEM
        else:
            self.hold_b = False
        self.set_atk_range()
        if self.damaged_cnt:  # 攻撃を受けている
            self.damaged_cnt -= 1
            if self.damaged_cnt>=PLAYER_DAMAGE_WAIT-8:
                _, self.x, self.y = self.playermove(self.x, self.y, Player.dmg_dir, True)
                _, self.x, self.y = self.playermove(self.x, self.y, Player.dmg_dir, True)
        ret = RET_NONE
        if Player.atk_posture_cnt:  # 攻撃中
            pass
        elif self.getitem_cnt:  # アイテム取得中
            self.getitem_cnt -= 1
            if self.getitem_cnt==0:
                if self.newitem==R_GETRUPEE100:
                    self.updown_rupee(100)
                elif self.newitem==R_GETRUPEE30:
                    self.updown_rupee(30)
                elif self.newitem==R_PAYRUPEE:
                    self.updown_rupee(-30)
                else:
                    Item.add(self.newitem)
        elif self.windwarp==0 and Wind.hit(self.x, self.y, 16, 16):
            self.windwarp = 1  # 旧マップでワープ中
        else:  #　攻撃していない＋アイテム取得中でない＝移動できる
            if UP in btndown:
                self.dirc = UP
                if self.damaged_cnt<PLAYER_DAMAGE_WAIT-8:
                    ret, self.x, self.y = self.playermove(self.x, self.y, self.dirc)
            elif DOWN in btndown:
                self.dirc = DOWN
                if self.damaged_cnt<PLAYER_DAMAGE_WAIT-8:
                    ret, self.x, self.y = self.playermove(self.x, self.y, self.dirc)
            elif LEFT in btndown:
                self.dirc = LEFT
                if self.damaged_cnt<PLAYER_DAMAGE_WAIT-8:
                    ret, self.x, self.y = self.playermove(self.x, self.y, self.dirc)
            elif RIGHT in btndown:
                self.dirc = RIGHT
                if self.damaged_cnt<PLAYER_DAMAGE_WAIT-8:
                    ret, self.x, self.y = self.playermove(self.x, self.y, self.dirc)
            if ret==RET_MOVED:
                self.walk_cnt += 1
                self.pushrock_cnt = 0
            if self.x==Map.cave_x*16 and self.y==Map.cave_y*16:
                ret = RET_CAVEIN
                self.cavein_cnt = 16
            elif self.appearitem and self.x==CENTER_X and self.y==CENTER_Y:
                if self.appearitem==I_HEART_CONTAINER:
                    self.maxhp += 8
                elif self.appearitem==I_MOREBOMB:
                    self.maxbomb += 4
                    self.updown_bomb(4)
                ret = RET_GETITEM
                self.newitem = self.appearitem
                self.appearitem = 0
                self.getitem_cnt = 50
            elif Map.now_map==GETITEM_MAP:
                finproc = False
                if Map.thismap_item==W_SWORD:  # ヒトリデハキケンジャ
                    if self.x==NEWITEM_X2 and self.y==NEWITEM_Y:
                        self.newitem = W_SWORD
                        self.updown_rupee(FIRST_GET_RUPEE)
                        finproc = True
                elif Map.thismap_item==R_PAYRUPEE:  # ドアノシュウリダイ
                    if self.x==NEWITEM_X2 and self.y==NEWITEM_Y:
                        ret = RET_GETITEM
                        self.newitem = R_PAYRUPEE
                        Map.thismap_item = R_PAIDRUPEE
                        self.getitem_cnt = 50
                elif Map.thismap_item==R_PAIDRUPEE:  # モウコワサナイデクレヨ
                    pass
                elif Map.thismap_item in (R_GETRUPEE100, R_GETRUPEE30):  # ミンナニナイショダヨ
                    if self.x==NEWITEM_X2 and self.y==NEWITEM_Y:
                        self.newitem = Map.thismap_item
                        finproc = True
                elif Map.thismap_item==S3_SHOP1:  # ナンカコウテクレヤ
                    if self.x==NEWITEM_X1 and self.y==NEWITEM_Y and self.rupee>=60 and I_BLUE_CANDLE not in Item.item:
                        self.newitem = I_BLUE_CANDLE
                        self.updown_rupee(-60)
                        finproc = True
                    elif self.x==NEWITEM_X2 and self.y==NEWITEM_Y and self.rupee>=20 and I_BOMB not in Item.item:
                        self.newitem = I_BOMB
                        self.maxbomb = 8
                        self.updown_bomb(4)
                        self.updown_rupee(-20)
                        finproc = True
                    elif self.x==NEWITEM_X3 and self.y==NEWITEM_Y and self.rupee>=80 and I_ARROW not in Item.item:
                        self.newitem = I_ARROW
                        self.updown_rupee(-80)
                        finproc = True
                elif Map.thismap_item==S3_SHOP2:  # コレハネウチモノデッセ
                    if self.x==NEWITEM_X1 and self.y==NEWITEM_Y and self.rupee>=90 and I_MAGICAL_ROD not in Item.item:  # I_MAGICAL_SHIELD(90)
                        self.newitem = I_MAGICAL_ROD
                        self.updown_rupee(-90)
                        finproc = True
                    elif self.x==NEWITEM_X2 and self.y==NEWITEM_Y and self.rupee>=250 and I_BLUE_RING not in Item.item:
                        self.newitem = I_BLUE_RING
                        self.updown_rupee(-250)
                        finproc = True
                    elif self.x==NEWITEM_X3 and self.y==NEWITEM_Y and self.rupee>=60 and self.maxhp<MAX_LIFE:  # I_FOOD(60)
                        self.newitem = I_HEART_CONTAINER
                        self.maxhp += 8
                        self.updown_rupee(-60)
                        finproc = True
                elif Map.thismap_item==I_MOREBOMB:  # バクダンヲモット
                    if self.x==NEWITEM_X2 and self.y==NEWITEM_Y and self.rupee>=100:
                        self.newitem = I_MOREBOMB
                        self.maxbomb += 4
                        self.updown_bomb(4)
                        self.updown_rupee(-100)
                        finproc = True
                elif Map.thismap_item==I2_2NDPOTION_HEARTCONTAINER:  # スキナホウヲサズケヨウ
                    if self.x==NEWITEM_X1 and self.y==NEWITEM_Y and I_2ND_POTION not in Item.item:
                        self.newitem = I_2ND_POTION
                        finproc = True
                    elif self.x==NEWITEM_X3 and self.y==NEWITEM_Y and self.maxhp<MAX_LIFE:
                        self.newitem = I_HEART_CONTAINER
                        self.maxhp += 8
                        finproc = True
                elif Map.thismap_item==I2_LIFEPOTION_2NDPOTION:  # クスリヲカッテユキナサイ
                    if self.x==NEWITEM_X1 and self.y==NEWITEM_Y and I_LETTER in Item.item and I_2ND_POTION not in Item.item and self.rupee>=40:
                        self.newitem = I_LIFE_POTION
                        self.updown_rupee(-40)
                        finproc = True
                    elif self.x==NEWITEM_X3 and self.y==NEWITEM_Y and I_LETTER in Item.item and I_2ND_POTION not in Item.item and self.rupee>=68:
                        self.newitem = I_2ND_POTION
                        self.updown_rupee(-68)
                        finproc = True
                elif Map.thismap_item==W_WHITE_SWORD:  # ツカイコナセルナラ
                    if self.x==NEWITEM_X2 and self.y==NEWITEM_Y and self.maxhp>=32:
                        self.newitem = Map.thismap_item
                        finproc = True
                elif Map.thismap_item==W_MAGICAL_SWORD:
                    if self.x==NEWITEM_X2 and self.y==NEWITEM_Y and self.maxhp>=40:
                        self.newitem = Map.thismap_item
                        finproc = True
                elif Map.thismap_item==I_RED_RING:
                    if self.x==NEWITEM_X2 and self.y==NEWITEM_Y and self.maxhp>=40:
                        self.newitem = Map.thismap_item
                        finproc = True
                elif Map.thismap_item and self.x==NEWITEM_X2 and self.y==NEWITEM_Y:  # その他
                    self.newitem = Map.thismap_item
                    finproc = True
                if finproc:
                    ret = RET_GETITEM
                    Map.thismap_item = 0
                    self.getitem_cnt = 50
            elif Map.now_map==PRINCESS_MAP and self.x==PERSON_X*16 and self.y==PERSON_Y*16+16:  # SAVE_PRINCESS
                ret = RET_SAVEPRINCESS
                self.saveprincess = 1
        self.set_dmg_range(self.x, self.y)
        return ret

    def draw(self):
        c = self.walk_cnt//2%2
        if self.gameover_cnt:
            if self.gameover_cnt<=16*4+2:
                if self.gameover_cnt>1:
                    Draw.flash(self.x, self.y, (self.gameover_cnt-2)//4)
            else:
                dirc = self.gameover_cnt//4%4
                ptn = self.gameover_cnt//4%2
                if dirc==3:
                    Draw.player(self.x, self.y, UP, ptn=ptn)
                elif dirc==2:
                    Draw.player(self.x, self.y, RIGHT, ptn=ptn)
                elif dirc==1:
                    Draw.player(self.x, self.y, DOWN, ptn=ptn)
                else:
                    Draw.player(self.x, self.y, LEFT, ptn=ptn)
        elif self.windwarp:
            pass
        elif self.saveprincess:
            Draw.player(PERSON_X*16+8, PERSON_Y*16, DOWN)
        elif self.cavein_cnt:
            Draw.player(self.x, self.y+(16-self.cavein_cnt), self.dirc, self.cavein_cnt//2%2, h=16-(16-self.cavein_cnt)-1)
        elif self.caveout_cnt:
            Draw.player(self.x, self.y-self.caveout_cnt, DOWN, self.caveout_cnt//2%2)
        elif self.getitem_cnt or self.relife_cnt:
            Draw.item(self.x, self.y-16, self.newitem)
            Draw.player(self.x, self.y, self.dirc, itm=True)
        elif self.damaged_cnt//2%2:
            pass
        else:
            if self.appearitem:
                Draw.item(CENTER_X, CENTER_Y, self.appearitem, align=True)
            Draw.player(self.x, self.y, self.dirc, ptn=c, swd=Player.atk_posture_cnt)

class Rupee:
    name = D_RUPEE
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cnt = 160

    def update(self):
        self.cnt -= 1
        if self.cnt==0:
            return RET_DISAPPEAR
        elif Player.hit(self.x, self.y, 8, 8) or Sword.hit(self.x, self.y, 8, 8) or Boomerang.hit(self.x, self.y, 8, 8):
            return RET_PLAYER_HIT
        return RET_NONE

    def draw(self):
        Draw.rupee(self.x, self.y, self.cnt//4%2)

class FiveRupees(Rupee):
    name = D_5RUPEES
    def draw(self):
        Draw.rupee(self.x, self.y, 1)

class Heart:
    name = D_HEART
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cnt = 160

    def update(self):
        self.cnt -= 1
        if self.cnt==0:
            return RET_DISAPPEAR
        elif Player.hit(self.x, self.y, 8, 8) or Sword.hit(self.x, self.y, 8, 8) or Boomerang.hit(self.x, self.y, 8, 8):
            return RET_PLAYER_HIT
        return RET_NONE

    def draw(self):
        Draw.heart(self.x, self.y, self.cnt//4%2)

class DropBomb:
    name = D_BOMB
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cnt = 160

    def update(self):
        self.cnt -= 1
        if self.cnt==0:
            return RET_DISAPPEAR
        elif Player.hit(self.x, self.y, 8, 8) or Sword.hit(self.x, self.y, 8, 8) or Boomerang.hit(self.x, self.y, 8, 8):
            return RET_PLAYER_HIT
        return RET_NONE

    def draw(self):
        Draw.bomb(self.x, self.y)

class EnemyDamage:
    def damage(self, x, y, w, h, incbomb=True):
        if Sword.hit(x, y, w, h):  # ソード(1,2,4)
            return Sword.atk_dmg, Sword.atk_dir
        elif SwordBeam.hit(x, y, w, h):  # ビーム(1,2,4)
            return SwordBeam.atk_dmg, SwordBeam.atk_dir
        elif incbomb and Bomb.hit(x, y, w, h):  # 爆弾(4)
            return 4, Bomb.atk_dir
        elif Arrow.hit(x, y, w, h):  # 矢(2)/銀の矢(4)
            return Arrow.atk_dmg, Arrow.atk_dir
        elif Rod.hit(x, y, w, h):  # ロッドビーム(2)
            return Rod.atk_dmg, Rod.atk_dir
        elif Candle.hit(x, y, w, h):  # ロウソク(1)
            return Candle.atk_dmg, Candle.atk_dir
        return 0, NO_DIR

    def stun(self, x, y, w, h):
        if Boomerang.hit(x, y, w, h):  # ブーメラン(0)
            return Boomerang.atk_dir
        return NO_DIR

class BaseEnemy(BaseMove, EnemyDamage):
    def __init__(self, x, y, hp=1, prj=200, hispd=1, atk_pt=1):
        self.x, self.y = x, y
        self.hp = hp
        self.prj = prj
        self.hispd = hispd
        self.atk_pt = atk_pt
        self.dirc = pyxel.rndi(UP,RIGHT)  # UP～RIGHT
        self.walk_cnt = 0
        self.smoke_cnt = 32
        self.moving = 0
        self.shooting = 0
        self.damaged_cnt = 0
        self.speed = 1
        self.stun_cnt = 0

    def getxyname(self):
        return self.x//16, self.y//16, self.name

    def update(self, food_x=-1, food_y=-1):
        self.walk_cnt += 1
        if self.smoke_cnt:
            self.smoke_cnt -= 1
            return RET_NONE, self.dirc
        if self.damaged_cnt:
            if self.damaged_cnt>8 and self.hp>0:
                _, self.x, self.y = self.canmove(self.x, self.y, self.dmg_dir, dst=4, rng=1)
            self.damaged_cnt -= 1
            if self.damaged_cnt==0 and self.hp<=0:
                return RET_KILLED, self.dirc
            return RET_NONE, self.dirc
        dmg_point, self.dmg_dir = self.damage(self.x, self.y, 16, 16)
        if dmg_point:
            self.damaged_cnt = 16
            self.hp -= dmg_point
            return RET_NONE, self.dirc
        else:
            self.dmg_dir = self.stun(self.x, self.y, 16, 16)
            if not self.dmg_dir==NO_DIR:
                self.damaged_cnt = 16
                if self.stun_cnt==0:
                    self.stun_cnt = 64
                return RET_NONE, self.dirc
        if self.stun_cnt:
            self.stun_cnt -= 1
            return RET_NONE, self.dirc
        if self.shooting:
            self.shooting -= 1
            if self.shooting==0:
                return RET_SHOOT, self.dirc
        elif self.moving==0:
            if pyxel.rndi(1,10)<=self.hispd:  # 1/10で倍速
                self.speed = 2
                self.moving = pyxel.rndi(8,18)*2
            else:
                self.speed = 1
                self.moving = pyxel.rndi(4,12)*4
            if food_x>=0:
                if pyxel.rndi(1,2)==1:
                    self.dirc = RIGHT if food_x>self.x else LEFT
                else:
                    self.dirc = DOWN if food_y>self.y else UP
            else:
                self.dirc = pyxel.rndi(UP,RIGHT)  # UP～RIGHT
        else:
            self.moving -= 1
            ret, self.x, self.y = self.canmove(self.x, self.y, self.dirc, dst=self.speed, rng=1)
            if not ret:
                self.moving = 0
        if pyxel.rndi(1,self.prj)==1:  # 1/200で飛び道具
            self.shooting = 16
        if Player.hit(self.x, self.y, 16, 16):
            return RET_ATTACK, self.dirc
        return RET_NONE, self.dirc

    def draw(self):
        if self.smoke_cnt:
            Draw.smoke(self.x, self.y, self.smoke_cnt)
        elif self.damaged_cnt and self.hp<=0:
            Draw.flash(self.x, self.y+ENEMY_Y_ALIGN, self.damaged_cnt)
        elif self.damaged_cnt%2:
            pass
        else:
            self.draw_enemy(self.x, self.y+ENEMY_Y_ALIGN, self.dirc, 0 if self.stun_cnt else self.walk_cnt//4%2)

class Octorok(BaseEnemy):
    name = OCTOROK
    def draw_enemy(self, x, y, dirc, ptn):  # ptn=0,1
        Draw.octorok(x, y, dirc, ptn)

class BlueOctorok(BaseEnemy):
    name = BLUEOCTOROK
    def draw_enemy(self, x, y, dirc, ptn):  # ptn=0,1
        Draw.blueoctorok(x, y, dirc, ptn)

class Moblin(BaseEnemy):
    name = MOBLIN
    def draw_enemy(self, x, y, dirc, ptn):  # ptn=0,1
        Draw.moblin(x, y, dirc, ptn)

class BlueMoblin(BaseEnemy):
    name = BLUEMOBLIN
    def draw_enemy(self, x, y, dirc, ptn):  # ptn=0,1
        Draw.bluemoblin(x, y, dirc, ptn)

class Lynel(BaseEnemy):
    name = LYNEL
    def draw_enemy(self, x, y, dirc, ptn):  # ptn=0,1
        Draw.lynel(x, y, dirc, ptn)

class BlueLynel(BaseEnemy):
    name = BLUELYNEL
    def draw_enemy(self, x, y, dirc, ptn):  # ptn=0,1
        Draw.bluelynel(x, y, dirc, ptn)

class BaseProjectile(BaseMove):
    def __init__(self, x, y, dirc, atk_pt=1):
        self.setxy(x, y, dirc)
        self.atk_pt = atk_pt
        self.dirc = dirc
        self.blocked = 0

    def update(self, player_dirc):
        if self.blocked:
            if self.dirc in (UP, RIGHT):
                self.x -= 2
                self.y += 2
            elif self.dirc in (DOWN, LEFT):
                self.x += 2
                self.y -= 2
            self.blocked -= 1
            if self.blocked==0:
                return RET_KILLED, self.dirc
        else:
            ret, self.x, self.y = self.canshoot2(self.x, self.y, self.dirc)
            if not ret:
                return RET_KILLED, self.dirc
            elif self.hit():
                if self.name in (OCTOROKROCK, MOBLINARROW) and not Player.atk_posture_cnt and self.dirc==REV_DIR[player_dirc]:
                    self.blocked = 6
                else:
                    return RET_ATTACK, self.dirc
        return RET_NONE, self.dirc

    def draw(self):
        self.draw_projectile(self.x, self.y+ENEMY_Y_ALIGN, self.dirc)

class OctorokRock(BaseProjectile):  # 8x10
    name = OCTOROKROCK
    def setxy(self, x, y, dirc):
        self.x, self.y = x+4, y+3

    def canshoot2(self, x, y, dirc):
        return self.canshoot(x, y, 8, 10, dirc, 4, 1)

    def hit(self):
        return Player.dmg_x-8<self.x<Player.dmg_x+Player.dmg_w and Player.dmg_y-10<self.y<Player.dmg_y+Player.dmg_h

    def draw_projectile(self, x, y, dirc):
        Draw.octorokrock(x, y)

class MoblinArrow(BaseProjectile):  # 5x16
    name = MOBLINARROW
    def setxy(self, x, y, dirc):
        if dirc in (UP, DOWN):
            self.x, self.y = x+2, y
        elif dirc in (LEFT, RIGHT):
            self.x, self.y = x, y+8
    
    def canshoot2(self, x, y, dirc):
        if dirc in (UP, DOWN):
            return self.canshoot(x, y, 5, 16, dirc, 4, 1)
        elif dirc in (LEFT, RIGHT):
            return self.canshoot(x, y, 16, 5, dirc, 4, 1)
        return False, x, y

    def hit(self):
        return (self.dirc in (UP, DOWN) and Player.dmg_x-5<self.x<Player.dmg_x+Player.dmg_w and Player.dmg_y-16<self.y<Player.dmg_y+Player.dmg_h) or \
                (self.dirc in (LEFT, RIGHT) and Player.dmg_x-16<self.x<Player.dmg_x+Player.dmg_w and Player.dmg_y-5<self.y<Player.dmg_y+Player.dmg_h)

    def draw_projectile(self, x, y, dirc):
        Draw.moblinarrow(x, y, dirc)

class LynelSword(BaseProjectile):  # 7x16
    name = LYNELSWORD
    def setxy(self, x, y, dirc):
        if dirc in (UP, DOWN):
            self.x, self.y = x+5, y
        elif dirc in (LEFT, RIGHT):
            self.x, self.y = x, y+8
    
    def canshoot2(self, x, y, dirc):
        if dirc in (UP, DOWN):
            return self.canshoot(x, y, 7, 16, dirc, 5, 1)
        elif dirc in (LEFT, RIGHT):
            return self.canshoot(x, y, 16, 7, dirc, 5, 1)
        return False, x, y

    def hit(self):
        return (self.dirc in (UP, DOWN) and Player.dmg_x-5<self.x<Player.dmg_x+Player.dmg_w and Player.dmg_y-16<self.y<Player.dmg_y+Player.dmg_h) or \
                (self.dirc in (LEFT, RIGHT) and Player.dmg_x-16<self.x<Player.dmg_x+Player.dmg_w and Player.dmg_y-5<self.y<Player.dmg_y+Player.dmg_h)

    def draw_projectile(self, x, y, dirc):
        Draw.lynelsword(x, y, dirc, pyxel.frame_count%4)

class Tektite(BaseMove, EnemyDamage):
    name = TEKTITE
    def __init__(self, x, y, blue=False):
        if blue==False:
            self.name = TEKTITE
        else:
            self.name = BLUETEKTITE
        self.x, self.y = x, y
        self.sx, self.sy, self.ex, self.ey = 0, 0, 0, 0
        self.hp = 1
        self.atk_pt = 1
        self.walk_cnt = 0
        self.ptn = 0
        self.smoke_cnt = 32
        self.damaged_cnt = 0
        self.stun_cnt = 0
        self.jump_intv = pyxel.rndi(1,20)
        self.jump_cnt = 0

    def getxyname(self):
        return self.x//16, self.y//16, self.name

    def update(self, food_x=-1, food_y=-1):
        self.walk_cnt += 1
        if self.walk_cnt%4==0 and pyxel.rndi(1,4)==1:
            self.ptn = 1-self.ptn
        if self.smoke_cnt:
            self.smoke_cnt -= 1
            return RET_NONE, NO_DIR
        if self.damaged_cnt:
            if self.damaged_cnt>8 and self.hp>0:
                _, self.x, self.y = self.canmove(self.x, self.y, self.dmg_dir, dst=4, rng=1)
            self.damaged_cnt -= 1
            if self.damaged_cnt==0 and self.hp<=0:
                return RET_KILLED, NO_DIR
            return RET_NONE, NO_DIR
        dmg_point, self.dmg_dir = self.damage(self.x, self.y, 16, 16)
        if dmg_point:
            self.damaged_cnt = 16
            self.hp -= dmg_point
            return RET_NONE, NO_DIR
        else:
            self.dmg_dir = self.stun(self.x, self.y, 16, 16)
            if not self.dmg_dir==NO_DIR:
                self.damaged_cnt = 16
                if self.stun_cnt==0:
                    self.stun_cnt = 64
                return RET_NONE, NO_DIR
        if self.stun_cnt:
            self.stun_cnt -= 1
            return RET_NONE, NO_DIR
        if self.jump_intv:
            self.jump_intv -= 1
            if self.jump_intv==0:
                self.sx, self.sy = self.x, self.y
                dx, dy = pyxel.rndi(-8 if self.name==TEKTITE else -12, 8 if self.name==TEKTITE else 12)*8, pyxel.rndi(-6, 6)*8
                if 16<=self.sx+dx<=(MAP_SIZE_X-2)*16:
                    self.ex = self.sx+dx
                else:
                    self.ex = self.sx-dx
                if 16<=self.sy+dy<=(MAP_SIZE_Y-2)*16:
                    self.ey = self.sy+dy
                else:
                    self.ey = self.sy-dy
                self.jump_cnt = 16
        else:  # ジャンプ中
            self.jump_cnt -= 1
            self.x = self.ex-(self.ex-self.sx)*self.jump_cnt//16
            self.y = self.ey-(self.ey-self.sy)*self.jump_cnt//16-(64-(self.jump_cnt-8)**2)//2
            if self.jump_cnt==0:
                self.jump_intv = pyxel.rndi(10 if self.name==TEKTITE else 80, 80 if self.name==TEKTITE else 160)
        if Player.dmg_x-16<self.x<Player.dmg_x+Player.dmg_w and Player.dmg_y-16<self.y<Player.dmg_y+Player.dmg_h:
            return RET_ATTACK, UP if self.jump_cnt else DOWN
        return RET_NONE, NO_DIR

    def draw(self):
        if self.smoke_cnt:
            Draw.smoke(self.x, self.y, self.smoke_cnt)
        elif self.damaged_cnt and self.hp<=0:
            Draw.flash(self.x, self.y+ENEMY_Y_ALIGN, self.damaged_cnt)
        elif self.damaged_cnt%2:
            pass
        else:
            if self.name==TEKTITE:
                Draw.tektite(self.x, self.y+ENEMY_Y_ALIGN, self.ptn)
            else:
                Draw.bluetektite(self.x, self.y+ENEMY_Y_ALIGN, self.ptn)

class Dodongo(BaseMove, EnemyDamage):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dirc = DOWN
        self.walk_cnt = 0
        self.moving = 0
        self.damaged_cnt = 0
        self.stun_cnt = 0
        self.eat_cnt = 0
        self.eaten = 0

    def update(self, player_x, player_y):
        self.walk_cnt += 1
        if self.damaged_cnt:
            self.damaged_cnt -= 1
            if self.damaged_cnt==0:
                return RET_KILLED, NO_DIR
            return RET_NONE, NO_DIR
        if self.stun_cnt:
            self.stun_cnt -= 1
            dmg_point, _ = self.damage(self.x, self.y, 16, 16, incbomb=False)
            if dmg_point:
                self.damaged_cnt = 16
            return RET_NONE, self.dirc
        if self.eat_cnt:
            self.eat_cnt -= 1
            if  self.eat_cnt==0 and self.eaten==2:
                self.damaged_cnt = 16
            return RET_NONE, self.dirc
        if self.moving==0:
            self.moving = pyxel.rndi(4,12)*4
            self.dirc = pyxel.rndi(UP,RIGHT)  # UP～RIGHT
        else:
            self.moving -= 1
            ret, self.x, self.y = self.movefree(self.x, self.y, 16, 16, self.dirc, dst=1, rng=2)
            if not ret:
                self.moving = 0
        # 爆弾を食べる
        if Bomb.bombhit(self.x+4, self.y+4, 8, 8):  # 爆弾
            self.eat_cnt = 32
            self.eaten += 1
            return RET_DELBOMB, NO_DIR
        # 煙で停止
        if Bomb.hit(self.x, self.y, 16, 16):  # 爆風(4)
            self.stun_cnt = 96

        if Player.hit(self.x, self.y, 16, 16):
            return RET_ATTACK, self.dirc

        return RET_NONE, NO_DIR

    def draw(self):
        if self.damaged_cnt:
            Draw.flash(self.x, self.y+ENEMY_Y_ALIGN, self.damaged_cnt)
        else:
            Draw.dodongo(self.x, self.y+ENEMY_Y_ALIGN, self.dirc, 2 if self.eat_cnt else self.stun_cnt//16%2 if self.stun_cnt else self.walk_cnt//4%2)

TESTITART_MOVESTEP = 30
class Testitart(BaseMove, EnemyDamage):
    def __init__(self, x, y, hp):
        self.x, self.y, self.sx, self.sy, self.ex, self.ey = x, y, x, y, x, y
        self.leftclaw_hp, self.rightclaw_hp, self.upclaw_hp, self.downclaw_hp = hp, hp, hp, hp
        self.leftclaw_dmgcnt, self.rightclaw_dmgcnt, self.upclaw_dmgcnt, self.downclaw_dmgcnt = 0, 0, 0, 0
        self.walk_cnt = 0
        self.damaged_cnt = 0
        self.move_cnt = 0
        self.beam = []
        self.beam_intv = pyxel.rndi(20,80)

    def update(self, player_x, player_y):
        self.walk_cnt += 1
        if self.beam_intv:
            self.beam_intv -= 1
            if self.beam_intv==1:
                self.beam_intv = pyxel.rndi(40,160)
                self.beam.append(Beam(self.x+4, self.y+3, player_x, player_y))  # 8x10
        for i in reversed(range(len(self.beam))):  # ビーム
            ret, dirc = self.beam[i].update() 
            if ret==RET_SCREENOUT:
                del self.beam[i]
            elif ret==RET_ATTACK:
                return RET_ATTACK, dirc
        if self.damaged_cnt:
            self.damaged_cnt -= 1
            if self.damaged_cnt==0:
                return RET_KILLED, NO_DIR
            return RET_NONE, NO_DIR
        if self.leftclaw_dmgcnt:
            self.leftclaw_dmgcnt -= 1
        if self.rightclaw_dmgcnt:
            self.rightclaw_dmgcnt -= 1
        if self.upclaw_dmgcnt:
            self.upclaw_dmgcnt -= 1
        if self.downclaw_dmgcnt:
            self.downclaw_dmgcnt -= 1
        if self.leftclaw_dmgcnt or self.rightclaw_dmgcnt or self.upclaw_dmgcnt or self.downclaw_dmgcnt:
            if self.leftclaw_hp<=0 and self.rightclaw_hp<=0 and self.upclaw_hp<=0 and self.downclaw_hp<=0:
                self.damaged_cnt = 16
                return RET_NONE, NO_DIR
        if self.leftclaw_hp and self.leftclaw_dmgcnt==0:
            dmg_point, _ = self.damage(self.x-16, self.y, 16, 16)
            if dmg_point:
                self.leftclaw_dmgcnt = 16
                self.leftclaw_hp -= dmg_point
                if self.leftclaw_hp<0:
                    self.leftclaw_hp = 0
        if self.rightclaw_hp and self.rightclaw_dmgcnt==0:
            dmg_point, _ = self.damage(self.x+16, self.y, 16, 16)
            if dmg_point:
                self.rightclaw_dmgcnt = 16
                self.rightclaw_hp -= dmg_point
                if self.rightclaw_hp<0:
                    self.rightclaw_hp = 0
        if self.upclaw_hp and self.upclaw_dmgcnt==0:
            dmg_point, _ = self.damage(self.x, self.y-16, 16, 16)
            if dmg_point:
                self.upclaw_dmgcnt = 16
                self.upclaw_hp -= dmg_point
                if self.upclaw_hp<0:
                    self.upclaw_hp = 0
        if self.downclaw_hp and self.downclaw_dmgcnt==0:
            dmg_point, _ = self.damage(self.x, self.y+16, 16, 16)
            if dmg_point:
                self.downclaw_dmgcnt = 16
                self.downclaw_hp -= dmg_point
                if self.downclaw_hp<0:
                    self.downclaw_hp = 0
        if self.move_cnt==0:
            deadclaw = len([i for i in [self.leftclaw_hp, self.rightclaw_hp, self.upclaw_hp, self.downclaw_hp] if i==0])
            self.sx, self.sy = self.ex, self.ey
            dx, dy = pyxel.rndi(-4-deadclaw*2, 4+deadclaw*2)*8, pyxel.rndi(-3-deadclaw, 3+deadclaw)*8
            if 16*2<=self.sx+dx<=(MAP_SIZE_X-3)*16:
                self.ex = self.sx+dx
            else:
                self.ex = self.sx-dx
            if 16*2<=self.sy+dy<=(MAP_SIZE_Y-3)*16:
                self.ey = self.sy+dy
            else:
                self.ey = self.sy-dy
        else:
            self.x = self.sx+(self.ex-self.sx)*self.move_cnt//TESTITART_MOVESTEP
            self.y = self.sy+(self.ey-self.sy)*self.move_cnt//TESTITART_MOVESTEP
        self.move_cnt += 1
        if self.move_cnt>=TESTITART_MOVESTEP:
            self.move_cnt = 0
        if Player.hit(self.x, self.y, 16, 16):
            return RET_ATTACK, DOWN
        elif self.leftclaw_hp and Player.hit(self.x-16, self.y, 16, 16):
            return RET_ATTACK, LEFT
        elif self.rightclaw_hp and Player.hit(self.x+16, self.y, 16, 16):
            return RET_ATTACK, RIGHT
        elif self.upclaw_hp and Player.hit(self.x, self.y-16, 16, 16):
            return RET_ATTACK, UP
        elif self.downclaw_hp and Player.hit(self.x, self.y+16, 16, 16):
            return RET_ATTACK, DOWN
        return RET_NONE, NO_DIR

    def draw(self):
        if self.damaged_cnt:
            Draw.flash(self.x, self.y+ENEMY_Y_ALIGN, self.damaged_cnt)
        else:
            Draw.testitart_body(self.x, self.y+ENEMY_Y_ALIGN)
            if (self.leftclaw_hp and self.leftclaw_dmgcnt//2%2==0) or (self.leftclaw_hp==0 and self.leftclaw_dmgcnt//2%2==1):
                Draw.testitart_leftclaw(self.x-16, self.y+ENEMY_Y_ALIGN, self.walk_cnt//(self.leftclaw_hp+2)%2)
            if (self.rightclaw_hp and self.rightclaw_dmgcnt//2%2==0) or (self.rightclaw_hp==0 and self.rightclaw_dmgcnt//2%2==1):
                Draw.testitart_rightclaw(self.x+16, self.y+ENEMY_Y_ALIGN, self.walk_cnt//(self.rightclaw_hp+2)%2)
            if (self.upclaw_hp and self.upclaw_dmgcnt//2%2==0) or (self.upclaw_hp==0 and self.upclaw_dmgcnt//2%2==1):
                Draw.testitart_upclaw(self.x, self.y+ENEMY_Y_ALIGN-16, self.walk_cnt//(self.upclaw_hp+2)%2)
            if (self.downclaw_hp and self.downclaw_dmgcnt//2%2==0) or (self.downclaw_hp==0 and self.downclaw_dmgcnt//2%2==1):
                Draw.testitart_downclaw(self.x, self.y+ENEMY_Y_ALIGN+16, self.walk_cnt//(self.downclaw_hp+2)%2)
        for i in reversed(range(len(self.beam))):
            self.beam[i].draw()

DIGDOGGER_MOVESTEP = 40
class Digdogger(BaseMove, EnemyDamage):
    def __init__(self, x, y, hp):
        self.x, self.y, self.sx, self.sy, self.ex, self.ey = x, y, x, y, x, y
        self.hp = hp
        self.walk_cnt = 0
        self.damaged_cnt = 0
        self.stun_cnt = 0
        self.move_cnt = 0

    def update(self, player_x, player_y, small):
        self.walk_cnt += 1
        if small:
            if self.damaged_cnt:
                self.damaged_cnt -= 1
                if self.damaged_cnt==0 and self.hp==0:
                    return RET_KILLED, NO_DIR
                return RET_NONE, NO_DIR
            dmg_point, _ = self.damage(self.x, self.y, 16, 16)
            if dmg_point:
                self.damaged_cnt = 16
                self.hp -= dmg_point
                if self.hp<0:
                    self.hp = 0
                return RET_NONE, NO_DIR
            else:
                if not self.stun(self.x, self.y, 16, 16)==NO_DIR:
                    self.damaged_cnt = 16
                    if self.stun_cnt==0:
                        self.stun_cnt = 64
                    return RET_NONE, NO_DIR
            if self.stun_cnt:
                self.stun_cnt -= 1
                return RET_NONE, NO_DIR
        if self.move_cnt==0:
            self.sx, self.sy = self.ex, self.ey
            self.ex, self.ey = pyxel.rndi(2*16, (MAP_SIZE_X-2)*16-16), pyxel.rndi(2*16, (MAP_SIZE_Y-2)*16-16)
        else:
            self.x = self.sx+(self.ex-self.sx)*self.move_cnt//DIGDOGGER_MOVESTEP
            self.y = self.sy+(self.ey-self.sy)*self.move_cnt//DIGDOGGER_MOVESTEP
        self.move_cnt += 1
        if self.move_cnt>=DIGDOGGER_MOVESTEP:
            self.move_cnt = 0
        if small:
            if Player.hit(self.x, self.y+4, 8, 8):
                return RET_ATTACK, LEFT
            elif Player.hit(self.x+8, self.y+4, 8, 8):
                return RET_ATTACK, RIGHT
            elif Player.hit(self.x, self.y, 16, 4):
                return RET_ATTACK, UP
            elif Player.hit(self.x, self.y+12, 16, 4):
                return RET_ATTACK, DOWN
        else:
            if Player.hit(self.x-7, self.y, 14, 16):
                return RET_ATTACK, LEFT
            elif Player.hit(self.x+7, self.y, 14, 16):
                return RET_ATTACK, RIGHT
            elif Player.hit(self.x-7, self.y-8, 28, 8):
                return RET_ATTACK, UP
            elif Player.hit(self.x-7, self.y+16, 28, 8):
                return RET_ATTACK, DOWN
        return RET_NONE, NO_DIR

    def draw(self, ptn=1):
        if self.damaged_cnt and self.hp==0:
            Draw.flash(self.x, self.y+ENEMY_Y_ALIGN, self.damaged_cnt)
        elif self.damaged_cnt//2%2:
            pass
        else:
            if ptn==0:
                Draw.digdogger(self.x, self.y+ENEMY_Y_ALIGN, small=False, ptn=self.walk_cnt//8%5)
            elif ptn==1:
                Draw.digdogger(self.x, self.y+ENEMY_Y_ALIGN, small=True, ptn=self.walk_cnt//4%2)

GOHMA_MOVEDST = 32
class Gohma(BaseMove, EnemyDamage):
    def __init__(self, x, y, hp):
        self.x, self.y = (x+8)//16*16, (y+8)//16*16
        self.init_y = self.y
        self.hp = hp
        self.walk_cnt = 0
        self.damaged_cnt = 0
        self.move_cnt = 0
        self.dx, self.dy = 0, 0
        self.eye_intv = pyxel.rndi(200,300)
        self.beam = []
        self.beam_intv = pyxel.rndi(50,100)

    def update(self, player_x, player_y):
        self.walk_cnt += 1
        if self.beam_intv:
            self.beam_intv -= 1
            if self.beam_intv==1:
                self.beam_intv = pyxel.rndi(60,240)
                self.beam.append(Beam(self.x+4, self.y+3, player_x, player_y))
        for i in reversed(range(len(self.beam))):
            ret, dirc = self.beam[i].update() 
            if ret==RET_SCREENOUT:
                del self.beam[i]
            elif ret==RET_ATTACK:
                return RET_ATTACK, dirc
        if self.damaged_cnt:
            self.damaged_cnt -= 1
            if self.damaged_cnt==0 and self.hp==0:
                return RET_KILLED, NO_DIR
            return RET_NONE, NO_DIR
        if self.eye_intv:
            self.eye_intv -= 1
            if self.eye_intv==0:
                self.eye_intv = pyxel.rndi(100,250)
        if 20<self.eye_intv<=60 and Arrow.hit(self.x, self.y, 16, 16):
            self.damaged_cnt = 16
            self.hp -= Arrow.atk_dmg
            if self.hp<0:
                self.hp = 0
            return RET_NONE, NO_DIR
        elif Arrow.hit(self.x-16, self.y, 48, 16):  # 当たってもダメージなし
            pass
        if self.move_cnt==0:
            self.x, self.y = (self.x+8)//16*16, (self.y+8)//16*16
            if self.y==self.init_y+GOHMA_MOVEDST:
                self.dx, self.dy = 0, -1
            elif pyxel.rndi(1,3)==1:
                self.dx, self.dy = 0, 1
            elif pyxel.rndi(1,2)==1 and self.x>16*3:
                self.dx, self.dy = -1, 0
            elif self.x<(MAP_SIZE_X-3)*16-16:
                self.dx, self.dy = 1, 0
            else:
                self.dx, self.dy = -1, 0
        else:
            self.x += self.dx
            self.y += self.dy
        self.move_cnt += 1
        if self.move_cnt>GOHMA_MOVEDST:
            self.move_cnt = 0
        if Player.hit(self.x-16, self.y, 48, 8):
            return RET_ATTACK, UP
        elif Player.hit(self.x-16, self.y+8, 48, 8):
            return RET_ATTACK, DOWN
        return RET_NONE, NO_DIR

    def draw(self):
        if self.damaged_cnt and self.hp==0:
            Draw.flash(self.x, self.y+ENEMY_Y_ALIGN, self.damaged_cnt)
        elif self.damaged_cnt//2%2:
            pass
        else:
            Draw.gohma(self.x, self.y+ENEMY_Y_ALIGN, ptn=self.walk_cnt//8%2, eye=self.eye_intv)
        for i in reversed(range(len(self.beam))):
            self.beam[i].draw()

class Object(EnemyDamage):  # 16x16, O_FLAME, O_OLDMAN1, O_OLDMAN2, O_OLDWOMAN
    def __init__(self, x, y, hp, obj):
        self.x, self.y, self.hp, self.obj = x, y, hp, obj
        self.cnt = 0
        self.damaged_cnt = 0
        self.stun_cnt = 0
        self.beam = []
        self.beam_intv = 0

    def beamon(self):
        if self.beam_intv==0:
            self.beam_intv = 30

    def update(self, player_x, player_y):
        self.cnt += 1
        if self.beam_intv:
            self.beam_intv -= 1
            if self.beam_intv==1:
                self.beam_intv = pyxel.rndi(60,120)
                self.beam.append(Beam(self.x+4, self.y+3, player_x, player_y))
        for i in reversed(range(len(self.beam))):
            ret, dirc = self.beam[i].update() 
            if ret==RET_SCREENOUT:
                del self.beam[i]
            elif ret==RET_ATTACK:
                return RET_ATTACK, dirc
        if self.damaged_cnt:
            self.damaged_cnt -= 1
            if self.damaged_cnt==0 and self.hp==0:
                return RET_KILLED, NO_DIR
            return RET_DAMAGED, NO_DIR
        dmg_point, _ = self.damage(self.x, self.y, 16, 16)
        if dmg_point:
            self.damaged_cnt = 16
            self.hp -= dmg_point
            if self.hp<0:
                self.hp = 0
            return RET_NONE, NO_DIR
        else:
            if not self.stun(self.x, self.y, 16, 16)==NO_DIR:
                self.damaged_cnt = 16
                if self.stun_cnt==0:
                    self.stun_cnt = 64
                return RET_DAMAGED, NO_DIR
        if self.stun_cnt:
            self.stun_cnt -= 1
            return RET_NONE, NO_DIR
        if self.obj==O_FLAME:
            if Player.hit(self.x, self.y+4, 8, 8):
                return RET_ATTACK, LEFT
            elif Player.hit(self.x+8, self.y+4, 8, 8):
                return RET_ATTACK, RIGHT
            elif Player.hit(self.x, self.y, 16, 4):
                return RET_ATTACK, UP
            elif Player.hit(self.x, self.y+12, 16, 4):
                return RET_ATTACK, DOWN
        return RET_NONE, NO_DIR

    def draw(self):
        if self.damaged_cnt and self.hp==0:
            Draw.flash(self.x, self.y+ENEMY_Y_ALIGN, self.damaged_cnt)
        elif self.damaged_cnt//2%2:
            pass
        else:
            if self.obj==O_FLAME:
                Draw.flame(self.x, self.y, self.cnt//4%2)
            elif self.obj==O_OLDMAN1:
                Draw.oldman1(self.x, self.y)
            elif self.obj==O_OLDMAN2:
                Draw.oldman2(self.x, self.y)
            elif self.obj==O_OLDWOMAN:
                Draw.oldwoman(self.x, self.y)
            elif self.obj==O_MOBLIN:
                Draw.moblin(self.x, self.y)
            elif self.obj==O_MERCHANT:
                Draw.merchant(self.x, self.y)
        for i in reversed(range(len(self.beam))):
            self.beam[i].draw()

class Gleeok(EnemyDamage):  # 24x32
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walk_cnt = 0
        self.gleeokhead1 = []
        self.gleeokhead2 = []
        self.beam = []
        for _ in range(3):
            self.gleeokhead1.append(GleeokHead1(x+8, y+24))
        self.damaged_cnt = 0

    def update(self, player_x, player_y):
        if self.damaged_cnt:
            self.damaged_cnt -= 1
            if self.damaged_cnt==0:
                return RET_KILLED, NO_DIR
            return RET_NONE, NO_DIR
        if pyxel.rndi(1,4)==1:
            self.walk_cnt += 1
        for i in reversed(range(len(self.gleeokhead1))):  # グリオーク（頭・ビーム）
            ret = self.gleeokhead1[i].update(player_x, player_y) 
            if ret==RET_KILLED:
                self.gleeokhead2.append(GleeokHead2(self.gleeokhead1[i].head_x-4, self.gleeokhead1[i].head_y))
                del self.gleeokhead1[i]
            elif ret==RET_BEAM:
                self.beam.append(Beam(self.gleeokhead1[i].head_x, self.gleeokhead1[i].head_y+6, player_x, player_y))
            elif ret==RET_ATTACK:
                return RET_ATTACK, DOWN
        for i in reversed(range(len(self.gleeokhead2))):  # グリオーク2（頭・ビーム）
            ret = self.gleeokhead2[i].update(player_x, player_y) 
            if ret==RET_BEAM:
                self.beam.append(Beam(self.gleeokhead2[i].head_x, self.gleeokhead2[i].head_y+6, player_x, player_y))
            elif ret==RET_ATTACK:
                return RET_ATTACK, DOWN
        for i in reversed(range(len(self.beam))):  # ビーム
            ret, dirc = self.beam[i].update() 
            if ret==RET_SCREENOUT:
                del self.beam[i]
            elif ret==RET_ATTACK:
                return RET_ATTACK, dirc
        _, _ = self.damage(self.x, self.y, 24, 32)  # 武器が当たったら消滅
        if Player.hit(self.x, self.y, 24, 32):  # グリオーク（体）
            return RET_ATTACK, DOWN
        elif not self.gleeokhead1:
            self.damaged_cnt = 64
        return RET_NONE, NO_DIR

    def draw(self):
        if self.damaged_cnt:
            for i in (-1,0,1):
                for j in (0,1):
                    Draw.flash(self.x+4+16*i, self.y+8+16*j, self.damaged_cnt//4)
            Draw.flash(self.x+4, self.y+8-16, self.damaged_cnt//4)
        else:
            Draw.gleeokbody(self.x, self.y, self.walk_cnt//4%4)
        for i in reversed(range(len(self.gleeokhead1))):
            self.gleeokhead1[i].draw()
        for i in reversed(range(len(self.gleeokhead2))):
            self.gleeokhead2[i].draw()
        for i in reversed(range(len(self.beam))):
            self.beam[i].draw()

GLEEOKHEAD1_MOVESTEP = 30
class GleeokHead1(EnemyDamage):  # 8x16
    def __init__(self, x, y):
        self.bx, self.by = x, y
        self.head_x, self.head_y = x, y+28
        self.sx, self.sy, self.ex, self.ey = x, y+28, x, y+28
        self.neck1_x, self.neck1_y = x, y+7
        self.neck2_x, self.neck2_y = x, y+14
        self.hp = 5
        self.move_cnt = 0
        self.damaged_cnt = 0
        self.beam_intv = pyxel.rndi(20,80)

    def update(self, player_x, player_y):
        if self.damaged_cnt:
            self.damaged_cnt -= 1
            if self.damaged_cnt==0 and self.hp<=0:
                return RET_KILLED
            return RET_NONE
        if self.move_cnt==0:
            self.sx, self.sy = self.ex, self.ey
            self.ex, self.ey = pyxel.rndi(self.bx-28, self.bx+28), pyxel.rndi(self.by+4, self.by+4+28)
        else:
            self.head_x = self.sx+(self.ex-self.sx)*self.move_cnt//GLEEOKHEAD1_MOVESTEP
            self.head_y = self.sy+(self.ey-self.sy)*self.move_cnt//GLEEOKHEAD1_MOVESTEP
            self.neck1_x = self.bx+(self.head_x-self.bx)//3
            self.neck1_y = self.by+(self.head_y-self.by)//3
            self.neck2_x = self.bx+(self.head_x-self.bx)*2//3
            self.neck2_y = self.by+(self.head_y-self.by)*2//3
        self.move_cnt += 1
        if self.move_cnt>=GLEEOKHEAD1_MOVESTEP:
            self.move_cnt = 0
        dmg_point, _ = self.damage(self.head_x, self.head_y, 8, 16)
        if dmg_point>=4:
            self.damaged_cnt = 16
            self.hp -= 1
        elif Player.hit(self.head_x, self.head_y, 8, 16):
            return RET_ATTACK
        if self.beam_intv:
            self.beam_intv -= 1
            if self.beam_intv==1:
                self.beam_intv = pyxel.rndi(100,200)
                return RET_BEAM
        return RET_NONE

    def draw(self):
        Draw.gleeokneck(self.neck1_x, self.neck1_y)  # 首1
        Draw.gleeokneck(self.neck2_x, self.neck2_y)  # 首2
        if self.damaged_cnt:
            if self.hp==0:
                Draw.smoke(self.head_x-4, self.head_y, self.damaged_cnt)
            else:
                Draw.gleeokhead1(self.head_x, self.head_y, self.damaged_cnt%2)
        else:
            Draw.gleeokhead1(self.head_x, self.head_y)

GLEEOKHEAD2_MOVESTEP = 30
class GleeokHead2(EnemyDamage):  # 16x16
    def __init__(self, x, y):
        self.head_x, self.head_y, self.sx, self.sy, self.ex, self.ey = x, y, x, y, x, y
        self.move_cnt = 0
        self.beam_intv = pyxel.rndi(20,80)

    def update(self, player_x, player_y):
        if self.move_cnt==0:
            self.sx, self.sy = self.ex, self.ey
            self.ex, self.ey = pyxel.rndi(3*16, (MAP_SIZE_X-3)*16-16), pyxel.rndi(3*16, (MAP_SIZE_Y-3)*16-16)
        else:
            self.head_x = self.sx+(self.ex-self.sx)*self.move_cnt//GLEEOKHEAD2_MOVESTEP
            self.head_y = self.sy+(self.ey-self.sy)*self.move_cnt//GLEEOKHEAD2_MOVESTEP
        self.move_cnt += 1
        if self.move_cnt>=GLEEOKHEAD2_MOVESTEP:
            self.move_cnt = 0
        _, _ = self.damage(self.head_x, self.head_y, 16, 16)  # 武器が当たったら消滅
        if Player.hit(self.head_x, self.head_y, 16, 16):
            return RET_ATTACK
        if self.beam_intv:
            self.beam_intv -= 1
            if self.beam_intv==1:
                self.beam_intv = pyxel.rndi(100,200)
                return RET_BEAM
        return RET_NONE

    def draw(self):
        Draw.gleeokhead2(self.head_x, self.head_y, self.move_cnt//2%2)

class Beam:  # 8x10
    def dir16(self, x, y):
        if x==0:
            if y<0:
                return UP, 0, -3
            else:
                return DOWN, 0, 3
        else:
            a = pyxel.atan2(y, x)
            if a<-170:
                return LEFT, -3, 0
            elif a<-150:
                return LEFT, -3, -1
            elif a<-120:
                return LEFT, -2, -2
            elif a<-100:
                return UP, -1, -3
            elif a<-80:
                return UP, 0, -3
            elif a<-60:
                return UP, 1, -3
            elif a<-30:
                return UP, 2, -2
            elif a<-10:
                return RIGHT, 3, -1
            elif a<10:
                return RIGHT, 3, 0
            elif a<30:
                return RIGHT, 3, 1
            elif a<60:
                return RIGHT, 2, 2
            elif a<80:
                return DOWN, 1, 3
            elif a<100:
                return DOWN, 0, 3
            elif a<120:
                return DOWN, -1, 3
            elif a<150:
                return DOWN, -2, 2
            elif a<170:
                return LEFT, -3, 1
            else:
                return LEFT, -3, 0
    
    def __init__(self, x, y, player_x, player_y, rng=0):
        self.x, self.y = x, y
        self.rng = rng
        self.dirc, self.dx, self.dy = self.dir16(player_x-x, player_y-y)
        self.ptn = 0

    def update(self):
        self.ptn += 1
        if self.ptn==4:
            self.ptn = 0
        self.x += self.dx
        self.y += self.dy
        if self.x<=self.rng*16 or self.x>=(MAP_SIZE_X-self.rng)*16-8 or self.y<=16*self.rng or self.y>(MAP_SIZE_Y-self.rng)*16-10:
            return RET_SCREENOUT, NO_DIR
        elif Player.hit(self.x, self.y, 8, 10):
            return RET_ATTACK, self.dirc
        return RET_NONE, NO_DIR

    def draw(self):
        Draw.beam(self.x, self.y, self.ptn)

class Draw:
    @classmethod
    def player(cls, x, y, dirc, ptn=0, swd=0, itm=False, h=16, ctype=0):  # ptn=0,1, ctype=0～2
        if I_RED_RING in Item.item:
            ctype = 2
        elif I_BLUE_RING in Item.item:
            ctype = 1
        if itm:
            pyxel.blt(x, Y_ALIGN+y, 0, 16*8, 16+16*ctype, 16, 16, 1)
        elif dirc==UP:
            if swd:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*7, 16+16*ctype, 16, 16, 1)
            else:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*4, 16+16*ctype, 16 if ptn else -16, h, 1)
        elif dirc==DOWN:
            if swd:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*5, 16+16*ctype, 16, 16, 1)
            else:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*ptn, 16+16*ctype, 16, h, 1)
        elif dirc==LEFT:
            if swd:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*6, 16+16*ctype, -16, 16, 1)
            else:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*2+16*ptn, 16+16*ctype, -16, h, 1)
        elif dirc==RIGHT:
            if swd:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*6, 16+16*ctype, 16, 16, 1)
            else:
                pyxel.blt(x, Y_ALIGN+y, 0, 16*2+16*ptn, 16+16*ctype, 16, h, 1)

    @classmethod
    def sword(cls, x, y, dirc, tp=-1, swd=-1):  # swd=0～
        if tp==-1:
            if W_MASTER_SWORD in Item.item:
                tp = W_MASTER_SWORD
            elif W_MAGICAL_SWORD in Item.item:
                tp = W_MAGICAL_SWORD
            elif W_WHITE_SWORD in Item.item:
                tp = W_WHITE_SWORD
            elif W_SWORD in Item.item:
                tp = W_SWORD
        if tp in (W_SWORD, W_WHITE_SWORD, W_MAGICAL_SWORD, W_MASTER_SWORD):
            if dirc==UP:
                if swd>2:
                    x += 3
                    y -= 12
                elif swd==2:
                    x += 3
                    y -= 11
                elif swd==1:
                    x += 3
                    y -= 3
                if swd:
                    pyxel.blt(x, Y_ALIGN+y, 0, -8+8*tp, 80, 7, 16, 1)
            elif dirc==DOWN:
                if swd>2:
                    x += 5
                    y += 11
                elif swd==2:
                    x += 5
                    y += 7
                elif swd==1:
                    x += 5
                    y += 3
                if swd:
                    pyxel.blt(x, Y_ALIGN+y, 0, -8+8*tp, 80, 7, -16, 1)
            elif dirc==LEFT:
                if swd>2:
                    x -= 11
                    y += 6
                elif swd==2:
                    x -= 7
                    y += 6
                elif swd==1:
                    x -= 3
                    y += 6
                if swd:
                    pyxel.blt(x, Y_ALIGN+y, 0, 48 if tp in (W_MAGICAL_SWORD, W_MASTER_SWORD) else 32, 
                            88 if tp in (W_WHITE_SWORD, W_MASTER_SWORD) else 80, -16, 7, 1)
            elif dirc==RIGHT:
                if swd>2:
                    x += 11
                    y += 6
                elif swd==2:
                    x += 7
                    y += 6
                elif swd==1:
                    x += 3
                    y += 6
                if swd:
                    pyxel.blt(x, Y_ALIGN+y, 0, 48 if tp in (W_MAGICAL_SWORD, W_MASTER_SWORD) else 32, 
                            88 if tp in (W_WHITE_SWORD, W_MASTER_SWORD) else 80, 16, 7, 1)

    @classmethod
    def sword_reflection(cls, x, y, cnt, ptn):  # cnt=5～, ptn=0～3
            pyxel.blt(x-cnt, Y_ALIGN+y-cnt, 0, 64+8*ptn, 80,  8,  9, 1)
            pyxel.blt(x+cnt, Y_ALIGN+y-cnt, 0, 64+8*ptn, 80, -8,  9, 1)
            pyxel.blt(x-cnt, Y_ALIGN+y+cnt, 0, 64+8*ptn, 80,  8, -9, 1)
            pyxel.blt(x+cnt, Y_ALIGN+y+cnt, 0, 64+8*ptn, 80, -8, -9, 1)

    @classmethod
    def boomerang(cls, x, y, cnt, magical=False):  # cnt=0～
        ptn = cnt%8
        v = 88 if magical else 80
        if ptn==0:
            pyxel.blt(x, Y_ALIGN+y, 0, 96, v, 8, 8, 1)
        elif ptn==1:
            pyxel.blt(x, Y_ALIGN+y, 0, 104, v, 8, 8, 1)
        elif ptn==2:
            pyxel.blt(x, Y_ALIGN+y, 0, 112, v, 8, 8, 1)
        elif ptn==3:
            pyxel.blt(x, Y_ALIGN+y, 0, 104, v, -8, 8, 1)
        elif ptn==4:
            pyxel.blt(x, Y_ALIGN+y, 0, 96, v, -8, 8, 1)
        elif ptn==5:
            pyxel.blt(x, Y_ALIGN+y, 0, 104, v, -8, -8, 1)
        elif ptn==6:
            pyxel.blt(x, Y_ALIGN+y, 0, 112, v, 8, -8, 1)
        else:
            pyxel.blt(x, Y_ALIGN+y, 0, 104, v, 8, -8, 1)

    @classmethod
    def bomb(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 0, 40, 64, 8, 16, 1)

    @classmethod
    def arrow(cls, x, y, dirc, silver=False):
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 0, 56 if silver else 48, 64, 5, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 0, 56 if silver else 48, 64, 5, -16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 0, 176, 73 if silver else 68, -16, 5, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 0, 176, 73 if silver else 68, 16, 5, 1)

    @classmethod
    def arrow_reflection(cls, x, y):
            pyxel.blt(x, Y_ALIGN+y, 0, 168, 64,  8,  8, 1)

    @classmethod
    def rod(cls, rx, ry, dirc):
        if dirc==UP:
            pyxel.blt(rx, Y_ALIGN+ry, 0, 92, 64, 4, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(rx, Y_ALIGN+ry, 0, 92, 64, 4, -16, 1)
        elif dirc==LEFT:
            pyxel.blt(rx, Y_ALIGN+ry, 0, 176, 64, -16, 4, 1)
        elif dirc==RIGHT:
            pyxel.blt(rx, Y_ALIGN+ry, 0, 176, 64, 16, 4, 1)

    @classmethod
    def rodbeam(cls, x, y, dirc, cnt):
        ptn = cnt%4
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 0, 128+16*ptn, 80, 16, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 0, 128+16*ptn, 80, 16, -16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 0, 192+16*ptn, 80, -16, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 0, 192+16*ptn, 80, 16, 16, 1)

    @classmethod
    def food(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 0, 96, 64, 8, 16, 1)

    @classmethod
    def wind(cls, x, y, cnt):  # cnt=0～
        ptn = cnt%4
        pyxel.blt(x, Y_ALIGN+y, 0, 144+16*ptn, 0, 16 if x<CENTER_X else -16, 16, 1)

    @classmethod
    def princess(cls, x, y, ptn):
        pyxel.blt(x, Y_ALIGN+y, 0, 224+16*ptn, 0, 16, 16, 1)

    @classmethod
    def oldman1(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 0, 0, 112, 16, 16, 1)

    @classmethod
    def oldman2(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 0, 16, 112, 16, 16, 1)

    @classmethod
    def oldwoman(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 0, 32, 112, 16, 16, 1)

    @classmethod
    def merchant(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 0, 48, 112, 16, 16, 1)

    @classmethod
    def ownrupee(cls, x, y, player_rupee):
        pyxel.blt(x, y, 0, 16, 96, 8, 8, 1)  # Rupee
        pyxel.text(x+12, y+2, '999' if player_rupee>999 else f'{player_rupee}', 7)

    @classmethod
    def ownbomb(cls, x, y, player_maxmbomb, player_bomb):
        if player_maxmbomb>0:
            pyxel.blt(x, y, 0, 16, 104, 8, 8, 1)  # Bomb
            pyxel.text(x+12, y+2, '99' if player_bomb>99 else f'{player_bomb}', 7)

    @classmethod
    def ownheart(cls, x, y, player_maxhp, player_hp):
        fn = (player_hp+3)//8  # Full_Heart数:
        r = player_hp-fn*8  # HP残り
        for i in range(fn):
            pyxel.blt(x+i*8, y, 0, 0, 104, 8, 8, 1)  # Full_Heart
        nx = fn*8  # 次の表示位置
        hn = (r+3)//4  # HP残り
        if hn:
            pyxel.blt(x+nx, y, 0, 8, 96, 8, 8, 1)  # Half_Heart
        nx += hn*8  # 次の表示位置
        en = player_maxhp//8-(fn+hn) 
        for i in range(en):
            pyxel.blt(x+nx+i*8, y, 0, 0, 96, 8, 8, 1)  # Empty_Heart
        #pyxel.text(x+nx+en*8, y+1, f'{player_hp}', 7)

    @classmethod
    def item(cls, x, y, item, align=False):
        ax = 4 if align else 0
        if item==W_SWORD:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 0, 64, 8, 16, 1)
        elif item==W_WHITE_SWORD:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 8, 64, 8, 16, 1)
        elif item==W_MAGICAL_SWORD:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 16, 64, 8, 16, 1)
        elif item==I_BOOMERANG:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 24, 64, 8, 16, 1)
        elif item==I_MAGICAL_BOOMERANG:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 32, 64, 8, 16, 1)
        elif item==I_BOMB:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 40, 64, 8, 16, 1)
        elif item==I_ARROW:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 48, 64, 5, 16, 1)
        elif item==I_SILVER_ARROW:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 56, 64, 5, 16, 1)
        elif item==I_BOW:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 64, 64, 8, 16, 1)
        elif item==I_BLUE_CANDLE:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 72, 64, 8, 16, 1)
        elif item==I_RED_CANDLE:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 80, 64, 8, 16, 1)
        elif item==I_RECORDER:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 88, 64, 4, 16, 1)
        elif item==I_MAGICAL_ROD:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 92, 64, 4, 16, 1)
        elif item==I_FOOD:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 96, 64, 8, 16, 1)
        elif item==I_LETTER:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 104, 64, 8, 16, 1)
        elif item==I_LIFE_POTION:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 112, 64, 8, 16, 1)
        elif item==I_2ND_POTION:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 120, 64, 8, 16, 1)
        elif item==I_BLUE_RING:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 128, 64, 8, 16, 1)
        elif item==I_RED_RING:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 136, 64, 8, 16, 1)
        elif item==I_POWER_BRACELET:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 144, 64, 8, 16, 1)
        elif item==I_BIBLE:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 152, 64, 8, 16, 1)
        elif item==I_MAGICAL_SHIELD:
            pyxel.blt(x+ax, Y_ALIGN+y, 0, 160, 64, 8, 16, 1)
        elif item==I_HEART_CONTAINER:
            pyxel.blt(x, Y_ALIGN+y, 0, 24, 96, 16, 16, 1)
        elif item==I_MOREBOMB:
            pyxel.blt(x, Y_ALIGN+y, 0, 96, 96, 16, 16, 1)
        elif item in (R_GETRUPEE100, R_GETRUPEE30):
            Draw.rupee(x+ax, y, pyxel.frame_count//4%2)
        elif item==R_PAYRUPEE:
            Draw.rupee(x+ax, y, 2)

    @classmethod
    def flame(cls, x, y, ptn):
        pyxel.blt(x, Y_ALIGN+y, 0, 128, 0, 16 if ptn else -16, 16, 0)

    @classmethod
    def smoke(cls, x, y, cnt):  # ctn=0～16
        if cnt>11:
            pyxel.blt(x, Y_ALIGN+y, 0, 16*5, 0, 16, 16, 1)
        elif cnt>6:
            pyxel.blt(x, Y_ALIGN+y, 0, 16*6, 0, 16, 16, 1)
        else:
            pyxel.blt(x, Y_ALIGN+y, 0, 16*7, 0, 16, 16, 1)

    @classmethod
    def flash(cls, x, y, cnt):  # ctn=0～16
        if cnt>12:
            pyxel.blt(x, Y_ALIGN+y, 0, 16, 0, 16, 16, 1)
        elif cnt>8:
            pyxel.blt(x, Y_ALIGN+y, 0, 16*2, 0, 16, 16, 1)
        elif cnt>4:
            pyxel.blt(x, Y_ALIGN+y, 0, 16*3, 0, 16, 16, 1)
        else:
            pyxel.blt(x, Y_ALIGN+y, 0, 16*4, 0, 16, 16, 1)

    @classmethod
    def rock(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 0, 16, 176, 16, 16, 1)  # 茶岩

    @classmethod
    def rupee(cls, x, y, ptn=0):  # ptn=0～1
        pyxel.blt(x, Y_ALIGN+y, 0, 72+8*ptn, 96, 8, 16, 1)

    @classmethod
    def heart(cls, x, y, ptn=0):  # ptn=0～1
        pyxel.blt(x, Y_ALIGN+y, 0, ptn*8, 104, 8, 8, 1)

    @classmethod
    def octorok(cls, x, y, dirc, ptn=0):  # ptn=0～1
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*ptn, 0, 16, -16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*ptn, 0, 16, 16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*2+16*ptn, 0, 16, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*2+16*ptn, 0, -16, 16, 1)

    @classmethod
    def blueoctorok(cls, x, y, dirc, ptn=0):  # ptn=0～1
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*4+16*ptn, 0, 16, -16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*4+16*ptn, 0, 16, 16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*6+16*ptn, 0, 16, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*6+16*ptn, 0, -16, 16, 1)

    @classmethod
    def octorokrock(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 1, 128, 0, 8, 10, 1)

    @classmethod
    def moblin(cls, x, y, dirc=DOWN, ptn=0):  # ptn = 0～1
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 16, 16, 16 if ptn else -16, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 0, 16, 16 if ptn else -16, 16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*2+16*ptn, 16, -16, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*2+16*ptn, 16, 16, 16, 1)

    @classmethod
    def bluemoblin(cls, x, y, dirc, ptn=0):  # ptn = 0～1
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*5, 16, 16 if ptn else -16, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*4, 16, 16 if ptn else -16, 16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*6+16*ptn, 16, -16, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*6+16*ptn, 16, 16, 16, 1)

    @classmethod
    def moblinarrow(cls, x, y, dirc):
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 128, 16, 5, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 128, 16, 5, -16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 136, 16, -16, 5, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 136, 16, 16, 5, 1)

    @classmethod
    def lynel(cls, x, y, dirc=DOWN, ptn=0):  # ptn = 0～1
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 16, 112, 16 if ptn else -16, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 0, 112, 16 if ptn else -16, 16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*2+16*ptn, 112, -16, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*2+16*ptn, 112, 16, 16, 1)

    @classmethod
    def bluelynel(cls, x, y, dirc, ptn=0):  # ptn = 0～1
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*5, 112, 16 if ptn else -16, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*4, 112, 16 if ptn else -16, 16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*6+16*ptn, 112, -16, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 16*6+16*ptn, 112, 16, 16, 1)

    @classmethod
    def lynelsword(cls, x, y, dirc, ptn):  # ptn = 0～4
        if dirc==UP:
            pyxel.blt(x, Y_ALIGN+y, 1, 128+8*ptn, 112, 7, 16, 1)
        elif dirc==DOWN:
            pyxel.blt(x, Y_ALIGN+y, 1, 128+8*ptn, 112, 7, -16, 1)
        elif dirc==LEFT:
            pyxel.blt(x, Y_ALIGN+y, 1, 176 if ptn in (2,3) else 160, 120 if ptn in (1,3) else 112, -16, 7, 1)
        elif dirc==RIGHT:
            pyxel.blt(x, Y_ALIGN+y, 1, 176 if ptn in (2,3) else 160, 120 if ptn in (1,3) else 112, 16, 7, 1)

    @classmethod
    def tektite(cls, x, y, ptn=0):  # ptn = 0～1
        pyxel.blt(x, Y_ALIGN+y, 1, 16*ptn, 32, 16, 16, 1)

    @classmethod
    def bluetektite(cls, x, y, ptn=0):  # ptn = 0～1
        pyxel.blt(x, Y_ALIGN+y, 1, 32+16*ptn, 32, 16, 16, 1)

    @classmethod
    def dodongo(cls, x, y, dirc, ptn):  # ptn = 0～1
        if dirc==UP:
            if ptn==2:
                pyxel.blt(x, Y_ALIGN+y, 1, 48, 192, 16, 16, 1)
            else:
                pyxel.blt(x, Y_ALIGN+y, 1, 32, 192, 16 if ptn else -16, 16, 1)
        elif dirc==DOWN:
            if ptn==2:
                pyxel.blt(x, Y_ALIGN+y, 1, 16, 192, 16, 16, 1)
            else:
                pyxel.blt(x, Y_ALIGN+y, 1, 0, 192, 16 if ptn else -16, 16, 1)
        elif dirc==LEFT:
            pyxel.blt(x-6, Y_ALIGN+y, 1, 64+32*ptn, 192, -28, 16, 1)
        elif dirc==RIGHT:
            pyxel.blt(x-6, Y_ALIGN+y, 1, 64+32*ptn, 192, 28, 16, 1)

    @classmethod
    def testitart_body(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 1, 64, 208, 16, 16, 1)

    @classmethod
    def testitart_leftclaw(cls, x, y, ptn):  # ptn = 0,1
        pyxel.blt(x, Y_ALIGN+y, 1, 0 if ptn else 16, 208, 16, 16, 1)

    @classmethod
    def testitart_rightclaw(cls, x, y, ptn):  # ptn = 0,1
        pyxel.blt(x, Y_ALIGN+y, 1, 0 if ptn else 16, 208, -16, 16, 1)

    @classmethod
    def testitart_upclaw(cls, x, y, ptn):  # ptn = 0,1
        pyxel.blt(x, Y_ALIGN+y, 1, 32 if ptn else 48, 208, 16, 16, 1)

    @classmethod
    def testitart_downclaw(cls, x, y, ptn):  # ptn = 0,1
        pyxel.blt(x, Y_ALIGN+y, 1, 32 if ptn else 48, 208, 16, -16, 1)

    @classmethod
    def digdogger(cls, x, y, small, ptn):  # ptn = 0～4
        if small:
            pyxel.blt(x, Y_ALIGN+y, 1, 96, 160 if ptn==0 else 176, 16, 16, 1)
        else:
            if ptn==0:
                pyxel.blt(x-6, Y_ALIGN+y-8, 1, 0, 160, 28, 32, 1)
            else:
                pyxel.blt(x-6, Y_ALIGN+y-8, 1, 32 if ptn in (1,3) else 64, 160, 28 if ptn in (1,2) else -28, 32, 1)

    @classmethod
    def gohma(cls, x, y, ptn, eye):  # ptn = 0～1, eye = 1～
        pyxel.blt(x-16, Y_ALIGN+y, 1, 0 if ptn==0 else 16, 144, 16, 16, 1)
        pyxel.blt(x+16, Y_ALIGN+y, 1, 16 if ptn==0 else 0, 144, -16, 16, 1)
        if eye>80:
            pyxel.blt(x, Y_ALIGN+y, 1, 32, 144, 16, 16, 1)
        elif eye>70:
            pyxel.blt(x, Y_ALIGN+y, 1, 48, 144, 16, 16, 1)
        elif eye>60:
            pyxel.blt(x, Y_ALIGN+y, 1, 64, 144, 16, 16, 1)
        elif eye>20:
            pyxel.blt(x, Y_ALIGN+y, 1, 80, 144, 16, 16, 1)
        elif eye>10:
            pyxel.blt(x, Y_ALIGN+y, 1, 64, 144, 16, 16, 1)
        else:
            pyxel.blt(x, Y_ALIGN+y, 1, 48, 144, 16, 16, 1)

    @classmethod
    def gleeokbody(cls, x, y, ptn):  # ptn = 0～3
        if ptn==3:
            ptn = 1
        pyxel.blt(x, Y_ALIGN+y, 1, 24*ptn, 224, 24, 32, 1)  # 体
        cls.gleeokneck(x+8, y+22)  # 首

    @classmethod
    def gleeokneck(cls, x, y):
        pyxel.blt(x, Y_ALIGN+y, 1, 72, 224, 8, 12, 1)  # 首

    @classmethod
    def gleeokhead1(cls, x, y, ptn=0):  # ptn = 0～1
        if ptn==0:
            pyxel.blt(x, Y_ALIGN+y, 1, 80, 224, 8, 16, 1)
        else:
            cls.gleeokhead2(x-4, y, 0)

    @classmethod
    def gleeokhead2(cls, x, y, ptn):  # ptn = 0～1
        pyxel.blt(x, Y_ALIGN+y, 1, 88+16*ptn, 224, 16, 16, 1)

    @classmethod
    def beam(cls, x, y, ptn):  # ptn = 0～3
        pyxel.blt(x, Y_ALIGN+y, 1, 72+8*ptn, 240, 8, 10, 1)

App()

