
import constantes 
import pygame
#configurações iniciais 
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
# pygame.display.set_caption(constantes.TITULO)
# clock = pygame.time.Clock()

    
# Classe Tile (representa um caminho)
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, row, column):
        # Inicializa a classe base Sprite
        super().__init__()
        self.tile_type = tile_type  # Define o tipo de tile: "wall" (parede) ou "path" (caminho)

        # Cria uma superfície para o tile e define a cor
        self.image = pygame.Surface((constantes.TAMANHO_QUADRADO, constantes.TAMANHO_QUADRADO))
        self.image.fill(constantes.PRETO if tile_type == "wall" else constantes.PRETO)  # Preto para parede,preto para caminho

        # Obtém o retângulo de posição do tile e define sua posição na grade
        self.rect = self.image.get_rect()
        self.rect.x = column * constantes.TAMANHO_QUADRADO  # Posição X com base na coluna e no tamanho do tile
        self.rect.y = row * constantes.TAMANHO_QUADRADO     # Posição Y com base na linha e no tamanho do tile
        
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

        # def novo_jogo(self):
        #     self.all.sprites = pygame.sprite.Group()
        #     self.rodar()
        
        # #loop do jogo    
        # def rodar(self):
        #     self.jogando = True 
        #     while self.jogando:
        #         self.clock.ticket(constantes.FPS)
        #         self.eventos()
        #         self.refresh_sprites()
        #         self.desenhar_sprites()
            
    
    



        