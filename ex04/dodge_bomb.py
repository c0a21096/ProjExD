import pygame as pg
import sys

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

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)
        screen_sfc.blit(koukatonimg_sfc, koukatonimg_rect)
        
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()