import pygame as pg
from collision import Object, CorePlayer

window_width, window_height = 900, 500
window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Walls!")

run = True
clock = pg.time.Clock()
fps = 60

player = CorePlayer(100, 200, "Ship", scale=2)
objects = [Object(0, 0, "Plank", 3, 90), Object(360, 0, "Plank", 3, 135)]

x_offset, y_offset = 0, 0

while run:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            ...
            
    player.script()

    player.collide(objects)

    x_offset, y_offset = player.rect.centerx - window_width/2, player.rect.centery - window_height/2

    window.fill((255, 255, 255))
    player.display(window, x_offset, y_offset)
    for obj in objects:
        obj.display(window, x_offset, y_offset)
    pg.display.update()

pg.quit()
quit()
