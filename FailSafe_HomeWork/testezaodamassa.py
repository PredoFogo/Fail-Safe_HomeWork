from tkinter import *
import pygame
from moviepy.editor import *


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('greatings.mp3')
pygame.mixer.music.play()


class a:
    def __init__(self):
        clip1 = VideoFileClip('eg2.mp4')
        clip1.preview()
        clip1.reader.close()
        del clip1.reader
        del clip1
        self.vid2()
    def vid2(self):
        pygame.mixer.music.load('releitura2.mp3')
        pygame.mixer.music.play()

