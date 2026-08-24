# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# settings.py
from functools import lru_cache
from pathlib import Path
import pygame

WIDTH, HEIGHT = 600, 650
GROUND_SPACE = 50
FPS = 60
SCROLL_SPEED = -6
GRAVITY = 0.5
BIRD_SIZE = (84, 60)
BIRD_JUMP_VELOCITY = -9

# Separated pipe sizes for fairer gameplay.
top_pipe_pair_sizes = [
    (1.5, 6.5),
    (2, 6),
]
middle_pipe_pair_sizes = [
    (3, 5),
    (4, 4),
    (5, 3),
]
bottom_pipe_pair_sizes = [
    (6, 2),
    (6.5, 1.5),
]

PIPE_SIZE = HEIGHT // 9
PIPE_GAP = (PIPE_SIZE * 2) + (PIPE_SIZE // 2)
PIPE_IMAGES = tuple(f"terrain/newerPipe{index}.png" for index in range(5))
TOP_PIPE_IMAGES = ("terrain/newerPipe1.png", "terrain/newerPipe4.png")

_ASSET_DIRECTORY = Path(__file__).resolve().parent / "assets"


def asset_path(relative_path: str) -> Path:
    return _ASSET_DIRECTORY / relative_path


@lru_cache
def load_image(relative_path: str) -> pygame.Surface:
    return pygame.image.load(asset_path(relative_path)).convert_alpha()


@lru_cache
def scaled_image(relative_path: str, size: tuple[int, int], flip_vertical: bool = False) -> pygame.Surface:
    image = pygame.transform.scale(load_image(relative_path), size)
    return pygame.transform.flip(image, False, True) if flip_vertical else image


def import_sprites(relative_directory: str) -> list[pygame.Surface]:
    directory = asset_path(relative_directory)
    images = [
        load_image(image.relative_to(_ASSET_DIRECTORY).as_posix())
        for image in sorted(directory.iterdir())
        if image.is_file() and image.suffix.lower() in {".png", ".jpg", ".jpeg"}
    ]
    if not images:
        raise FileNotFoundError(f"No sprite images found in {directory}")
    return images
