# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
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
        self.screen.blit(ins1, (70, 400))
        self.screen.blit(ins2, (70, 450))
    def end_game_sprite(self):
        pygame.display.set_caption("NECC Flappy Bird")
        image = pygame.image.load('assets/misc/GameOver.png')
        image = pygame.transform.scale(image, (350, 100))
        self.screen.blit(image, (120,150))
    def end_game_restart_text(self):
        restart_text = "Press \"R\" To Restart The Game"
        restart = self.inst_font.render(restart_text, True, self.inst_color)
        self.screen.blit(restart, (120,100))
    def end_game_score_text(self, int_score):
        final_score = "Final score: " + str(int_score)
        color = pygame.Color(0, 0, 0)

        if int_score <= 5:
            color = pygame.Color(255, 0, 0)  # Red
        elif 5 < int_score < 11:
            color = pygame.Color(255, 255, 0)  # Yellow
        else:
            color = pygame.Color(0, 0, 255)  # Blue

        final = self.inst_font.render(final_score, True, color)
        self.screen.blit(final, (120, 125))
