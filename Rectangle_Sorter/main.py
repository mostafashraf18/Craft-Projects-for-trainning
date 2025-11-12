import pygame
import random
import sorter
import Rectangle



settings = [line.split(": ")[1] for line in open("settings.txt", "r").read().split("\n")[:5]]
amount = int(settings[0])
vspeed = settings[1]
repeat = settings[2]
display_width = int(settings[3])
display_height = int(settings[4])
sorter_box_height = display_height - 100

color(0, 200, 0)