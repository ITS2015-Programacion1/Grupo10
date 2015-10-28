# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
fondo=pilas.fondos.Fondo("fondo.jpg")
fondo.definir_escala(2.5)


class Tanque1(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "/home/julianluna/Grupo10/tanque1.png"

class Tanque2(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "/home/julianluna/Grupo10/tanque2.png"
        
jugador1 = Tanque1(pilas)
jugador1.x =-300
jugador1.definir_escala(0.3)


jugador2 = Tanque2(pilas)
jugador2.x = 300
jugador2.definir_escala(0.3)
jugador2.rotacion=180



pilas.ejecutar()
