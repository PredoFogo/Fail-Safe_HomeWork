'''
Fail-Safe BY:Pedro Lucas Miguel
A utilização deste código fonte esta aberta a todos, também estão liberadas cópias de código.
'''

#Imports
import speech_recognition as sr
import pygame
from tkinter import *
from moviepy.editor import *
import time

#Perguntas

teste_q = ['teste']
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
        # ____Teste____#
        elif (receave in teste_q):
            self.StartR()
        # ____Easter Eggs____#
        elif (receave == 'geração coca-cola'):
            self.GeracaoCocaCola()
        # ____Easter Eggs 2____#
        elif (receave == 'e o gole'):
            self.EoGole()

    #Chama a tela do jorge amado
    def GoJorge(self):
        root2 = Toplevel(self.master)
        jorge = JorgeAmado(root2)

    #Chama janela do livro
    def GoBook(self):
        root3 = Toplevel(self.master)
        book = Book(root3)

    # Chama janelas dos personagens
    def StartR(self):
        self.GoPB()

    # Pedro Bala
    def GoPB(self):
        root11 = Toplevel(self.master)
        pb = PedroBala(root11)

    #Fecha a janela principal
    def Destoy_Main(self):
        self.master.destroy()

    #EasterEGG #1
    def GeracaoCocaCola(self):
        clip = VideoFileClip('eg1.mp4')
        clip.preview()
        pygame.quit()
        self.master.mainloop()

    #EasterEGG #2
    def EoGole(self):
        clip = VideoFileClip('eg2.mp4')
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
class BoaVida:
    def __init__(self,master):
        self.master = master
        self.master.title('Boa Vida')
        self.master.resizable(0, 0)
        w = 493
        h = 608
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo4 = PhotoImage(file='Boa Vida.png')
        self.label = Label(self.master, image=self.photo4, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoPI)
        self.master.mainloop()

    # Pirulito
    def GoPI(self):
        root12 = Toplevel(self.master)
        pi = Pirulito(root12)

class Daninha:
    def __init__(self,master):
        self.master = master
        self.master.title('D`Aninha')
        self.master.resizable(0, 0)
        w = 576
        h = 723
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo5 = PhotoImage(file='d aninha.png')
        self.label = Label(self.master, image=self.photo5, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoPJP)
        self.master.mainloop()

    # Padre Jose Pedro
    def GoPJP(self):
        root10 = Toplevel(self.master)
        pjp = Padre(root10)

class Dalva:
    def __init__(self,master):
        self.master = master
        self.master.title('Dalva')
        self.master.resizable(0, 0)
        w = 373
        h = 644
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo6 = PhotoImage(file='Dalva.png')
        self.label = Label(self.master, image=self.photo6, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoDA)
        self.master.mainloop()

    # D'Aninha
    def GoDA(self):
        root5 = Toplevel(self.master)
        da = Daninha(root5)

class Dora:
    def __init__(self,master):
        self.master = master
        self.master.title('Dora')
        self.master.resizable(0, 0)
        w = 851
        h = 675
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo7 = PhotoImage(file='Dora.png')
        self.label = Label(self.master, image=self.photo7, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoBV)
        self.master.mainloop()

    # Boa Vida
    def GoBV(self):
        root4 = Toplevel(self.master)
        bv = BoaVida(root4)

class Gato:
    def __init__(self,master):
        self.master = master
        self.master.title('Gato')
        self.master.resizable(0, 0)
        w = 442
        h = 709
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo8 = PhotoImage(file='Gato.png')
        self.label = Label(self.master, image=self.photo8, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoDO)
        self.master.mainloop()

    # Dora
    def GoDO(self):
        root7 = Toplevel(self.master)
        do = Dora(root7)

class JoaoGrande:
    def __init__(self,master):
        self.master = master
        self.master.title('João Grande')
        self.master.resizable(0, 0)
        w = 483
        h = 654
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo9 = PhotoImage(file='Joao Grande.png')
        self.label = Label(self.master, image=self.photo9, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoGA)
        self.master.mainloop()

    # Gato
    def GoGA(self):
        root8 = Toplevel(self.master)
        ga = Gato(root8)

class Padre:
    def __init__(self,master):
        self.master = master
        self.master.title('Padre José Pedro')
        self.master.resizable(0, 0)
        w = 666
        h = 714
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo10 = PhotoImage(file='Padre Jose Pedro.png')
        self.label = Label(self.master, image=self.photo10, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoQDD)
        self.master.mainloop()

    # Querido de Deus
    def GoQDD(self):
        root14 = Toplevel(self.master)
        qdd = QueridoDeDeus(root14)

class PedroBala:
    def __init__(self,master):
        self.master = master
        self.master.title('PedroBala')
        self.master.resizable(0, 0)
        w = 729
        h = 723
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo11 = PhotoImage(file='Pedro Bala.png')
        self.label = Label(self.master, image=self.photo11, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoPR)
        self.master.mainloop()

    # Professor
    def GoPR(self):
        root13 = Toplevel(self.master)
        pr = Professor(root13)

class Pirulito:
    def __init__(self,master):
        self.master = master
        self.master.title('Pirulito')
        self.master.resizable(0, 0)
        w = 1004
        h = 781
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo12 = PhotoImage(file='Pirulito.png')
        self.label = Label(self.master, image=self.photo12, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoVS)
        self.master.mainloop()

    # Volta Seca
    def GoVS(self):
        root16 = Toplevel(self.master)
        vs = VoltaSeca(root16)

class Professor:
    def __init__(self,master):
        self.master = master
        self.master.title('Professor')
        self.master.resizable(0, 0)
        w = 529
        h = 788
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo13 = PhotoImage(file='Professor.png')
        self.label = Label(self.master, image=self.photo13, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoSP)
        self.master.mainloop()

    # Sem Pernas
    def GoSP(self):
        root15 = Toplevel(self.master)
        sp = SemPerna(root15)

class QueridoDeDeus:
    def __init__(self,master):
        self.master = master
        self.master.title('Querido de Deus')
        self.master.resizable(0, 0)
        w = 393
        h = 717
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo14 = PhotoImage(file='Querido de deus.png')
        self.label = Label(self.master, image=self.photo14, bg='black').grid(row=0,column=0)
        self.master.mainloop()

class SemPerna:
    def __init__(self,master):
        self.master = master
        self.master.title('Sem Perna')
        self.master.resizable(0, 0)
        w = 748
        h = 772
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo15 = PhotoImage(file='Sem Perna.png')
        self.label = Label(self.master, image=self.photo15, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoJG)
        self.master.mainloop()

    # João Grande
    def GoJG(self):
        root9 = Toplevel(self.master)
        jg = JoaoGrande(root9)

class VoltaSeca:
    def __init__(self,master):
        self.master = master
        self.master.title('Volta Seca')
        self.master.resizable(0, 0)
        w = 983
        h = 653
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.photo16 = PhotoImage(file='Volta Seca.png')
        self.label = Label(self.master, image=self.photo16, bg='black').grid(row=0,column=0)
        self.master.after(2000, self.GoDV)
        self.master.mainloop()

    # Dalva
    def GoDV(self):
        root6 = Toplevel(self.master)
        dv = Dalva(root6)

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

