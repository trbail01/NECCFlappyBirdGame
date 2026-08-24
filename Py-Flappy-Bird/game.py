# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# game.py
import pygame
from settings import HEIGHT, WIDTH, scaled_image

pygame.font.init()


class GameIndicator:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Bauhaus 93', 60)
        self.inst_font = pygame.font.SysFont('Bauhaus 93', 30)
        self.color = pygame.Color("black")
        self.inst_color = pygame.Color("black")
        self.game_over_image = scaled_image("misc/GameOver.png", (350, 100))

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
        instructions = (
            "Press SPACE or CLICK mouse to Jump",
            'Press "R" Button to Restart Game',
            "Press ESC to Exit Game",
        )
        y_start = HEIGHT - 195
        padding = 10

        for index, instruction in enumerate(instructions):
            text = self.inst_font.render(instruction, True, self.inst_color)
            x_pos = (WIDTH - text.get_width()) // 2
            y_pos = y_start + index * (text.get_height() + 20)
            pygame.draw.rect(
                self.screen,
                pygame.Color("white"),
                (
                    x_pos - padding,
                    y_pos - padding,
                    text.get_width() + 2 * padding,
                    text.get_height() + 2 * padding,
                ),
            )
            self.screen.blit(text, (x_pos, y_pos))


    def end_game_sprite(self):
        self.screen.blit(self.game_over_image, (120, 150))

    def end_game_restart_text(self):
        restart_text = 'Press "R" To Restart or ESC To Exit'
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
