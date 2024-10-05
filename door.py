import pygame as pg

pg.font.init()

window_width, window_height = 900, 500
window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Doors!")

run = True
fps = 60
clock = pg.time.Clock()

assets = {"Door": pg.transform.scale_by(pg.transform.rotate(pg.image.load("assets/Plank.png"), 90), 3), "Player": pg.Surface((50, 50))}
assets["Player"].fill((200, 0, 0))



class Player:
    def __init__(self, x, y, name) -> None:
        self.image = assets[name]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name
        self.speed = 4
        self.mask = pg.mask.from_surface(self.image)

    def display(self, window: pg.Surface):
        window.blit(self.image, self.rect)

    def script(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed


class Door:
    def __init__(self, x, y, name) -> None:
        self.image = assets[name]
        self.rotatedImage = assets[name]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name
        self.pivot = "topleft"
        self.orientation = "horizontal"
        self.angle = 0
        self.mask = pg.mask.from_surface(self.rotatedImage)
        self.iter = 0
        self.maxSwing = 15
        self.topLev = True

    def display(self, window: pg.Surface):
        window.blit(self.rotatedImage, self.rect)

    def reload(self):
        self.rect = self.rotatedImage.get_rect(topleft=self.rect.topleft)
        self.mask = pg.mask.from_surface(self.rotatedImage)

    def aftScript(self):
        self.topLev = True

    def script(self, player: Player):
        if not pg.sprite.collide_mask(self, player) and self.topLev:
            self.angle += 1
            self.angle = min(max(self.angle, -90), 0)
            self.rotatedImage = pg.transform.rotate(self.image, self.angle)
            self.reload()
            return
        elif not pg.sprite.collide_mask(self, player):
            self.iter = 0
            return
        if player.rect.y < self.rect.bottom:
            self.angle -= 1
            self.angle = min(max(self.angle, -90), 0)
            self.rotatedImage = pg.transform.rotate(self.image, self.angle)
        self.reload()
        self.iter += 1
        if self.iter > self.maxSwing:
            self.iter = 0
            return
        self.topLev = False
        self.script(player)

door = Door(250, 250, "Door")
player = Player(100, 100, "Player")

while run:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    player.script()
    door.script(player)
    door.aftScript()

    window.fill((255, 255, 255))
    window.fill((100, 100, 100), (0, 250, door.rect.x, 24))
    window.fill((100, 100, 100), (250+120, 250, window_width, 24))
    door.display(window)
    player.display(window)
    pg.display.update()
