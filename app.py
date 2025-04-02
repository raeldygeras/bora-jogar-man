import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Convite para Jogar 🎮🔥")

# Cores
PRETO = (0, 0, 0)
AZUL = (0, 150, 255)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Fonte
fonte = pygame.font.Font(None, 40)

# Lista de elementos animados
estrelas = []

# Classe para criar estrelas subindo
class Estrela:
    def __init__(self):
        self.x = random.randint(50, LARGURA - 50)
        self.y = ALTURA
        self.velocidade = random.uniform(1, 3)
        self.tamanho = random.randint(5, 15)
        self.cor = AZUL

    def mover(self):
        self.y -= self.velocidade  # Movimento para cima

    def desenhar(self):
        pygame.draw.circle(screen, self.cor, (self.x, self.y), self.tamanho)

# Estado do jogo
mostrar_convite = False
respondeu = False
pos_x_nao = 350  # Posição inicial do botão "Não"

# Loop principal
rodando = True
relogio = pygame.time.Clock()
tempo_inicio = pygame.time.get_ticks()

while rodando:
    screen.fill(PRETO)  # Fundo preto

    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if mostrar_convite and not respondeu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 150 <= x <= 250 and 400 <= y <= 450:  # Botão "Sim"
                    respondeu = True
                if pos_x_nao <= x <= pos_x_nao + 100 and 400 <= y <= 450:  # Botão "Não"
                    pos_x_nao = random.randint(50, 500)  # Faz o botão fugir

    # Criar estrelas enquanto o convite não aparece
    if not mostrar_convite:
        if random.randint(1, 20) == 1:
            estrelas.append(Estrela())

        for estrela in estrelas[:]:
            estrela.mover()
            estrela.desenhar()
            if estrela.y < -20:
                estrelas.remove(estrela)

        # Depois de 5 segundos, mostra o convite
        if pygame.time.get_ticks() - tempo_inicio > 5000:
            mostrar_convite = True

    # Exibe o convite para jogar
    if mostrar_convite:
        texto = fonte.render("Bora jogar? 🎮🔥", True, BRANCO)
        screen.blit(texto, (LARGURA // 2 - 100, 300))

        if respondeu:
            resposta = fonte.render("Partiu! 🚀", True, VERDE)
            screen.blit(resposta, (LARGURA // 2 - 50, 400))
        else:
            # Botão "Sim"
            pygame.draw.rect(screen, VERDE, (150, 400, 100, 50))
            texto_sim = fonte.render("Sim", True, PRETO)
            screen.blit(texto_sim, (180, 410))

            # Botão "Não" (que foge)
            pygame.draw.rect(screen, VERMELHO, (pos_x_nao, 400, 100, 50))
            texto_nao = fonte.render("Não", True, PRETO)
            screen.blit(texto_nao, (pos_x_nao + 30, 410))

    # Atualiza a tela
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
