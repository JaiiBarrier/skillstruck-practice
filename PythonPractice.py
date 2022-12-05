import pygame
pygame.init() 

X = 500
Y = 500
GREEN = (11, 194, 0)
PINK = (249, 145, 255)


DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:

	DISPLAY.fill(GREEN)
	
	pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 20],2)
	pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 20],2)
	pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 20],2)
	pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 20],2)
	pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 20],2)
	pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 20],2)
	pygame.display.flip()