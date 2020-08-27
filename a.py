import pygame

def convert():
    pygame.init()
    pygame.display.set_mode()
    image = pygame.image.load("download.png").convert_alpha()
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            if image.get_at((x, y)) == (255, 255, 255, 255):
                image.set_at((x, y), (255, 255, 255, 0))
    pygame.image.save(image, "dot.png")

convert()