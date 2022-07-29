from pygame import *
font.init()
win_x = 700
win_y = 500
font = font.SysFont('Arial',40)
run = True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_x_speed,player_y_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
    def fire(self):
        bullet = Bullet('bullet.jpg',self.rect.right,self.rect.centery,25,15,15)
        bullets.add(bullet)
class enemy(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_x_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.x_speed = player_x_speed
        self.direction = 'left'
    def update(self):
        if self.rect.x > 420:
            self.direction = 'left'
        if self.rect.x < 80:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -=self.x_speed
        elif self.direction == 'right':
            self.rect.x +=self.x_speed
class Bullet(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x > win_x + 10:
            self.kill
window = display.set_mode((win_x,win_y))
display.set_caption("Лабиринт!")
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)
enemy1 = enemy('ghost.jpg',500,40,60,50,5)
final = GameSprite('without_name.png',650,420,40,40)
packman = Player('packman.png',5, 420,60,60,0,0)
wall_2 = GameSprite('1071741.png',100,150,300,10)
wall_1 = GameSprite('1071741.png',370,100,50,400)
wall_3 = GameSprite('1071741.png',540,100,160,10)
wall_4 = GameSprite('1071741.png',390,200,160,10)
wall_5 = GameSprite('1071741.png',540,300,160,10)
wall_6 = GameSprite('1071741.png',0,400,260,10)
finish = False
Final_end = sprite.Group()
barriers = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
monsters.add(enemy1)
Final_end.add(final)
barriers.add(wall_1)
barriers.add(wall_2)
barriers.add(wall_3)
barriers.add(wall_4)
barriers.add(wall_5)
barriers.add(wall_6)
win_pic = transform.scale(image.load('cool_final.png'),(700,500))
los_pic = transform.scale(image.load('loser.jpg'),(700,500))
while run:
    time.delay(30)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                packman.x_speed = -5
            elif e.key == K_d:
                packman.x_speed = 5
            elif e.key == K_w:
                packman.y_speed = -5
            elif e.key == K_s:
                packman.y_speed = 5
            elif e.key == K_SPACE:
                packman.fire()
        elif e.type == KEYUP:
            if e.key == K_a:
                packman.x_speed =0
            elif e.key == K_d:
                packman.x_speed = 0
            elif e.key == K_w:
                packman.y_speed = 0
            elif e.key == K_s:
                packman.y_speed = 0
    if finish != True:
        window.fill((DARK_BLUE))
        packman.update()
        packman.reset()
        bullets.update()
        bullets.draw(window)
        barriers.draw(window)
        final.reset()
        sprite.groupcollide(monsters,bullets,True,True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets,barriers,True,False)
        if sprite.spritecollide(packman,monsters,False):
            window.blit(los_pic,(0,0))
            packman.kill()
            finish = True
        final_touched = sprite.spritecollide(packman,Final_end,False)
        platforms_touched = sprite.spritecollide(packman,barriers,False)
        for p in platforms_touched:
            window.blit(los_pic,(0,0))
            packman.kill()
            finish = True
        for p in final_touched:
            window.blit(win_pic,(0,0))
            packman.kill
            finish =True
    display.update()
