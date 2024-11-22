# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# bird.py
import pygame
from settings import import_sprite
# This is a test
class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # bird basic info
        self.frame_index = 0
        self.animation_delay = 7 # WAS 3
        self.jump_move = -9
        # bird animation
        self.bird_img = import_sprite("assets/bird")
        self.image = self.bird_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        # bird status
        self.direction = pygame.math.Vector2(0, 0)
        self.score = 0

    # for bird's flying animation
    def _animate(self):
        sprites = self.bird_img
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0

    # to make the bird fly higher
    def _jump(self):
        self.direction.y = self.jump_move

    # updates the bird's overall state
    def update(self, is_jump):
        if is_jump:
            self._jump()
        self._animate()
