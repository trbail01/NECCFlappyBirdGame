import pygame
from settings import FPS, GROUND_SPACE, HEIGHT, SCROLL_SPEED, WIDTH, asset_path
from world import World


class Main:
    def __init__(self, screen):
        self.screen = screen
        icon = pygame.image.load(asset_path("misc/favicon.ico"))
        pygame.display.set_icon(icon)
        self.bg_img = pygame.image.load(asset_path("terrain/bg.png")).convert_alpha()
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT + 2))
        self.ground_img = pygame.image.load(asset_path("terrain/ground.png")).convert_alpha()
        self.ground_img = pygame.transform.scale(self.ground_img, (WIDTH, self.ground_img.get_height()))
        self.ground_scroll = 0
        self.clock = pygame.time.Clock()
        self.game_over_sfx = pygame.mixer.Sound(asset_path("sounds/sfx_die.mp3"))
        self.game_over_sfx.set_volume(0.5)

    def main(self):
        world = World(self.screen)
        sound_played = False

        while True:
            player_event = None
            self.screen.blit(self.bg_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

                    if not world.playing and not world.game_over:
                        if event.key == pygame.K_SPACE:
                            world.playing = True

                    if event.key == pygame.K_SPACE and world.playing:
                        player_event = "jump"

                    if event.key == pygame.K_r:
                        player_event = "restart"
                        sound_played = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not world.playing and not world.game_over:
                        world.playing = True

                    if world.playing:
                        player_event = "jump"

            if world.game_over and not sound_played:
                self.game_over_sfx.play()
                sound_played = True

            world.update(player_event)
            self.screen.blit(self.ground_img, (self.ground_scroll, HEIGHT))
            if not world.game_over:
                self.ground_scroll += SCROLL_SPEED
                if abs(self.ground_scroll) > 35:
                    self.ground_scroll = 0

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + GROUND_SPACE))
    pygame.display.set_caption("NECC Flappy Bird")
    Main(screen).main()
    pygame.quit()
