import time

class Robot:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.motorDireita = ""
        self.motorEsquerda = ""
    
    @classmethod
    def DefinirMotor(self, lado, p1):
        if (lado == "esquerda"):
            self.motorEsquerda = p1
        else:
            self.motorDireita = p1
        return f"O motor da {lado} está na porta {p1}"

    def Andar(self, dir, mod):
        if (mod == "aut"):
            dur = input("Insira o tempo: ")
            dur = int(dur)
            print(f"Andando para a {dir}")            
            time.sleep(dur)
            print("Instrução finalizada")
        else:
            while (True):
                print (f"Andando para a {dir}")
