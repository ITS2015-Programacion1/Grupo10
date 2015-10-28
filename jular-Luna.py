# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()
fondo=pilas.fondos.Fondo("fondo.jpg")
fondo.definir_escala(2.5)


teclas = {pilas.simbolos.a: 'izquierda',
                      pilas.simbolos.d: 'derecha',
                      pilas.simbolos.w: 'arriba',
                      pilas.simbolos.s: 'abajo',
                      pilas.simbolos.ESPACIO: 'boton'}

class Tanque1(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "/home/julianluna/Grupo10/tanque1.png"

class Tanque2(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "/home/julianluna/Grupo10/tanque2.png"
        mi_control = pilas.control.Control(pilas.escena_actual(), teclas)
   def actualizar(self):
        if pilas.escena_actual().control.izquierda:
                self.x -= 5
                self.espejado = True
        elif pilas.escena_actual().control.derecha:
            self.x += 5
            self.espejado = False        

jugador1 = Tanque1(pilas)
jugador1.x =-100
jugador1.definir_escala(0.3)
jugador1.aprender(pilas.habilidades.LimitadoABordesDePantalla)
jugador1.aprender(pilas.habilidades.MoverseComoCoche)


jugador2 = Tanque2(pilas)
jugador2.x = 100
jugador2.definir_escala(0.3)
jugador2.rotacion=180
jugador2.aprender(pilas.habilidades.LimitadoABordesDePantalla)
jugador2.aprender(pilas.habilidades.MoverseComoCoche)



pilas.ejecutar()
