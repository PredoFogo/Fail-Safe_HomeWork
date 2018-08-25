from moviepy.editor import *
import pygame

pygame.display.set_caption('Hello World!')

clip = VideoFileClip('yo.mp4')
clip.preview()

pygame.quit()