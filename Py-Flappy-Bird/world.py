# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!

# world.py
import pygame
from pipe import Pipe
from bird import Bird
from game import GameIndicator
from settings import WIDTH, HEIGHT, pipe_size, pipe_gap, top_pipe_pair_sizes, middle_pipe_pair_sizes, bottom_pipe_pair_sizes
import random

class World:
    def __init__(self, screen):
        self.screen = screen
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.5 #was .5
        self.current_pipe = None
        self.pipes = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.playing = False
        self.game_over = False
        self.passed = True
        self.game = GameIndicator(screen)
        self.score = 0
        self.pipe_options = [
            self._add_top_pipe,
            self._add_middle_pipe,
            self._add_bottom_pipe
        ]
        self.game = GameIndicator(screen)
        self._generate_world()
    # adds pipe once the last pipe added reached the desired pipe horizontal spaces
    def _add_pipe(self):
        if self.score == 0:
            # Middle pipe is spawned first
            self._generate_pipe(middle_pipe_pair_sizes)
            # Update pipe options for random selection
            self.pipe_options = [
                self._add_top_pipe,
                self._add_middle_pipe,
                self._add_bottom_pipe
            ]
        else:
            # Choose a random pipe-generating method and call it
            pipe_choice = random.choice(self.pipe_options)
            pipe_choice()

            # Dynamically adjust the pipe options based on the chosen pipe
            if pipe_choice == self._add_top_pipe:
                self.pipe_options = [
                    self._add_top_pipe,
                    self._add_middle_pipe
                ]
            elif pipe_choice == self._add_middle_pipe:
                self.pipe_options = [
                    self._add_top_pipe,
                    self._add_middle_pipe,
                    self._add_bottom_pipe
                ]
            elif pipe_choice == self._add_bottom_pipe:
                self.pipe_options = [
                    self._add_middle_pipe,
                    self._add_bottom_pipe
                ]

    def _generate_pipe(self, pair_sizes):
        pipe_pair_size = random.choice(pair_sizes)
        top_pipe_height, bottom_pipe_height = pipe_pair_size[0] * pipe_size, pipe_pair_size[1] * pipe_size
        pipe_top = Pipe((WIDTH, 0 - (bottom_pipe_height + pipe_gap)), pipe_size, HEIGHT, True)
        pipe_bottom = Pipe((WIDTH, top_pipe_height + pipe_gap), pipe_size, HEIGHT, False)
        self.pipes.add(pipe_top, pipe_bottom)
        self.current_pipe = pipe_top


    def _add_top_pipe(self):
        self._generate_pipe(top_pipe_pair_sizes)

    def _add_middle_pipe(self):
        self._generate_pipe(middle_pipe_pair_sizes)

    def _add_bottom_pipe(self):
        self._generate_pipe(bottom_pipe_pair_sizes)

    # creates the player and the obstacle
    def _generate_world(self):
        self._add_pipe()
        bird = Bird((WIDTH//2 - pipe_size, HEIGHT//2 - pipe_size), 30)
        self.player.add(bird)

    #for moving background/obstacle
    def _scroll_x(self):
        if self.playing:
            self.world_shift = -6
        else:
            self.world_shift = 0

    # add gravity to bird for falling
    def _apply_gravity(self, player):
        if self.playing or self.game_over:
            player.direction.y += self.gravity
            player.rect.y += player.direction.y

    # handles scoring and collision
    def _handle_collisions(self):
        bird = self.player.sprite
        # for collision checking
        if pygame.sprite.groupcollide(self.player, self.pipes, False, False) or bird.rect.bottom >= HEIGHT or bird.rect.top <= 0:
            self.playing = False
            self.game_over = True

            # Switch to crash sprite of bird
            bird.show_crash_sprite()

            # img_path = 'assets/misc/GameOver.png'
            # self.image = pygame.image.load(img_path)
            # print("Game over!")
        else:
            # if player pass through the pipe gaps
            bird = self.player.sprite
            self.score_point_sound = pygame.mixer.Sound("assets/sounds/sfx_point.mp3") # load sfx asset
            if bird.rect.x >= self.current_pipe.rect.centerx:
                bird.score += 1
                self.score_point_sound.play()
                self.score = bird.score
                self.passed = True

# updates the bird's overall state
    def update(self, player_event=None):
        # Add a new pipe when needed
        if self.current_pipe.rect.centerx <= (WIDTH // 2) - pipe_size:
            self._add_pipe()

        # Update and draw pipes
        self.pipes.update(self.world_shift)
        self.pipes.draw(self.screen)

        # Apply physics
        self._apply_gravity(self.player.sprite)
        self._scroll_x()
        self._handle_collisions()

        # Handle player events
        if player_event == "jump" and not self.game_over:
            player_event = True
        elif player_event == "restart":
            self.game_over = False
            self.pipes.empty()
            self.player.empty()
            self.player.score = 0
            self.score = 0
            self._generate_world()
        else:
            player_event = False

        # Display instructions if not playing
        if not self.playing and not self.game_over:
            bird = self.player.sprite
            self.game.instructions()
        if self.game_over:
            self.game.end_game_sprite()
            self.game.end_game_restart_text()
            self.game.end_game_score_text(self.score)


        # Update and draw player
        self.player.update(player_event)
        self.player.draw(self.screen)

        # Show score
        self.game.show_score(self.player.sprite.score)

