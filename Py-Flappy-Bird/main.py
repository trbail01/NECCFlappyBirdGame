import pygame
import sys
from settings import WIDTH, HEIGHT, ground_space
from world import World

pygame.init()
pygame.mixer.init()  # Initialize the mixer for sound

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT + ground_space))
pygame.display.set_caption("NECC Flappy Bird")

# Load the "game over" sound effect
game_over_sfx = pygame.mixer.Sound('assets/sounds/sfx_die.mp3')
game_over_sfx.set_volume(0.5)  # Adjust the volume if needed

class Main:
    def __init__(self, screen):
        self.screen = screen
        icon = pygame.image.load('assets/misc/favicon.ico')
        pygame.display.set_icon(icon)
        self.bg_img = pygame.image.load('assets/terrain/bg.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT + 2))
        self.ground_img = pygame.image.load('assets/terrain/ground.png')
        self.ground_img = pygame.transform.scale(self.ground_img, (WIDTH, self.ground_img.get_height()))
        self.ground_scroll = 0
        self.scroll_speed = -6
        self.FPS = pygame.time.Clock()
        self.stop_ground_scroll = False

    def main(self):
        world = World(screen)
        sound_played = False  # Flag to ensure the sound is played only once

        while True:
            self.stop_ground_scroll = world.game_over
            self.screen.blit(self.bg_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle key events
                elif event.type == pygame.KEYDOWN:
                    if not world.playing and not world.game_over:
                        # Start the game only when the SPACEBAR is pressed
                        if event.key == pygame.K_SPACE:
                            world.playing = True

                    # Handle SPACEBAR jump during gameplay
                    if event.key == pygame.K_SPACE and world.playing:
                        world.update("jump")

                    # Restart the game if 'R' is pressed
                    if event.key == pygame.K_r:
                        world.update("restart")
                        sound_played = False  # Reset the sound flag when restarting

                # Handle mouse events
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not world.playing and not world.game_over:
                        # Start the game when the mouse button is clicked
                        world.playing = True

                    # Handle jump action on mouse click during gameplay
                    if world.playing:
                        world.update("jump")

            # Play the game over sound once when game over
            if world.game_over and not sound_played:
                game_over_sfx.play()
                sound_played = True

            world.update()
            self.screen.blit(self.ground_img, (self.ground_scroll, HEIGHT))
            if not self.stop_ground_scroll:
                self.ground_scroll += self.scroll_speed
                if abs(self.ground_scroll) > 35:
                    self.ground_scroll = 0

            pygame.display.update()
            self.FPS.tick(60)

if __name__ == "__main__":
    play = Main(screen)
    play.main()
