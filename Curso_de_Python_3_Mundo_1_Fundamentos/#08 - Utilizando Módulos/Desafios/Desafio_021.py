'''
Desafio 021

Faça um programa em python que abre e reproduza
o áudio de um arquivo MP3.
'''

import pygame

pygame.init()

arquivo_mp3 = '01 - The Day is My Enemy.mp3'

pygame.mixer.init()

pygame.mixer.music.load(arquivo_mp3)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

# Encerra o pygame
pygame.quit()
