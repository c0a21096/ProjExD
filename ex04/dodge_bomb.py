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
    bombimg_rect = bombimg_sfc.get_rect()
    bombimg_rect.centerx = random.randint(0, screen_rect.width)
    bombimg_rect.centery = random.randint(0, screen_rect.height)

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
        
        screen_sfc.blit(koukatonimg_sfc, koukatonimg_rect)
        screen_sfc.blit(bombimg_sfc, bombimg_rect)
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()