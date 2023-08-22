import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Hello pygame")
clock = pygame.time.Clock()

sky_surface = pygame.image.load("graphics/Sky.png")
sky_surface = pygame.transform.scale(sky_surface, (1000, 600))

ground_surface = pygame.image.load("graphics/Ground.png")
ground_surface = pygame.transform.scale(ground_surface, (1000, 100))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surface, (0, 0))
	screen.blit(ground_surface, (0, 500))

	pygame.display.update()
	clock.tick(60)