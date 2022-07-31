import pygame
dog = False
while dog == False:
    pygame.init()
    pygame.mixer.music.load('ex01.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
