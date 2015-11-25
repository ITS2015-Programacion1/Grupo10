# coding: utf-8
import pilasengine
import time
import random
pilas = pilasengine.iniciar(alto=640,ancho=800)
puntajeJ1=0
puntajeJ2=0


class Menu(pilasengine.escenas.Escena):
    
    def iniciar(self):
        fondo=pilas.fondos.Fondo("fondo.jpg")
        fondo.definir_escala(4)
        intro = pilas.musica.cargar("Battle City (NES) Music - Game Start.mp3")
        intro.reproducir()
        self.menu=pilas.actores.Menu([("Iniciar Juego",self.iniciar_juego), ("Instrucciones",self.instrucciones),("Salir",self.salir)])

    def iniciar_juego(self):
        self.menu.eliminar()
        pilas.escenas.Juego()

    def salir(self):
        exit()

    def instrucciones(self):
        self.menu.eliminar()
        pilas.escenas.Instr()

class Instr(pilasengine.escenas.Escena):
    
    def iniciar(self):
        instr=pilas.fondos.Fondo("Ayuda.png")
        self.menui=pilas.actores.Menu([("Comenzar Juego",self.comenzar),("Volver al Menu",self.salirm)])
        intro = pilas.musica.cargar("Battle City (NES) Music - Game Start.mp3")
        intro.reproducir()

    def comenzar(self):
        self.menui.eliminar()
        pilas.escenas.Juego()
    
    def salirm(self):
        self.menui.eliminar()
        pilas.escenas.Menu()

class Pantalla_puntaje(pilasengine.escenas.Escena):

    def iniciar(self):
        fondo=pilas.fondos.Fondo("fondo.jpg")
        fondo.definir_escala(4)
        intro = pilas.musica.cargar("Battle City (NES) Music - Game Start.mp3")
        intro.reproducir()
        texto_guion=pilasengine.actores.texto.Texto(pilas,texto="Jugador 1:   -    :Jugador 2")
        texto_guion.y=-200
        texto_p1=pilasengine.actores.texto.Texto(pilas,texto=str(puntajeJ1))
        texto_p1.y=-200
        texto_p1.x=-12
        texto_p2=pilasengine.actores.texto.Texto(pilas,texto=str(puntajeJ2))
        texto_p2.y=-200
        texto_p2.x=10        
        self.menu=pilas.actores.Menu([("Seguir Juego",self.iniciar_juego),("Volver al Menu",self.salir)])
    
    def iniciar_juego(self):
        self.menu.eliminar()
        pilas.escenas.Juego()
    
    def salir(self):
        global puntajeJ2, puntajeJ1
        puntajeJ1=0
        puntajeJ2=0
        self.menu.eliminar()
        pilas.escenas.Menu()

class Juego(pilasengine.escenas.Escena):
    
    def iniciar(self):
        pilas.fisica.gravedad_x=0
        pilas.fisica.gravedad_y=0
        teclas = {pilas.simbolos.a: 'izquierda',
                      pilas.simbolos.d: 'derecha',
                      pilas.simbolos.w: 'arriba',
                      pilas.simbolos.s: 'abajo',
                      pilas.simbolos.j: 'boton'}
        mi_control = pilas.control.Control(teclas)
        mapa = pilas.actores.MapaTiled("mapa.tmx")
        musica = pilas.musica.cargar("Dendy 8Bit Battle City Music Remix2.mp3")
        musica.reproducir(repetir=True)
        
        def pasar_a_menu():
            pilas.escenas.Pantalla_puntaje()
        
        def Tanque1_destruido(Tanque1,Bala):
            global puntajeJ2
            efecto = random.uniform(.25,.75)
            Tanque1.eliminar()
            Bala.eliminar()
            puntajeJ2+=1
            texto_victoria=pilasengine.actores.texto.Texto(pilas,texto="El Tanque Rojo es el vencedor!")
            texto_victoria.y = -100
            texto_victoria.escala = (efecto,1),.5
            texto_victoria.definir_color(pilas.colores.negro)
            texto_guion=pilasengine.actores.texto.Texto(pilas,texto="Jugador 1:   -    :Jugador 2")
            texto_guion.y=-200
            texto_guion.definir_color(pilas.colores.negro)
            texto_p1=pilasengine.actores.texto.Texto(pilas,texto=str(puntajeJ1))
            texto_p1.y=-200
            texto_p1.x=-12
            texto_p1.definir_color(pilas.colores.negro)
            texto_p2=pilasengine.actores.texto.Texto(pilas,texto=str(puntajeJ2))
            texto_p2.y=-200
            texto_p2.x=10
            texto_p2.definir_color(pilas.colores.negro)
            jugador2.definir_radio_de_colision(0)
            pilas.tareas.agregar(2.2,pasar_a_menu)
            
        def Tanque2_destruido(Tanque2,Bala):
            global puntajeJ1
            efecto = random.uniform(.25,.75)
            Tanque2.eliminar()
            Bala.eliminar()
            puntajeJ1+=1
            texto_victoria=pilasengine.actores.texto.Texto(pilas,texto="El Tanque Verde es el vencedor!")
            texto_victoria.y = -100
            texto_victoria.escala = (efecto,1),.5
            texto_victoria.definir_color(pilas.colores.negro)
            texto_guion=pilasengine.actores.texto.Texto(pilas,texto="Jugador 1:   -    :Jugador 2")
            texto_guion.y=-200
            texto_guion.definir_color(pilas.colores.negro)
            texto_p1=pilasengine.actores.texto.Texto(pilas,texto=str(puntajeJ1))
            texto_p1.y=-200
            texto_p1.x=-12
            texto_p1.definir_color(pilas.colores.negro)
            texto_p2=pilasengine.actores.texto.Texto(pilas,texto=str(puntajeJ2))
            texto_p2.y=-200
            texto_p2.x=10
            texto_p2.definir_color(pilas.colores.negro)
            jugador1.definir_radio_de_colision(0)
            pilas.tareas.agregar(2.2,pasar_a_menu)
            
        class Balita(pilasengine.actores.Actor):
            
            def iniciar(self):
                self.imagen = pilas.imagenes.cargar("bala.png")
                self.radio_de_colision = 2

        class Tanque1(pilasengine.actores.Actor):
        
            def iniciar(self):
                self.grilla = pilas.imagenes.cargar_grilla ("tanque1.png",8)
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

        class Tanque2(pilasengine.actores.Actor):
        
            def iniciar(self):
                self.grilla = pilas.imagenes.cargar_grilla ("tanque2.png",8)
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

        jugador1 = Tanque1(pilas)
        jugador2 = Tanque2(pilas)

        jugador1.definir_escala(1)
        jugador2.definir_escala(1)

        jugador1.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        jugador2.aprender(pilas.habilidades.LimitadoABordesDePantalla)

        jugador2.rotacion=180

        jugador1.aprender(pilas.habilidades.Disparar,frecuencia_de_disparo=1,grupo_enemigos=jugador2,cuando_elimina_enemigo=Tanque2_destruido,municion=Balita)
        jugador2.aprender(pilas.habilidades.Disparar,frecuencia_de_disparo=1,control=mi_control,grupo_enemigos=jugador1,cuando_elimina_enemigo=Tanque1_destruido,municion=Balita)

        jugador1.aprender(pilas.habilidades.PuedeExplotar)
        jugador2.aprender(pilas.habilidades.PuedeExplotar)

        rect1 = pilas.fisica.Rectangulo(-100,0,26,26,dinamica=False)
        rect2 = pilas.fisica.Rectangulo(100,0,26,26,dinamica=False)

        rect1.x =-250
        rect2.x = 250

        rect1.y =-250
        rect2.y = 250

        rect2.rotacion = 180

        jugador1.aprender(pilas.habilidades.Imitar,rect1)
        jugador2.aprender(pilas.habilidades.Imitar,rect2)

        jugador1.aprender(pilas.habilidades.MoverseConElTeclado,velocidad_maxima=2,direcciones=4)
        jugador2.aprender(pilas.habilidades.MoverseConElTeclado,velocidad_maxima=2,direcciones=4,control=mi_control)

pilas.escenas.vincular(Menu)
pilas.escenas.vincular(Juego)
pilas.escenas.vincular(Pantalla_puntaje)
pilas.escenas.vincular(Instr)
pilas.escenas.Menu()

pilas.ejecutar()
