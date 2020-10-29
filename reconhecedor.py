from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana","10","italic","bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri","9")
        self.sair["width"] = 10
        #An option is pass event by bind, as:
        self.sair.bind("<Button-1>", self.mudarTexto)
        #Another option, it's calling event using command, like:
        self.sair["command"] = self.mudarTexto 
        self.sair.pack()

        self.fontePadrao = ("Arial","10")
        self.primeiroContainer = Frame(master)

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
root = Tk()
root.geometry("500x100") #Width x Height
Application(root)
root.mainloop()