# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()
fondo=pilas.fondos.Fondo("fondo.jpg")
fondo.definir_escala(2.5)
teclas = {pilas.simbolos.a: 'izquierda',
              pilas.simbolos.d: 'derecha',
              pilas.simbolos.w: 'arriba',
              pilas.simbolos.s: 'abajo',
              pilas.simbolos.j: 'boton'}
mi_control = pilas.control.Control(teclas)


def iniciarjuego():
    menu.eliminar()

    class BalaT(pilasengine.actores.Actor):


        def __init__(self, pilas, x=0, y=0, rotacion=0, velocidad_maxima=9,
                     angulo_de_movimiento=0):

            super(BalaT, self).__init__(pilas=pilas, x=x, y=y)
            self.imagen = pilas.imagenes.cargar("/home/julianluna/Grupo10/bala.png")
            self.rotacion = 0

            self.radio_de_colision = 5

            self.hacer(pilas.comportamientos.Proyectil,
                       velocidad_maxima=velocidad_maxima,
                       aceleracion=1,
                       angulo_de_movimiento=angulo_de_movimiento,
                       gravedad=0)

            self.aprender(self.pilas.habilidades.EliminarseSiSaleDePantalla)
            self.cuando_se_elimina = None

        def eliminar(self):
            if self.cuando_se_elimina:
                self.cuando_se_elimina(self)

            super(BalaT, self).eliminar()

    class Tanque1(pilasengine.actores.Actor):
        def iniciar(self):
            self.grilla = pilas.imagenes.cargar_grilla ("/home/julianluna/Grupo10/tanque1.png",8)
            self.imagen = self.grilla
        
        def actualizar(self):
            if pilas.escena_actual().control.izquierda:
                self.imagen.avanzar()
                self.rotacion = 180
            if pilas.escena_actual().control.derecha:
                self.imagen.avanzar()
                self.rotacion = 0
            if pilas.escena_actual().control.arriba:
                self.rotacion = 90
                self.imagen.avanzar()
            if pilas.escena_actual().control.abajo:
                self.rotacion = 270
                self.imagen.avanzar()



    jugador1 = Tanque1(pilas)
    jugador1.x =-100
    jugador1.definir_escala(1)
    jugador1.aprender(pilas.habilidades.LimitadoABordesDePantalla)
    jugador1.aprender(pilas.habilidades.MoverseConElTeclado,velocidad_maxima=2,direcciones=4)
    jugador1.aprender(pilas.habilidades.Disparar,frecuencia_de_disparo=2,municion=BalaT)


    class Tanque2(pilasengine.actores.Actor):
        def iniciar(self):
            self.grilla = pilas.imagenes.cargar_grilla ("/home/julianluna/Grupo10/tanque2.png",8)
            self.imagen = self.grilla

        def actualizar(self):
            if mi_control.izquierda:
                self.imagen.avanzar()
                self.rotacion = 180
            if mi_control.derecha:
                self.imagen.avanzar()
                self.rotacion = 0
            if mi_control.arriba:
                self.rotacion = 90
                self.imagen.avanzar()
            if mi_control.abajo:
                self.rotacion = 270
                self.imagen.avanzar()
            if mi_control.boton:
                BalaT.rotacion = 180



           

    jugador2 = Tanque2(pilas)
    jugador2.x = 100
    jugador2.definir_escala(1)
    jugador2.rotacion=180
    jugador2.aprender(pilas.habilidades.LimitadoABordesDePantalla)
    jugador2.aprender(pilas.habilidades.MoverseConElTeclado,velocidad_maxima=2,direcciones=4,control=mi_control)
    jugador2.aprender(pilas.habilidades.Disparar,frecuencia_de_disparo=2,municion=BalaT,control=mi_control)

    disparo = BalaT
    
    """def Tanque1_destruido(BalaT,Tanque1):
        Tanque1.eliminar()
        BalaT.eliminar()
    pilas.colisiones.agregar(disparo,jugador1,Tanque1_destruido)
 

    def Tanque2_destruido(BalaT,Tanque2):
        Tanque2.eliminar()
        BalaT.eliminar()
    pilas.colisiones.agregar(disparo,jugador2,Tanque2_destruido)"""

def Salir():
    pilas.terminar()


menu=pilas.actores.Menu([("Iniciar juego", iniciarjuego),("Salir del juego", Salir)])

pilas.ejecutar()
