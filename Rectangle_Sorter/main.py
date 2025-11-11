import pygame
import random
import sorter
import Rectangle




settings = [line.split(": ")[1] for line in open("settings.txt", "r").read().split("\n")[:5]]
amount = int(settings[0])

