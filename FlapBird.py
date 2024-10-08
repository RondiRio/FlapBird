import pygame
import os 
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load('imgs/pipe.png'))
IMAGEM_CHAO =  pygame.transform.scale2x(pygame.image.load('imgs/base.png'))
IMAGEM_BACKGROUND =  pygame.transform.scale2x(pygame.image.load('imgs/bg.png'))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load('imgs/bird1.png')),
    pygame.transform.scale2x(pygame.image.load('imgs/bird2.png')),
    pygame.transform.scale2x(pygame.image.load('imgs/bird3.png'))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial',50)

class Passaro:
    IMGS = IMAGEM_PASSARO
    
    
    # Animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]
        
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        
        
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento <0 :
            deslocamento -= 2
        
        self.y += deslocamento

class Cano:
    pass

class Chao:
    pass

# print(IMAGEM_CANO, IMAGEM_BACKGROUND, IMAGEM_CHAO)

# # Teste iniciando o jogo
# pygame.init()
# tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
# pygame.display.set_caption('vendo a imagem')
# rodando_imagem = True

# while rodando_imagem:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False
#     tela.fill((0,0,0))
    
#     tela.blit(IMAGEM_BACKGROUND,(100, 100))
    
#     pygame.display.update()
    
# pygame.quit()
# # fim teste iniciando o jogo

