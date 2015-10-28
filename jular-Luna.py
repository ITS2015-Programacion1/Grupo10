# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
fondo=pilas.fondos.Fondo("fondo.jpg")
fondo.definir_escala(2.5)
class Alien(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "alien.png"
        
jugador1=pilasengine.actores.Nave(x=-300, y=0)
jugador1.x=-300
jugador2=pilas.actores.Nave(x=300, y=0)
jugador2.x=300
jugador1.aprender(pilas.habilidades.LimitadoABordesDePantalla)
jugador2.aprender(pilas.habilidades.LimitadoABordesDePantalla)
pilas.ejecutar()