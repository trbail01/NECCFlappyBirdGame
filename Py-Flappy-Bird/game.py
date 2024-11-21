# game.py
import pygame
from settings import WIDTH, HEIGHT
from settings import import_sprite

pygame.font.init()

class GameIndicator:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Bauhaus 93', 60)
        self.inst_font = pygame.font.SysFont('Bauhaus 93', 30)
        self.color = pygame.Color("white")
        self.inst_color = pygame.Color("black")


    def show_score(self, int_score):
        bird_score = str(int_score)
        score = self.font.render(bird_score, True, self.color)
        self.screen.blit(score, (WIDTH // 2, 50))

    def instructions(self):
        inst_text1 = "Press SPACE or CLICK button to Jump,"
        inst_text2 = "Press \"R\" Button to Restart Game."
        ins1 = self.inst_font.render(inst_text1, True, self.inst_color)
        ins2 = self.inst_font.render(inst_text2, True, self.inst_color)
        self.screen.blit(ins1, (95, 400))
        self.screen.blit(ins2, (70, 450))
    def end_game_sprite(self):

        pygame.display.set_caption("NECC Flappy Bird")
        image = pygame.image.load('assets/misc/GameOver.png')
        original_width, original_height = image.get_size()
        new_width = int(original_width * 1.5)
        #new_height = int(original_height)
        image = pygame.transform.scale(image, (new_width, original_height))
        self.screen.blit(image, (WIDTH // 2, HEIGHT // 2))
