'''
Desafio 021

Faça um programa em python que abre e reproduza
o áudio de um arquivo MP3.
'''
import pygame

#inciando o pygame
pygame.init()

#funcionalidade mixer e carregamento do arquivo mp3
pygame.mixer.music.load('01 - The Prodigy - Smack My Bitch Up.mp3')

#executando o arquivo mp3
pygame.mixer.music.play()

#esperando o envento terminar para encerrar o programa
pygame.event.wait()