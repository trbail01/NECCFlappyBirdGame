# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# pipe.py
import pygame
import random


class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, flip):
        super().__init__()
        self.width = width

        # Randomly select a pipe image
        #pipe_number = random.randint(0, 5)
        #img_path = f'assets/terrain/newerPipe{pipe_number}.png'
        img_path = 'assets/terrain/newerPipe2.png'
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        # Flip the pipe if specified
        if flip:
            flipped_image = pygame.transform.flip(self.image, False, True)
            self.image = flipped_image

        self.rect = self.image.get_rect(topleft=pos)

    # Update object position due to world scroll
    def update(self, x_shift):
        self.rect.x += x_shift
        # Remove the pipe from the game when it leaves the screen
        if self.rect.right < (-self.width):
            self.kill()
