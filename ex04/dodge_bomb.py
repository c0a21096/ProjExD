import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #surface
    screen_rect = screen_sfc.get_rect()

    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rect)

    koukatonimg_sfc = pg.image.load("fig/6.png")
    koukatonimg_sfc = pg.transform.rotozoom(koukatonimg_sfc, 0, 2.0) 
    koukatonimg_rect = koukatonimg_sfc.get_rect()
    koukatonimg_rect.center = 900, 400

    bombimg_sfc = pg.Surface((20, 20))
    bombimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bombimg_sfc, (255, 0, 0), (10, 10), 10)
    bomb_num = 30
    bombimg_rect = [0]*bomb_num
    vx = [0]*bomb_num
    vy = [0]*bomb_num
    for i in range(bomb_num):
        bombimg_rect[i] = bombimg_sfc.get_rect()
        bombimg_rect[i].centerx = random.randint(10, screen_rect.width-10)
        bombimg_rect[i].centery = random.randint(10, screen_rect.height-10)
        vx[i] = 1
        vy[i] = 1

    life_sfc = pg.Surface((20, 20))
    life_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(life_sfc, (0, 255, 0), (10, 10), 10)
    pl_life = 1500
    life_rect = [0]*pl_life
    for i in range(pl_life):
        life_rect[i] = life_sfc.get_rect()
        life_rect[i].center = 10+i, 10

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)
        
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True:
            koukatonimg_rect.centery -= 1
        if key_states[pg.K_DOWN] == True:
            koukatonimg_rect.centery += 1
        if key_states[pg.K_LEFT] == True:
            koukatonimg_rect.centerx -= 1
        if key_states[pg.K_RIGHT] == True:
            koukatonimg_rect.centerx += 1
        if check_bound(koukatonimg_rect, screen_rect) != (1, 1):
            if key_states[pg.K_UP] == True:
                koukatonimg_rect.centery += 1
            if key_states[pg.K_DOWN] == True:
                koukatonimg_rect.centery -= 1
            if key_states[pg.K_LEFT] == True:
                koukatonimg_rect.centerx += 1
            if key_states[pg.K_RIGHT] == True:
                koukatonimg_rect.centerx -= 1
        screen_sfc.blit(koukatonimg_sfc, koukatonimg_rect) 

        for i in range(bomb_num):
            yoko, tate = check_bound(bombimg_rect[i], screen_rect)
            vx[i] *= yoko
            vy[i] *= tate
            bombimg_rect[i].move_ip(vx[i], vy[i])
            screen_sfc.blit(bombimg_sfc, bombimg_rect[i])

        for i in range(bomb_num):    
            if koukatonimg_rect.colliderect(bombimg_rect[i]):
                pl_life -= 1
        for i in range(pl_life):
            screen_sfc.blit(life_sfc, life_rect[i])

        if pl_life <= 0:
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rect, scr_rect):
    #[1]rct:こうかとん or bomb
    #[2]scr_rect:スクリーンのrect
    yoko, tate = +1, +1 #領域内かどうか
    if rect.left < scr_rect.left or scr_rect.right < rect.right:
        yoko = -1
    if rect.top < scr_rect.top or scr_rect.bottom < rect.bottom:
        tate = -1
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()