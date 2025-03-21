# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# bird.py
import pygame
from settings import import_sprite



class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # bird basic info
        self.frame_index = 0
        self.animation_delay = 3 # WAS 7
        self.jump_move = -9

        # bird animation
        self.bird_img = import_sprite("assets/bird/new")
        self.crash_img = pygame.image.load("assets/bird/JazzyFly_Crash.png") # Load the crash sprite
        self.crash_img = pygame.transform.scale(self.crash_img, (size,size)) # scale to match bird size

        self.image = self.bird_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)

        # bird status
        self.direction = pygame.math.Vector2(0, 0)
        self.score = 0
        # load sound fx
        self.flap_sound = pygame.mixer.Sound("assets/sounds/sfx_wing.mp3")

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
        self.flap_sound.play()

    # Method for crashing bird sprite
    def show_crash_sprite(self):
        self.image = self.crash_img
        self.mask = pygame.mask.from_surface(self.image)

    # updates the bird's overall state
    def update(self, is_jump):
        if is_jump:
            self._jump()
        self._animate()
