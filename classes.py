from tela_inicial import *

class map:
    def __init__(self, largura, altura):
        self.width = largura
        self.height = altura
        self.offsetx = 0
        self.offsety = 0
        self.image = pygame.image.load('assets/tomb_of_foxy_inicio.png').convert
        self.image = pygame.transform.scale(self.image,(self.width, self.height))

    def movimento_mapa(self, dx, dy):
        self.offsetx += dx
        self.offsety += dy

    def desenhar_mapa(self, screen):
        screen.blit(self.image, )
    



        