import library
import time

r = library.Robot(1, 2)
d1 = library.Robot.DefinirMotor("direita", 2)
d2 = library.Robot.DefinirMotor("esquerda", 1)
print (d1 + " - " + d2)
r.Andar("frente", "aut")
print("Finalizando")
time.sleep(5)
print("Entrando no modo teleop")
time.sleep(2)
r.Andar("esquerda", "teleop")

#Added a coment