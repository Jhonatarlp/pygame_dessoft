from config import *
class map(pygame.sprite.Sprite):
    def __init__(self):
        self.width = largura
        self.height = altura
        self.offset_x = 0 
        self.offset_y = 0 
        self.image = image
    
    def movimention(self,dx,dy):
        self.offset_x += dx
        self.offset_y += dy

    def draw(self):
        screen.blit(self.image, (self.offset_x, self.offset_y))

class raposa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/raposa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
    
    def draw(self):
        screen.blit(self.image, (self.x - map.offset_x, self.y - map.offset_y))

    
class jogo:
    def __init__(self):
        while game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        map.movimention(0, -5)
                    elif event.key == K_DOWN:
                        map.movimention(0, 5)
                    elif event.key == K_LEFT:
                        map.movimention(-5, 0)
                    elif event.key == K_RIGHT:
                        map.movimention(5, 0)
