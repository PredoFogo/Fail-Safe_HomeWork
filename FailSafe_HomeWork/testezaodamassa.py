from tkinter import *
import pygame
from moviepy.editor import *
import time

class a:
    def __init__(self):
        clip = VideoFileClip('eg2.mp4')
        clip.preview()
        clip.reader.close()
        clip.audio.reader.close_proc()
        time.sleep(3)
        clip1 = VideoFileClip('eg2.mp4')
        clip1.preview()
        clip1.reader.close()
        clip1.audio.reader.close_proc()





a()
