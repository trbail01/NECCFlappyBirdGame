# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# bird.py
import pygame
from settings import BIRD_JUMP_VELOCITY, asset_path, import_sprites

class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.frame_index = 0
        self.animation_delay = 3
        self.jump_move = BIRD_JUMP_VELOCITY

        self.frames = [
            pygame.transform.scale(frame, size)
            for frame in import_sprites("bird/new")
        ]
        crash_image = pygame.image.load(asset_path("bird/JazzyFly_Crash.png")).convert_alpha()
        self.crash_img = pygame.transform.scale(crash_image, size)

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.direction = pygame.math.Vector2(0, 0)
        self.score = 0
        self.crashed = False
        self.flap_sound = pygame.mixer.Sound(asset_path("sounds/sfx_wing.mp3"))

    def _animate(self):
        sprite_index = self.frame_index // self.animation_delay
        self.image = self.frames[sprite_index]
        self.frame_index = (self.frame_index + 1) % (len(self.frames) * self.animation_delay)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    def _jump(self):
        self.direction.y = self.jump_move
        self.flap_sound.play()

    def show_crash_sprite(self):
        self.crashed = True
        self.image = self.crash_img
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, is_jump):
        if self.crashed:
            return
        if is_jump:
            self._jump()
        self._animate()
