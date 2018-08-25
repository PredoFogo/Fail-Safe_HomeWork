#Imports
import speech_recognition as sr
import pygame
from tkinter import *
from moviepy.editor import *
import time

#Inicializar Pygame
pygame.init()
pygame.mixer.init()

#Variaveis para chamar a interface
r = sr.Recognizer()
enter = False

#Janela Principal
class FailSafe_Main:
    def __init__(self,master):
        self.master = master
        self.master.title("Fail-Safe")
        self.master.resizable(0,0)
        self.master.configure(background='black')
        photo1 = PhotoImage(file='failsafe.png')
        Label(self.master, image=photo1, bg='black').grid(row=0,column=0)
        Button(self.master, text='Clique e fale',width=50,command=self.receaver,font=24) .grid(row=1, column=0)
        Button(self.master, text='Sair', width=50, command=self.Destoy_Main).grid(row=2, column=0)
        self.master.mainloop()

    #Def Receaver, função que recebe os comandos de voz com suas respectivas ações
    def receaver(self):
        with sr.Microphone() as m:
            l = r.listen(m)
            r.adjust_for_ambient_noise(m)

        receave = r.recognize_google(l, language='pt')
        print(receave)
        #____Olá____#
        if (receave == 'Olá'):
            pygame.mixer.music.load('ola.mp3')
            pygame.mixer.music.play()
        elif (receave == 'Oi'):
            pygame.mixer.music.load('ola.mp3')
            pygame.mixer.music.play()
        elif (receave == 'saudações'):
            pygame.mixer.music.load('ola.mp3')
            pygame.mixer.music.play()
        #____O que você é____#
        elif (receave == 'o que você é'):
            pygame.mixer.music.load('sobre.mp3')
            pygame.mixer.music.play()
        elif (receave == 'você é o quê'):
            pygame.mixer.music.load('sobre.mp3')
            pygame.mixer.music.play()
        elif (receave == 'quem você é'):
            pygame.mixer.music.load('sobre.mp3')
            pygame.mixer.music.play()
        # ____Como você funciona____#
        elif (receave == 'como você funciona'):
            pygame.mixer.music.load('funcionamento.mp3')
            pygame.mixer.music.play()
        elif (receave == 'você funciona como'):
            pygame.mixer.music.load('funcionamento.mp3')
            pygame.mixer.music.play()
        # ____Jorge Amado____#
        elif (receave == 'Quem é Jorge Amado'):
            self.GoJorge()
        elif (receave == 'Quem foi Jorge Amado'):
            self.GoJorge()
        elif (receave == 'Jorge Amado'):
            self.GoJorge()
        # ____Livro____#
        elif (receave == 'Me fale sobre o livro'):
            self.GoBook()
        elif (receave == 'me conte sobre o livro'):
            self.GoBook()
        elif (receave == 'conte sobre o livro'):
            self.GoBook()
        elif (receave == 'me conta sobre o livro'):
            self.GoBook()
        elif (receave == 'conta sobre o livro'):
            self.GoBook()
        elif (receave == 'fale sobre o livro'):
            self.GoBook()
        elif (receave == 'fala sobre o livro'):
            self.GoBook()
        elif (receave == 'defina o livro'):
            self.GoBook()
        elif (receave == 'livro'):
            self.GoBook()
        # ____Easter Eggs____#
        elif (receave == 'geração coca-cola'):
            self.GeracaoCocaCola()

    #Chama a tela do jorge amado
    def GoJorge(self):
        root2 = Toplevel(self.master)
        jorge = JorgeAmado(root2)

    #Chama janela do livro
    def GoBook(self):
        root3 = Toplevel(self.master)
        book = Book(root3)

    #Fecha a janela principal
    def Destoy_Main(self):
        self.master.destroy()

    #EasterEGG #1
    def GeracaoCocaCola(self):
        clip = VideoFileClip('eg1.mp4')
        clip.preview()
        pygame.quit()
        self.master.mainloop()

#############################################################################################################

#Janela Jorge Amado
class JorgeAmado:
    def __init__(self, master):
        self.master = master
        self.master.title("Jorge Amado")
        self.master.resizable(0,0)
        self.photo2 = PhotoImage(file='jorgeamado.png')
        self.label = Label(self.master, image=self.photo2, bg='black').grid(row=0,column=0)

        #Opção para evitar o mainloop e chamar algumas coisas depois da execução
        self.master.update_idletasks()
        self.master.update()

        self.AudioJorge()

    def AudioJorge(self):
        pygame.mixer.music.load('jorgeamado.mp3')
        pygame.mixer.music.play()
        time.sleep(49)
        self.CloseJorge()

    def CloseJorge(self):
        self.master.destroy()


#Janela do livro
class Book:
    def __init__(self,master):
        self.master = master
        self.master.title("Capitães da Areia")
        self.master.resizable(0,0)
        self.photo3 = PhotoImage(file='livro.png')
        self.label = Label(self.master, image=self.photo3, bg='black').grid(column=0,row=0)
        self.AudioBook()
        self.master.update_idletasks()
        self.master.update()

    def AudioBook(self):
        pygame.mixer.music.load('livro.mp3')
        pygame.mixer.music.play()
        time.sleep(31)

    def CloseBook(self):
        self.master.destroy()

#############################################################################################################

#Def que chama a janela principal
def main():
    root = Tk()
    failsafemain = FailSafe_Main(root)
    root.mainloop()

#Loop do Call da interface
while (enter!=True):
    with sr.Microphone() as m:
        l = r.listen(m)
        r.adjust_for_ambient_noise(m)

    receave = r.recognize_google(l)
    print(receave)
    if(receave=='Fail-Safe'):
        a = True
        main()
    else:
        print("ALGO DEU ERRADO! REPITA A FRASE")

