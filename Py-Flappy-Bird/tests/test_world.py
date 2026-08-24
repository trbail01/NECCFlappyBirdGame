import os
from pathlib import Path
import sys
import unittest

os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pygame

from settings import BIRD_SIZE, HEIGHT
from world import World


class WorldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.mixer.init()
        cls.screen = pygame.display.set_mode((600, HEIGHT + 50))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_bird_frames_stay_scaled_and_crash_sprite_is_preserved(self):
        world = World(self.screen)
        bird = world.player.sprite

        self.assertTrue(all(frame.get_size() == BIRD_SIZE for frame in bird.frames))

        bird.show_crash_sprite()
        bird.update(False)

        self.assertEqual(bird.image, bird.crash_img)

    def test_pipe_pair_scores_only_once(self):
        world = World(self.screen)
        bird = world.player.sprite
        world.playing = True
        world.current_pipe.rect.centerx = bird.rect.left

        world._handle_collisions()
        world._handle_collisions()

        self.assertEqual(bird.score, 1)

    def test_restart_creates_a_clean_world(self):
        world = World(self.screen)
        world.game_over = True

        world.update("restart")

        self.assertFalse(world.game_over)
        self.assertFalse(world.playing)
        self.assertEqual(world.player.sprite.score, 0)
        self.assertEqual(len(world.pipes), 2)


if __name__ == "__main__":
    unittest.main()
