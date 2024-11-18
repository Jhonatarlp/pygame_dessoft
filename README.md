# 🦊 **JPygame Dessoft: Tomb Of Foxy** 🎮

## 📖 **Descrição do Projeto**
Este é um jogo de aventura onde o jogador controla uma raposa que deve explorar labirintos, coletar moedas, evitar armadilhas e alcançar o final de cada mapa. Desenvolvido utilizando a biblioteca **Pygame**, o jogo oferece desafios em mapas progressivamente mais difíceis, com animações, música de fundo e uma tela final comemorativa ao completar todos os desafios.

---

## 🚀 **Como Foi Criado**
O jogo foi desenvolvido em Python com a biblioteca **Pygame**, utilizando os seguintes conceitos e recursos:

- **Estrutura de Classes**:
  - Classe `Jogador`: Gerencia as ações do personagem principal, incluindo movimento, animações, e colisões.
  - Classe `Tile`, `Espinho`, `Moeda`, `Fim`: Representam os diferentes elementos do jogo, como caminhos, armadilhas, itens coletáveis e o ponto final.
  
- **Mapas**:
  - Os labirintos são definidos como matrizes em arquivos separados. Cada elemento da matriz corresponde a um tipo de objeto no jogo.

- **Música e Sons**:
  - Adicionamos música de fundo com o módulo `pygame.mixer` para criar uma atmosfera imersiva.

- **Movimentação e Colisões**:
  - Implementamos movimentação baseada em direção e detectamos colisões com paredes, espinhos e moedas utilizando o sistema de retângulos (`rect`) do Pygame.

- **Transição entre Mapas**:
  - Ao completar o mapa atual, o jogador é reposicionado no ponto inicial do próximo mapa.
  - Uma tela final é exibida quando todos os mapas são concluídos.

---

## 🎮 **Como Jogar**

1. **Movimente a Raposa**:
   - Use as **setas do teclado** para mover a raposa:
     - `↑`: Subir.
     - `↓`: Descer.
     - `←`: Esquerda.
     - `→`: Direita.

2. **Objetivo**:
   - Alcance o ponto final do labirinto.
   - Colete moedas para aumentar sua pontuação.
   - Evite colidir com os espinhos, pois cada colisão reduz uma vida.

3. **Transição Entre Mapas**:
   - Complete o mapa atual para avançar para o próximo.

4. **Tela Final**:
   - Ao completar o último mapa, uma tela especial de parabéns será exibida com o tempo total gasto.

---

## 🛠️ **O que foi Usado**
### Tecnologias e Ferramentas:
- **Python 3.11.4**: Linguagem de programação principal.
- **Pygame**: Biblioteca para criação de jogos 2D, responsável por animações, colisões e gerenciamento de sprites.
- **Pygame.mixer**: Usado para adicionar música de fundo.
- **Chat-GPT**: Foi utilizado para auxílio de dúvidas.

### Estrutura do Código:
- **Mapas**:
  - Arquivos que definem os labirintos com matrizes.
  - Exemplo de símbolo no mapa:
    - `'muro'`: Representa as paredes.
    - `'ponto'`: Representa moedas.
    - `'espinho'`: Representa armadilhas.
    - `'fim'`: Representa o ponto de saída.
    - `'inicio'`: Representa a posição inicial do jogador.

- **Sprites**:
  - Imagens utilizadas para representar elementos do jogo, como a raposa animada, moedas e espinhos.

- **Música e Sons**:
  - Arquivo `fundo.mp3` para a trilha sonora do jogo.


## 🌟 **Recursos Implementados**
- **Animações**:
  - A raposa possui animações suaves enquanto está parada ou em movimento.
- **Colisões**:
  - Verificações precisas de colisão entre o jogador e elementos do mapa (moedas, espinhos, paredes).
- **Transição entre Mapas**:
  - Sistema para carregar mapas de forma sequencial.
- **Tela Final**:
  - Tela personalizada exibindo uma mensagem de parabéns e o tempo total de jogo.
- **Música de Fundo**:
  - Adicionada trilha sonora contínua para aumentar a imersão do jogador.

---