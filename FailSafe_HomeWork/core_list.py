'''
Fail-Safe BY:Pedro Lucas Miguel
A utilização deste código fonte esta aberta a todos, também estão liberadas cópias de código.
'''

#Imports
import speech_recognition as sr
import pygame
from tkinter import *
from moviepy.editor import *
import webbrowser

#Perguntas

ola_q = ['Oi','Olá','saudações']
oque_q = ['o que você é','você é o quê','quem você é','quem é você']
funciona_q = ['como você funciona','você funciona como']
jorge_q = ['Quem é Jorge Amado','Quem foi Jorge Amado','Jorge Amado','Me fale sobre Jorge Amado','fale sobre Jorge Amado','me conte sobre Jorge Amado']
livro_q = ['Me fale sobre o livro','me conte sobre o livro','conte sobre o livro','me conta sobre o livro','conta sobre o livro','fale sobre o livro','fala sobre o livro','defina o livro','livro']
contexto_q = ['Me fale sobre o contexto histórico','fale sobre o contexto histórico','Qual é o contexto histórico','contexto histórico','Como é o contexto histórico']
codigo_q = ['me mostre o seu código-fonte','me mostre como você é feita','Como é seu código-fonte','código fonte','me mostre como você é prgramada','me mostre seu código-fonte']
releitura_q = ['teste','faça uma releitura do livro','faça a releitura do livro','releitura','Conte a releitura do livro','me conte a releitura do livrro','me faça uma releitura do livro']
tempo_q = ['Como é o tempo do livro','Qual o tempo do livro','Como é o tempo cronoóligoc do livro','Qual é o tempor cronológico do livro']
narrador_q = ['como o livro é narrado','Que tipo de narrador o livro tem','Qual é o tipo de narrador','o livro narrado como','como livrar narrado']
obrigado_q = ['obrigado','Muito obrigado','agradeço']
pedro_bala_q = ['Pedro Bala','Quem é Pedro Bala','Quem foi Pedro Bala']
professor_q = ['professor','quem é professor','quem foi professor','quem é o professor','Quem foi o professor']
sem_perna_q = ['sem perna','sem pernas','quem é o sem perna','quem é o sem pernas','Quem foi o sem pernas','Quem foi o sem perna','quem é sem pernas','quem é sem perna','Quem foi sem pernas','Quem foi sem perna']
joao_grande_q = ['João Grande','Quem é João Grande','Quem foi João Grande','Quem é o João Grande','Quem foi o João Grande']
gato_q = ['gato','quem é gato','Quem foi o gato','Quem foi gato','quem é o gato']
dora_q = ['Dora','Quem é Dora','Quem foi Dora','quem é a Dora','Quem foi a Dora']
pirulito_q = ['pirulito','quem é pirulito','Quem foi pirulito','quem é o pirulito','Quem foi o pirulito']
boa_vida_q = ['boa vida','quem é boa vida','Quem foi boa vida','quem é o Boa Vida','Quem foi o Boa Vida']
volta_seca_q = ['volta seca','quem é volta seca','Quem foi volta seca','quem é o volta seca','Quem foi o volta seca']
dalva_q = ['Dalva','quem é Dalva','Quem foi Dalva','quem é a Dalva','Quem foi a Dalva']
aninha_q = ['Aninha','quem é Aninha','Quem foi Aninha','quem é Aninha','Quem foi a Aninha']
padre_q = ['Padre José Pedro','Padre','quem é o padre','quem é Padre','Quem foi Padre','Quem foi o padre José Pedro','quem é o padre José Pedro','quem é Padre José Pedro','Quem foi Padre José Pedro','Quem foi o padre José Pedro']
querido_q = ['querido de Deus','querido','quem é querido','Quem foi querido','quem é o querido','Quem foi ou querido','quem é querido de Deus','Quem foi querido de Deus','quem é o querido de Deus','Quem foi ou querido de Deus']

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
        # ____Contexto histórico____#
        elif (receave in contexto_q):
            pygame.mixer.music.load('contexto.mp3')
            pygame.mixer.music.play()
        # ____Código fonte____#
        elif (receave in codigo_q):
            pygame.mixer.music.load('codigo.mp3')
            new = 2
            url = 'https://github.com/PredoFogo/Fail-Safe_HomeWork/blob/master/FailSafe_HomeWork/core_list.py'
            webbrowser.open(url,new=new)
            pygame.mixer.music.play()
        # ____Releitura____#
        elif (receave in releitura_q):
            pygame.mixer.music.load('releitura1.mp3')
            pygame.mixer.music.play()
            self.master.after(27000, self.GoPB)
        # ____Obrigado____#
        elif (receave in obrigado_q):
            pygame.mixer.music.load('obrigado.mp3')
            pygame.mixer.music.play()
            self.master.after(24000, self.Destoy_Main)
        # ____Jorge Amado____#
        elif (receave in jorge_q):
            self.GoJorge()
        # ____Livro____#
        elif (receave in livro_q):
            self.GoBook()
        # ____Tempor cronológico____#
        elif (receave in tempo_q):
            pygame.mixer.music.load('Tempo.mp3')
            pygame.mixer.music.play()
        # ____Narrador____#
        elif (receave in narrador_q):
            pygame.mixer.music.load('Narrador.mp3')
            pygame.mixer.music.play()
        # ____Pedro Bala Q____#
        elif (receave in pedro_bala_q):
            self.GoPB2()
        # ____Professor Q____#
        elif (receave in professor_q):
            self.GoPR2()
        # ____Sem Pernas Q____#
        elif (receave in sem_perna_q):
            self.GoSP2()
        # ____João Grande Q____#
        elif (receave in joao_grande_q):
            self.GoJG2()
        # ____Gato Q____#
        elif (receave in gato_q):
            self.GoGA2()
        # ____Dora Q____#
        elif (receave in dora_q):
            self.GoDO2()
        # ____Pirulito Q____#
        elif (receave in pirulito_q):
            self.GoPI2()
        # ____Boa Vida Q____#
        elif (receave in boa_vida_q):
            self.GoBV2()
        # ____Volta Seca Q____#
        elif (receave in volta_seca_q):
            self.GoVS2()
        # ____Dalva Q____#
        elif (receave in dalva_q):
            self.GoDV2()
        # ____D'Aninha Q____#
        elif (receave in aninha_q):
            self.GoDA2()
        # ____Padre José Pedro Q____#
        elif (receave in padre_q):
            self.GoPJP2()
        # ____Querido de Deus Q____#
        elif (receave in querido_q):
            self.GoQDD2()
        # ____Easter Eggs____#
        elif (receave == 'geração coca-cola'):
            self.GeracaoCocaCola()
        # ____Easter Eggs 2____#
        elif (receave == 'e o gole'):
            self.EoGole()
        else:
            pygame.mixer.music.load('erro.mp3')
            pygame.mixer.music.play()

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

    # Professor
    def GoPR(self):
        root13 = Toplevel(self.master)
        pr = Professor(root13)

    # Sem Pernas
    def GoSP(self):
        root15 = Toplevel(self.master)
        sp = SemPerna(root15)

    # João Grande
    def GoJG(self):
        root9 = Toplevel(self.master)
        jg = JoaoGrande(root9)

    # Gato
    def GoGA(self):
        root8 = Toplevel(self.master)
        ga = Gato(root8)

    # Dora
    def GoDO(self):
        root7 = Toplevel(self.master)
        do = Dora(root7)

    # Pirulito
    def GoPI(self):
        root17 = Toplevel(self.master)
        bv = Pirulito(root17)

    # Boa Vida
    def GoBV(self):
        root4 = Toplevel(self.master)
        bv = BoaVida(root4)

    # Volta Seca
    def GoVS(self):
        root16 = Toplevel(self.master)
        vs = VoltaSeca(root16)

    # Dalva
    def GoDV(self):
        root6 = Toplevel(self.master)
        dv = Dalva(root6)

    # D'Aninha
    def GoDA(self):
        root5 = Toplevel(self.master)
        da = Daninha(root5)

    # Padre Jose Pedro
    def GoPJP(self):
        root10 = Toplevel(self.master)
        pjp = Padre(root10)

    # Querido de Deus
    def GoQDD(self):
        root14 = Toplevel(self.master)
        qdd = QueridoDeDeus(root14)

#############################################################################################################

    # Pedro Bala 2
    def GoPB2(self):
        root19 = Toplevel(self.master)
        pb2 = PedroBala2(root19)

    # Professor
    def GoPR2(self):
        root20 = Toplevel(self.master)
        pr2 = Professor2(root20)

    # Sem Pernas 2
    def GoSP2(self):
        root21 = Toplevel(self.master)
        sp2 = SemPerna2(root21)

    # João Grande
    def GoJG2(self):
        root22 = Toplevel(self.master)
        jg2 = JoaoGrande2(root22)

    # Gato
    def GoGA2(self):
        root23 = Toplevel(self.master)
        ga2 = Gato2(root23)

    # Dora
    def GoDO2(self):
        root24 = Toplevel(self.master)
        do2 = Dora2(root24)

    # Pirulito
    def GoPI2(self):
        root25 = Toplevel(self.master)
        bv2 = Pirulito2(root25)

    # Boa Vida
    def GoBV2(self):
        root26 = Toplevel(self.master)
        bv2 = BoaVida2(root26)

    # Volta Seca
    def GoVS2(self):
        root27 = Toplevel(self.master)
        vs2 = VoltaSeca2(root27)

    # Dalva
    def GoDV2(self):
        root28 = Toplevel(self.master)
        dv2 = Dalva2(root28)

    # D'Aninha
    def GoDA2(self):
        root29 = Toplevel(self.master)
        da2 = Daninha2(root29)

    # Padre Jose Pedro
    def GoPJP2(self):
        root30 = Toplevel(self.master)
        pjp2 = Padre2(root30)

    # Querido de Deus
    def GoQDD2(self):
        root31 = Toplevel(self.master)
        qdd2 = QueridoDeDeus2(root31)

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
        self.master.after(49000, self.master.withdraw)

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
        self.master.after(42000, self.master.withdraw)

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
        pygame.mixer.music.load('Boa Vida.mp3')
        pygame.mixer.music.play()
        self.master.after(2000, self.master.withdraw)
        self.master.after(2800, self.GoVS)
        self.master.mainloop()

    def GoVS(self):
        root16 = Toplevel(self.master)
        vs = VoltaSeca(root16)

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
        pygame.mixer.music.load('Aninha.mp3')
        pygame.mixer.music.play()
        self.master.after(7000, self.master.withdraw)
        self.master.after(7800, self.GoDO)
        self.master.mainloop()

    def GoDO(self):
        root7 = Toplevel(self.master)
        do = Dora(root7)

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
        self.master.mainloop()

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
        pygame.mixer.music.load('releitura5.mp3')
        pygame.mixer.music.play()
        self.master.after(12000, self.master.withdraw)
        self.master.after(12800, self.Video3)
        self.master.mainloop()
        self.master.mainloop()

    def Video3(self):
        clip2 = VideoFileClip('Dora.mp4')
        clip2.preview()
        pygame.mixer.music.load('releitura6.mp3')
        pygame.mixer.music.play()
        self.master.after(7000, self.Video4)

    def Video4(self):
        clip3 = VideoFileClip('Dora2.mp4')
        clip3.preview()
        pygame.mixer.music.load('releitura7.mp3')
        pygame.mixer.music.play()
        self.master.after(8000, self.Video5)
    def Video5(self):
        clip4 = VideoFileClip('DoraM.mp4')
        clip4.preview()
        clip5 = VideoFileClip('Finish.mp4')
        clip5.preview()
        pygame.mixer.music.load('Finish.mp3')
        pygame.mixer.music.play()

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
        pygame.mixer.music.load('Gato.mp3')
        pygame.mixer.music.play()
        self.master.after(2000, self.master.withdraw)
        self.master.after(2800, self.GoPI)
        self.master.mainloop()

    def GoPI(self):
        root17 = Toplevel(self.master)
        bv = Pirulito(root17)

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
        pygame.mixer.music.load('Joao Grande.mp3')
        pygame.mixer.music.play()
        self.master.after(2000, self.master.withdraw)
        self.master.after(2800, self.GoGA)
        self.master.mainloop()

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
        pygame.mixer.music.load('Padre.mp3')
        pygame.mixer.music.play()
        self.master.after(19000, self.master.withdraw)
        self.master.after(19800, self.GoDA)
        self.master.mainloop()

    def GoDA(self):
        root5 = Toplevel(self.master)
        da = Daninha(root5)

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
        pygame.mixer.music.load('Pedro bala.mp3')
        pygame.mixer.music.play()
        self.master.after(2000, self.master.withdraw)
        self.master.after(2800, self.GoPR)
        self.master.mainloop()

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
        pygame.mixer.music.load('Pirulito.mp3')
        pygame.mixer.music.play()
        self.master.after(2000, self.master.withdraw)
        self.master.after(2800, self.GoBV)
        self.master.mainloop()

    def GoBV(self):
        root4 = Toplevel(self.master)
        bv = BoaVida(root4)

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
        pygame.mixer.music.load('Professor.mp3')
        pygame.mixer.music.play()
        self.master.after(2000, self.master.withdraw)
        self.master.after(2800, self.GoSP)
        self.master.mainloop()

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
        pygame.mixer.music.load('Querido de Deus.mp3')
        pygame.mixer.music.play()
        self.master.after(12000, self.master.withdraw)
        self.master.after(12800, self.GoPJP)
        self.master.mainloop()

    def GoPJP(self):
        root10 = Toplevel(self.master)
        pjp = Padre(root10)

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
        pygame.mixer.music.load('Sem Pernas.mp3')
        pygame.mixer.music.play()
        self.master.after(2000, self.master.withdraw)
        self.master.after(2800, self.GoJG)
        self.label = Label(self.master, image=self.photo15, bg='black').grid(row=0,column=0)
        self.master.mainloop()

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
        pygame.mixer.music.load('Volta Seca.mp3')
        pygame.mixer.music.play()
        self.master.after(5000, self.master.withdraw)
        self.master.after(5500, self.Releitura)
        self.master.mainloop()

    def Releitura(self):
        pygame.mixer.music.load('releitura2.mp3')
        pygame.mixer.music.play()
        self.master.after(14000, self.Releitura2)

    def Releitura2(self):
        clip = VideoFileClip('releitura2.mp4')
        clip.preview()
        pygame.mixer.music.load('releitura3.mp3')
        pygame.mixer.music.play()
        self.master.after(5000, self.Releitura3)

    def Releitura3(self):
        clip2 = VideoFileClip('releitura3.mp4')
        clip2.preview()
        clip2.reader.close()
        pygame.mixer.music.load('releitura4.mp3')
        pygame.mixer.music.play()
        self.master.after(7000, self.GoQDD)

    def GoQDD(self):
        root14 = Toplevel(self.master)
        qdd = QueridoDeDeus(root14)

##################################Personagens apenas contando como são###########################################
class BoaVida2:
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
        self.photo17 = PhotoImage(file='Boa Vida.png')
        self.label = Label(self.master, image=self.photo17, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('BoaVidaQ.mp3')
        pygame.mixer.music.play()
        self.master.after(35000, self.master.withdraw)
        self.master.mainloop()

class Daninha2:
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
        self.photo18 = PhotoImage(file='d aninha.png')
        self.label = Label(self.master, image=self.photo18, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('AninhaQ.mp3')
        pygame.mixer.music.play()
        self.master.after(7000, self.master.withdraw)
        self.master.mainloop()

class Dalva2:
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
        self.photo19 = PhotoImage(file='Dalva.png')
        self.label = Label(self.master, image=self.photo19, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('DalvaQ.mp3')
        pygame.mixer.music.play()
        self.master.after(9000, self.master.withdraw)
        self.master.mainloop()

class Dora2:
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
        self.photo20 = PhotoImage(file='Dora.png')
        self.label = Label(self.master, image=self.photo20, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('DoraQ.mp3')
        pygame.mixer.music.play()
        self.master.after(46000, self.master.withdraw)
        self.master.mainloop()

class Gato2:
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
        self.photo21 = PhotoImage(file='Gato.png')
        self.label = Label(self.master, image=self.photo21, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('GatoQ.mp3')
        pygame.mixer.music.play()
        self.master.after(29000, self.master.withdraw)
        self.master.mainloop()

class JoaoGrande2:
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
        self.photo22 = PhotoImage(file='Joao Grande.png')
        self.label = Label(self.master, image=self.photo22, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('JoaoQ.mp3')
        pygame.mixer.music.play()
        self.master.after(35000, self.master.withdraw)
        self.master.mainloop()

class Padre2:
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
        self.photo23 = PhotoImage(file='Padre Jose Pedro.png')
        self.label = Label(self.master, image=self.photo23, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('Padre.mp3')
        pygame.mixer.music.play()
        self.master.after(19000, self.master.withdraw)
        self.master.mainloop()

class PedroBala2:
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
        self.photo24 = PhotoImage(file='Pedro Bala.png')
        self.label = Label(self.master, image=self.photo24, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('PedroQ.mp3')
        pygame.mixer.music.play()
        self.master.after(30000, self.master.withdraw)
        self.master.mainloop()

class Pirulito2:
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
        self.photo25 = PhotoImage(file='Pirulito.png')
        self.label = Label(self.master, image=self.photo25, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('PirulitoQ.mp3')
        pygame.mixer.music.play()
        self.master.after(27000, self.master.withdraw)
        self.master.mainloop()

class Professor2:
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
        self.photo26 = PhotoImage(file='Professor.png')
        self.label = Label(self.master, image=self.photo26, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('ProfessorQ.mp3')
        pygame.mixer.music.play()
        self.master.after(18000, self.master.withdraw)
        self.master.mainloop()

class QueridoDeDeus2:
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
        self.photo27 = PhotoImage(file='Querido de deus.png')
        self.label = Label(self.master, image=self.photo27, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('QueridoQ.mp3')
        pygame.mixer.music.play()
        self.master.after(16000, self.master.withdraw)
        self.master.mainloop()

class SemPerna2:
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
        self.photo28 = PhotoImage(file='Sem Perna.png')
        self.label = Label(self.master, image=self.photo28, bg='black').grid(row=0, column=0)
        pygame.mixer.music.load('SemPernasQ.mp3')
        pygame.mixer.music.play()
        self.master.after(31000, self.master.withdraw)
        self.master.mainloop()

class VoltaSeca2:
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
        self.photo29 = PhotoImage(file='Volta Seca.png')
        self.label = Label(self.master, image=self.photo29, bg='black').grid(row=0,column=0)
        pygame.mixer.music.load('VoltaSecaQ.mp3')
        pygame.mixer.music.play()
        self.master.after(9000, self.master.withdraw)
        self.master.mainloop()

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
        enter = True
        main()
    else:
        print("ALGO DEU ERRADO! REPITA A FRASE")
