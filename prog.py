import time
import biblioteca

r = biblioteca.Robo(1, 2)
d1 = biblioteca.Robo.definirMotores("esquerda", 1)
d2 = biblioteca.Robo.definirMotores("direita", 2)

print(d1 + " - " + d2)
r.Andar("frente", "aut")
print("Instrução finalizada")
time.sleep(5)
print("Entrando no modo teleoperado")
time.sleep(5)
r.Andar("frente", "teleOP")