
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
        self.tile_type = tile_type  # Define o tipo de tile: "wall" ou "path"

        # Cria uma superfície para o tile e define a cor
        self.image = pygame.Surface((constantes.TAMANHO_QUADRADO, constantes.TAMANHO_QUADRADO))
        self.image.fill(constantes.PRETO if tile_type == "wall" else constantes.BRANCO)  # Preto para parede,branco para caminho

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

    # def morrer(self):
    #     self.kill()  # Remove o obstáculo do grupo de sprites
        
class Jogador:
    def __init__(self, x, y, velocidade,imagem):
        self.posicao = pygame.Vector2(x, y)
        self.velocidade = velocidade
        self.direcao = None
        
        # Carrega a imagem do jogador
        self.image = pygame.image.load(constantes.IMG_DIR / 'foxy1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))  # Redimensiona 

        # Define o rect com base na posição do jogador e na imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicao.x, self.posicao.y)  # A posição inicial do jogador no jogo


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
            
            # Atualizando o rect com a nova posição
        self.rect.topleft = (self.posicao.x, self.posicao.y)

    def desenhar(self, screen):
        # 'Desenha' o jogador 
        screen.blit(self.image, self.rect)
        
        
        
    def verificar_colisao(self, obstaculos):
        # Verifica colisão com os obstáculos
        for obstaculo in obstaculos:
            if self.rect.colliderect(obstaculo.rect):
                return True  # Retorna verdadeiro se houver colisão
        return False    

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
            
    
    



        