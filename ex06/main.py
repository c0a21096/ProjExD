import pygame as pg
import sys


#画像読み込み
PLAYER_IMG = "fig/0.png"
BULLET_IMG = "fig/9.png"
ENEMY_IMG = "fig/6.png"
BACKGROUND_IMG = "fig/pg_bg.jpg"

#定数定義
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_ENEMY_NUM = 20


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Player:
    
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()          
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        #操作反映
        key_states = pg.key.get_pressed()
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1

        #領域外かどうか判定
        if self.rct.left <= scr.rct.left:
            self.rct.centerx += 1
        elif self.rct.right >= scr.rct.right:
            self.rct.centerx -= 1
        
        self.blit(scr)


class Bullet:
    
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()          
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        self.rct.move_ip(0, -1)
        self.blit(scr)
        


class Enemy:

    def __init__(self, image: str, size: float, xy, vx, vy):
        self.sfc = pg.image.load(image)    
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()          
        self.rct.center = xy
        self.vx = vx #自身の向き(左:-1, 右:1)
        self.vy = vy
        self.flame = 0
        self.move_count = 0

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        self.flame += 1
        if self.flame % 1000 == 0:
            if self.move_count >= 5:
                self.rct.move_ip(0, self.vy)
                self.vx *= -1
                self.move_count = 0
            else:
                self.rct.move_ip(self.vx, 0)
                self.move_count += 1
            
        self.blit(scr)


if __name__ == "__main__": #main
    pg.init()
    screen = Screen("shoot", (SCREEN_WIDTH, SCREEN_HEIGHT), BACKGROUND_IMG)
    player = Player(PLAYER_IMG, 1.0, (SCREEN_WIDTH/2, 500))
    bullets = []
    enemys =[]
    for i in range(MAX_ENEMY_NUM//5):
        for j in range(MAX_ENEMY_NUM//4):
            enemy = Enemy(
                    ENEMY_IMG, 
                    1.0, 
                    (50+j*100, (i+1)*50), 
                    20, 
                    50)
            enemys.append(enemy)

    while True: #mainloop

        for event in pg.event.get():
            #終了用イベント
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            #shot判定
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                bullet = Bullet(BULLET_IMG, 0.5, (player.rct.center))
                bullets.append(bullet)

        screen.blit()
        player.update(screen)
        if bullets:
            for i in range(len(bullets)):
                bullets[i].update(screen)
            for bullet in bullets:
                if bullet.rct.top <= 0:
                    del bullet    
        for enemy in enemys:
            enemy.update(screen)
        
        #ヒット判定
        for bullet in bullets:
            for enemy in enemys:
                if bullet.rct.colliderect(enemy.rct):
                    del bullet
                    del enemy
                    break

        pg.display.update()
