#Imports
import speech_recognition as sr
import pygame
from tkinter import *
from moviepy.editor import *
import time

#Perguntas

ola_q = ['Oi','Olá','saudações']
oque_q = ['o que você é','você é o quê','quem você é','quem é você']
funciona_q = ['como você funciona','você funciona como']
jorge_q = ['Quem é Jorge Amado','Quem foi Jorge Amado','Jorge Amado','Me fale sobre Jorge Amado','fale sobre Jorge Amado','me conte sobre Jorge Amado']
livro_q = ['Me fale sobre o livro','me conte sobre o livro','conte sobre o livro','me conta sobre o livro','conta sobre o livro','fale sobre o livro','fala sobre o livro','defina o livro','livro']

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
        w = 750
        h = 550
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
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
        # ____Olá____#
        if (receave in ola_q):
            pygame.mixer.music.load('greatings.mp3')
            pygame.mixer.music.play()
        #____O que você é____#
        elif (receave in oque_q):
            pygame.mixer.music.load('sobre.mp3')
            pygame.mixer.music.play()
        # ____Como você funciona____#
        elif (receave in funciona_q):
            pygame.mixer.music.load('funcionamento.mp3')
            pygame.mixer.music.play()
        # ____Jorge Amado____#
        elif (receave in jorge_q):
            self.GoJorge()
        # ____Livro____#
        elif (receave in livro_q):
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
        w = 480
        h = 628
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.master.resizable(0,0)
        self.photo2 = PhotoImage(file='jorgeamado.png')
        self.label = Label(self.master, image=self.photo2, bg='black').grid(row=0,column=0)
        self.master.after(500, self.AudioJorge)
        self.master.mainloop()

    def AudioJorge(self):
        pygame.mixer.music.load('jorgeamado.mp3')
        pygame.mixer.music.play()
        time.sleep(48)
        self.CloseJorge()


    def CloseJorge(self):
        self.master.destroy()


#Janela do livro
class Book:
    def __init__(self,master):
        self.master = master
        self.master.title("Capitães da Areia")
        self.master.resizable(0, 0)
        w = 333
        h = 500
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo3 = PhotoImage(file='livro.png')
        self.label = Label(self.master, image=self.photo3, bg='black').grid(column=0,row=0)
        self.master.after(500, self.AudioBook)
        self.master.mainloop()

    def AudioBook(self):
        pygame.mixer.music.load('livro.mp3')
        pygame.mixer.music.play()
        time.sleep(31)
        self.CloseBook()

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

