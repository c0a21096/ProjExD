import pygame as pg
import sys
import random


class Screen:

    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:

    #key_delta = {UP:(0, -1), DOWN:(0, 1), 
    #             LEFT:(-1, 0), RIGHT:(1, 0)}

    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()     # Rect
        self.rct.center = xy

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)

    def attack(self):
        return Shot(self, "fig/beam.png", 0.2)


class Bomb:
    def __init__(self, color, size, vxy, scr):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
        

class Shot:
    def __init__(self, chr:Bird, image, size):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()     # Rect
        self.rct.midleft = chr.rct.center

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        self.rct.move_ip(5, 0)
        self.blit(scr)
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            del self


def main():
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    beam = None
    beams = []
    bkd_num = 3
    bkds = [0]*bkd_num
    for i in range(bkd_num):
        bkds[i] = Bomb((255, 0, 0), 10, (i+1, i+1), scr)

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beams.append(kkt.attack())
  
        kkt.update(scr)
        for bkd in bkds:
            bkd.update(scr)
        if len(beams) != 0:
            for beam in beams:
                beam.update(scr) 

        for beam in beams:
            for i in range(len(bkds)):
                if beam.rct.colliderect(bkds[i].rct):
                    bkds[i] = 0
        # for i in bkds:
        #     if  kkt.rct.colliderect(i.rct):
        #         return 
 
        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()