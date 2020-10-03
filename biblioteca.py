import time

class Robo():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.motorEsquerda = ""
        self.motorDireita = ""

    @classmethod
    def definirMotores(self, lado, p):
        if (lado == "Esquerda"):
            self.motorEsquerda = p
        else:
            self.motorDireita = p
        return f"O motor da {lado} está conectado na porta {p}"

    def Andar(self, dir, mod):
        if (mod == "aut"):
            dur = input("Insira o tempo: ")
            dur = int(dur)
            print(f"Andando para a {dir}")
            time.sleep(dur)
            print("Instrução finalizada")
        else:
            while(True):
                print(f"Andando para a {dir}")