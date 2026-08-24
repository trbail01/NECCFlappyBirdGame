import random

import pygame

from bird import Bird
from game import GameIndicator
from pipe import Pipe
from settings import (
    BIRD_SIZE,
    GRAVITY,
    HEIGHT,
    PIPE_GAP,
    PIPE_IMAGES,
    PIPE_SIZE,
    SCROLL_SPEED,
    WIDTH,
    asset_path,
    bottom_pipe_pair_sizes,
    middle_pipe_pair_sizes,
    top_pipe_pair_sizes,
)


class World:
    def __init__(self, screen):
        self.screen = screen
        self.world_shift = 0
        self.gravity = GRAVITY
        self.current_pipe = None
        self.pipes = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.playing = False
        self.game_over = False
        self.score = 0
        self.score_point_sound = pygame.mixer.Sound(asset_path("sounds/sfx_point.mp3"))
        self.score_point_sound.set_volume(0.5)
        self.pipe_options = [
            self._add_top_pipe,
            self._add_middle_pipe,
            self._add_bottom_pipe,
        ]
        self.game = GameIndicator(screen)
        self._generate_world()

    def _add_pipe(self):
        if self.score == 0:
            self._generate_pipe(middle_pipe_pair_sizes)
            self.pipe_options = [
                self._add_top_pipe,
                self._add_middle_pipe,
                self._add_bottom_pipe,
            ]
            return

        pipe_choice = random.choice(self.pipe_options)
        pipe_choice()

        if pipe_choice == self._add_top_pipe:
            self.pipe_options = [self._add_top_pipe, self._add_middle_pipe]
        elif pipe_choice == self._add_middle_pipe:
            self.pipe_options = [
                self._add_top_pipe,
                self._add_middle_pipe,
                self._add_bottom_pipe,
            ]
        else:
            self.pipe_options = [self._add_middle_pipe, self._add_bottom_pipe]

    def _generate_pipe(self, pair_sizes):
        top_units, bottom_units = random.choice(pair_sizes)
        top_pipe_height = top_units * PIPE_SIZE
        bottom_pipe_height = bottom_units * PIPE_SIZE
        image_path = random.choice(PIPE_IMAGES)
        pipe_top = Pipe(
            (WIDTH, -(bottom_pipe_height + PIPE_GAP)),
            PIPE_SIZE,
            HEIGHT,
            True,
            image_path,
        )
        pipe_bottom = Pipe(
            (WIDTH, top_pipe_height + PIPE_GAP),
            PIPE_SIZE,
            HEIGHT,
            False,
            image_path,
        )
        self.pipes.add(pipe_top, pipe_bottom)
        self.current_pipe = pipe_top

    def _add_top_pipe(self):
        self._generate_pipe(top_pipe_pair_sizes)

    def _add_middle_pipe(self):
        self._generate_pipe(middle_pipe_pair_sizes)

    def _add_bottom_pipe(self):
        self._generate_pipe(bottom_pipe_pair_sizes)

    def _generate_world(self):
        self._add_pipe()
        bird = Bird((WIDTH // 2 - PIPE_SIZE, HEIGHT // 2 - PIPE_SIZE), BIRD_SIZE)
        self.player.add(bird)

    def _scroll_x(self):
        self.world_shift = SCROLL_SPEED if self.playing else 0

    def _apply_gravity(self, player):
        if self.playing or self.game_over:
            player.direction.y += self.gravity
            player.rect.y += player.direction.y

    def _handle_collisions(self):
        bird = self.player.sprite
        collided_with_pipe = pygame.sprite.spritecollide(
            bird, self.pipes, False, pygame.sprite.collide_mask
        )
        if collided_with_pipe or bird.rect.bottom >= HEIGHT or bird.rect.top <= 0:
            self.playing = False
            self.game_over = True
            bird.show_crash_sprite()
            return

        if not self.current_pipe.scored and bird.rect.left >= self.current_pipe.rect.centerx:
            self.current_pipe.scored = True
            bird.score += 1
            self.score_point_sound.play()
            self.score = bird.score

    def _restart(self):
        self.pipes.empty()
        self.player.empty()
        self.current_pipe = None
        self.score = 0
        self.playing = False
        self.game_over = False
        self._generate_world()

    def update(self, player_event=None):
        if player_event == "restart":
            self._restart()
            player_event = None

        self._scroll_x()
        self.pipes.update(self.world_shift)
        self._apply_gravity(self.player.sprite)

        if self.playing:
            self._handle_collisions()
            if self.playing and self.current_pipe.rect.centerx <= (WIDTH // 2) - PIPE_SIZE:
                self._add_pipe()

        is_jump = player_event == "jump" and self.playing and not self.game_over

        if not self.playing and not self.game_over:
            self.game.instructions()
        if self.game_over:
            self.game.end_game_sprite()
            self.game.end_game_restart_text()
            self.game.end_game_score_text(self.score)

        self.pipes.draw(self.screen)
        self.player.update(is_jump)
        self.player.draw(self.screen)
        self.game.show_score(self.player.sprite.score)
