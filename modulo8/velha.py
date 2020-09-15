import pygame
from pygame.locals import *

simbolo = 'X'
tabuleiro = [[None, None, None],
             [None, None, None],
             [None, None, None]]

pygame.init()

tela = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Jogo da Velha')

#pygame.display.flip()

#desenhar o jogo
fundo = pygame.Surface((300, 300))
fundo.fill((150, 150, 150))
#Linhas Verticais
pygame.draw.line(fundo,(0,0,0), (100, 0), (100, 300), 10)
pygame.draw.line(fundo,(0,0,0), (200, 0), (200, 300), 10)
#Linhas Horizontais
pygame.draw.line(fundo,(0,0,0), (0, 100), (300, 100), 10)
pygame.draw.line(fundo,(0,0,0), (0, 200), (300, 200), 10)

def posicao_tabuleiro(x, y):

    linha, coluna = 0, 0

    if (x < 100):
        coluna = 0
    elif (x < 200):
        coluna = 1
    else:
        coluna = 2

    if (y < 100):
        linha = 0
    elif (y < 200):
        linha = 1
    else:
        linha = 2

    return (linha, coluna)

def desenha_movimento(fundo, linha, coluna, simbolo):
    tabuleiro[linha][coluna] = simbolo
    
    centro_x = (coluna * 100) + 50
    centro_y = (linha * 100) + 50
    
    if (simbolo == 'O'):
        pygame.draw.circle(fundo, (0, 0, 0), (centro_x, centro_y), 35, 10)
    else:
        pygame.draw.line(fundo, (0,0,0), (centro_x -25, centro_y - 25), (centro_x + 25, centro_y + 25), 10)
        pygame.draw.line(fundo, (0,0,0), (centro_x +25, centro_y - 25), (centro_x - 25, centro_y + 25), 10)

def verifica_fim():
    pass    
        

def registra_clique(fundo):
    
    global tabuleiro, simbolo

    (x, y) = pygame.mouse.get_pos()
    (linha, coluna) = posicao_tabuleiro(x, y)

    if(tabuleiro[linha][coluna] is not None):
        return

    desenha_movimento(fundo, linha, coluna, simbolo)

    if (simbolo == 'X'):
        simbolo = 'O'
    else:
        simbolo = 'X'

rodando = True

while rodando:

    #ver eventos de iteração
    for event in pygame.event.get():
        if event.type is QUIT:
            rodando = False
        
        if event.type is MOUSEBUTTONDOWN:
            registra_clique(fundo)
    #verificar se o estado é um fim de jogo
    #verifica_fim()

    #atualizar tela
    tela.blit(fundo, (0,0))
    pygame.display.flip()