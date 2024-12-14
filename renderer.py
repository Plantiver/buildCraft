import pygame as pg
import numpy as np
import time as t

pg.init()

class Renderer:
    def __init__(self, size:tuple[int,int]) -> None:
        self.tick = pg.time.Clock()
        self.pgScreen = pg.display.set_mode(size)
    
    def render(self, array:np.ndarray):
        self.running=True
        pg.surfarray.blit_array(self.pgScreen, array)
        pg.display.flip()
        while self.running:
            self.tick.tick(1)
            for e in pg.event.get(pg.QUIT):
                if e.type == pg.QUIT:
                    pg.quit()
                    self.running = False
