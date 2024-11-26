# Hello Java and Advanced C# Students at NECC. Please feel free to make any changes you would like
# Please post any desired changes to the main branch and I will review them. Happy Coding!!!
# settings.py
from os import walk
from tarfile import fully_trusted_filter

import pygame

WIDTH, HEIGHT = 600, 650
#Seperated pipe sizes for less randomness for game fairness.
top_pipe_pair_sizes = [
    (1.5,6.5),
    (2,6),

]
middle_pipe_pair_sizes = [
    (3,5),
    (4, 4),
    (5, 3),
]
bottom_pipe_pair_sizes = [
    (6, 2),
    (6.5, 1.5)
]


pipe_size = HEIGHT // 9 #was 10
pipe_gap = (pipe_size * 2) + (pipe_size // 2);
ground_space = 50

def import_sprite(path):
    surface_list = []
    for _, _, img_file in walk(path):
        for image in img_file:
            full_path = f"{path}/{image}"
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    return surface_list

