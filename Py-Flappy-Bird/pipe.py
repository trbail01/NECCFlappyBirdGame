# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# pipe.py
import pygame
from settings import scaled_image


class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, flip, image_path):
        super().__init__()
        self.image = scaled_image(image_path, (width, height), flip)
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.scored = False

    def update(self, x_shift):
        self.rect.x += x_shift
        if self.rect.right < 0:
            self.kill()
