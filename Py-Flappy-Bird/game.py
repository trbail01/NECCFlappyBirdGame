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
        self.color = pygame.Color("black")
        self.inst_color = pygame.Color("black")

        # Load the "game over" sound effect
        self.game_over_sound = pygame.mixer.Sound('assets/sounds/sfx_die.mp3')
        self.game_over_sound.set_volume(0.5)  # Adjust volume

    def play_game_over_sound(self):
        #play the game over sound
        self.game_over_sound()

    def show_score(self, int_score):
        bird_score = str(int_score)
        score = self.font.render(bird_score, True, self.color)

        # Calculate text size
        text_width, text_height = score.get_size()

        # Center position for the text
        x_pos = (WIDTH - text_width) // 2
        y_pos = 50  # Fixed vertical position

        # Padding for the rectangle
        padding_x = 10
        padding_y = 5

        # Rectangle dimensions
        rect_x = x_pos - padding_x
        rect_y = y_pos - padding_y
        rect_width = text_width + 2 * padding_x
        rect_height = text_height + 2 * padding_y

        # Draw background rectangle
        pygame.draw.rect(self.screen, pygame.Color("white"), (rect_x, rect_y, rect_width, rect_height))
        pygame.draw.rect(self.screen, pygame.Color("black"), (rect_x, rect_y, rect_width, rect_height), 2)

        # Render the score text
        self.screen.blit(score, (x_pos, y_pos))



    def instructions(self):
        inst_text1 = "Press SPACE or CLICK mouse to Jump"
        inst_text2 = "Press \"R\" Button to Restart Game"

        # Render the text
        ins1 = self.inst_font.render(inst_text1, True, self.inst_color)
        ins2 = self.inst_font.render(inst_text2, True, self.inst_color)

        # Calculate text dimensions for centering
        ins1_width = ins1.get_width()
        ins2_width = ins2.get_width()
        ins_height = ins1.get_height() + 10  # Add padding

        # Center positions
        x_center1 = (WIDTH - ins1_width) // 2
        x_center2 = (WIDTH - ins2_width) // 2
        y_start = HEIGHT - 150  # Start near the bottom

        # Draw white background rectangles for readability
        bg_padding = 10
        pygame.draw.rect(self.screen, pygame.Color("white"),
                         (x_center1 - bg_padding, y_start - bg_padding, ins1_width + 2 * bg_padding, ins_height + 10))
        pygame.draw.rect(self.screen, pygame.Color("white"),
                         (x_center2 - bg_padding, y_start + ins_height + bg_padding, ins2_width + 2 * bg_padding, ins_height + 10))

        # Draw text onto the screen
        self.screen.blit(ins1, (x_center1, y_start))
        self.screen.blit(ins2, (x_center2, y_start + ins_height + 20))


    def end_game_sprite(self):
        pygame.display.set_caption("NECC Flappy Bird")
        image = pygame.image.load('assets/misc/GameOver.png')
        image = pygame.transform.scale(image, (350, 100))
        self.screen.blit(image, (120,150))
    def end_game_restart_text(self):
        restart_text = "Press \"R\" To Restart The Game"
        restart = self.inst_font.render(restart_text, True, self.inst_color)

        # Calculate centered position
        text_width, text_height = restart.get_size()
        x_pos = (WIDTH - text_width) // 2
        y_pos = (HEIGHT // 2) + 50

        # Draw background rectangle for better visibility
        pygame.draw.rect(self.screen, pygame.Color("white"), (x_pos - 10, y_pos - 5, text_width + 20, text_height + 10))
        pygame.draw.rect(self.screen, pygame.Color("black"), (x_pos - 10, y_pos - 5, text_width + 20, text_height + 10), 2)

        # Render the text
        self.screen.blit(restart, (x_pos, y_pos))

    def end_game_score_text(self, int_score):
        final_score = "Final Score: " + str(int_score)

        # Determine color based on score
        if int_score <= 5:
            color = pygame.Color(255, 0, 0)  # Red
        elif 5 < int_score < 11:
            color = pygame.Color(255, 215, 0)  # Yellow
        else:
            color = pygame.Color(34, 177, 76)  # Green

        final = self.inst_font.render(final_score, True, color)

        # Calculate centered position
        text_width, text_height = final.get_size()
        x_pos = (WIDTH - text_width) // 2
        y_pos = (HEIGHT // 2) - 50

        # Draw background rectangle for better visibility
        pygame.draw.rect(self.screen, pygame.Color("white"), (x_pos - 10, y_pos - 5, text_width + 20, text_height + 10))
        pygame.draw.rect(self.screen, pygame.Color("black"), (x_pos - 10, y_pos - 5, text_width + 20, text_height + 10), 2)

        # Render the text
        self.screen.blit(final, (x_pos, y_pos))
