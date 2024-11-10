
from constantes import *
import pygame
import constantes

    
# Classe Tile (representa um caminho)
# Atualiza a classe Tile para usar as imagens diretamente
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_img, row, column):
        super().__init__()
        self.image = tile_img  # A imagem já é carregada no assets
        self.rect = self.image.get_rect()
        self.rect.x = column * TAMANHO_QUADRADO  # Posição X com base na coluna e no tamanho do tile
        self.rect.y = row * TAMANHO_QUADRADO     # Posição Y com base na linha e no tamanho do tile
# Classe Obstáculo (obstáculo que "morre" ao colidir)
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Tamanho do obstáculo
        self.image.fill(constantes.VERMELHO)   # Cor do obstáculo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def morrer(self):
        self.kill()  # Remove o obstáculo do grupo de sprites
        
class Jogador:
    def __init__(self, x, y, velocidade):
        self.posicao = pygame.Vector2(x, y)
        self.velocidade = velocidade
        self.direcao = None

    def movimentar(self):
        # Movimenta o jogador com base na direção atual
        if self.direcao == "cima":
            self.posicao.y -= self.velocidade
        elif self.direcao == "baixo":
            self.posicao.y += self.velocidade
        elif self.direcao == "esquerda":
            self.posicao.x -= self.velocidade
        elif self.direcao == "direita":
            self.posicao.x += self.velocidade

    def desenhar(self, screen):
        # Desenha o jogador como um quadrado azul
        pygame.draw.rect(screen, constantes.AZUL, (self.posicao.x, self.posicao.y, 40, 40))
    
    



        