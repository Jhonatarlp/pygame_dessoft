from tela_inicial import *
from constantes import *
#configurações iniciais 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
pygame.display.set_caption(constantes.TITULO)
#clock = pygame.time.Clock()
self.esta_rodando = True 
    
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

    def desenhar(self, tela):
        # Desenha o jogador como um quadrado azul
        pygame.draw.rect(tela, AZUL, (self.posicao.x, self.posicao.y, 40, 40))

    def novo_jogo(self):
        self.all.sprites = pygame.sprite.Group()
        self.rodar()
    
    #loop do jogo    
    def rodar(self):
        self.jogando = True 
        while self.jogando:
            self.clock.ticket(constantes.FPS)
            self.eventos()
            self.refresh_sprites()
            self.desenhar_sprites()
        
    
    



        