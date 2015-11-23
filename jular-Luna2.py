# coding: utf-8
import pilasengine
import time
import random
pilas = pilasengine.iniciar(alto=640,ancho=800)
pilas.fisica.gravedad_x=0
pilas.fisica.gravedad_y=0
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
        instr=pilas.fondos.Noche()
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
        global puntajeJ2
        global puntajeJ1
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
        
        medio = pilas.actores.Actor(x=0,y=0)
        medio.escala = 0
        medio.crear_figura_de_colision_rectangular(0,0,160,160)

        techo = pilas.actores.Actor(x=0,y=312)
        techo.escala = 0
        techo.crear_figura_de_colision_rectangular(0,0,800,16)

        suelo = pilas.actores.Actor(x=0,y=-312)
        suelo.escala = 0
        suelo.crear_figura_de_colision_rectangular(0,0,800,16)

        paredD = pilas.actores.Actor(x=392,y=0)
        paredD.escala = 0
        paredD.crear_figura_de_colision_rectangular(0,0,16,800)

        paredI = pilas.actores.Actor(x=-392,y=0)
        paredI.escala = 0
        paredI.crear_figura_de_colision_rectangular(0,0,16,800)

        obsAr1 = pilas.actores.Actor(x=0,y=272)
        obsAr1.escala = 0
        obsAr1.crear_figura_de_colision_rectangular(0,0,32,64)

        obsAr2 = pilas.actores.Actor(x=0,y=112)
        obsAr2.escala = 0
        obsAr2.crear_figura_de_colision_rectangular(0,0,32,64)

        obsAb1 = pilas.actores.Actor(x=0,y=-272)
        obsAb1.escala = 0
        obsAb1.crear_figura_de_colision_rectangular(0,0,32,64)

        obsAb2 = pilas.actores.Actor(x=0,y=-112)
        obsAb2.escala = 0
        obsAb2.crear_figura_de_colision_rectangular(0,0,32,64)

        obsDe1 = pilas.actores.Actor(x=328,y=0)
        obsDe1.escala = 0
        obsDe1.crear_figura_de_colision_rectangular(0,0,112,32)

        obsDe2 = pilas.actores.Actor(x=144,y=0)
        obsDe2.escala = 0
        obsDe2.crear_figura_de_colision_rectangular(0,0,64,32)

        obsIz1 = pilas.actores.Actor(x=-328,y=0)
        obsIz1.escala = 0
        obsIz1.crear_figura_de_colision_rectangular(0,0,112,32)

        obsIz2 = pilas.actores.Actor(x=-112,y=0)
        obsIz2.escala = 0
        obsIz2.crear_figura_de_colision_rectangular(0,0,64,32)

        LArD1 = pilas.actores.Actor(x=200,y=216)
        LArD1.escala = 0
        LArD1.crear_figura_de_colision_rectangular(0,0,80,16)

        LArD2 = pilas.actores.Actor(x=232,y=184)
        LArD2.escala = 0
        LArD2.crear_figura_de_colision_rectangular(0,0,16,80)

        LAbD1 = pilas.actores.Actor(x=200,y=-216)
        LAbD1.escala = 0
        LAbD1.crear_figura_de_colision_rectangular(0,0,80,16)

        LAbD2 = pilas.actores.Actor(x=232,y=-184)
        LAbD2.escala = 0
        LAbD2.crear_figura_de_colision_rectangular(0,0,16,80)

        LArI1 = pilas.actores.Actor(x=-200,y=216)
        LArI1.escala = 0
        LArI1.crear_figura_de_colision_rectangular(0,0,80,16)

        LArI2 = pilas.actores.Actor(x=-232,y=184)
        LArI2.escala = 0
        LArI2.crear_figura_de_colision_rectangular(0,0,16,80)

        LAbI1 = pilas.actores.Actor(x=-200,y=-216)
        LAbI1.escala = 0
        LAbI1.crear_figura_de_colision_rectangular(0,0,80,16)

        LAbI2 = pilas.actores.Actor(x=-232,y=-184)
        LAbI2.escala = 0
        LAbI2.crear_figura_de_colision_rectangular(0,0,16,80)

        paredes = [techo,suelo,paredD,paredI,obsAr1,obsAr2,obsAb1,obsAb2,obsDe1,obsDe2,obsIz1,obsIz2,LArD1,LArD2,LAbD1,LAbD2,LArI1,LArI2,LAbI1,LAbI2]

        def pasar_a_menu():
            pilas.escenas.Pantalla_puntaje()
        
        def Tanque1_destruido(Tanque1,Bala):
            global puntajeJ2
            efecto = random.uniform(.25,.75)
            Tanque1.eliminar()
            Bala.eliminar()
            texto_victoria=pilasengine.actores.texto.Texto(pilas,texto="El Tanque Rojo es el vencedor!")
            texto_victoria.y = -100
            texto_victoria.escala = (efecto,1),.5
            texto_victoria.definir_color(pilas.colores.negro)
            jugador2.definir_radio_de_colision(0.1)
            pilas.tareas.agregar(2.2,pasar_a_menu)
            puntajeJ2+=1

        def Tanque2_destruido(Tanque2,Bala):
            global puntajeJ1
            efecto = random.uniform(.25,.75)
            Tanque2.eliminar()
            Bala.eliminar()
            texto_victoria=pilasengine.actores.texto.Texto(pilas,texto="El Tanque Verde es el vencedor!")
            texto_victoria.y = -100
            texto_victoria.escala = (efecto,1),.5
            texto_victoria.definir_color(pilas.colores.negro)
            jugador1.definir_radio_de_colision(0.1)
            pilas.tareas.agregar(2.2,pasar_a_menu)
            puntajeJ1+=1

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

        jugador1.aprender(pilas.habilidades.Disparar,frecuencia_de_disparo=1.25,grupo_enemigos=jugador2,cuando_elimina_enemigo=Tanque2_destruido)
        jugador2.aprender(pilas.habilidades.Disparar,frecuencia_de_disparo=1.25,control=mi_control,grupo_enemigos=jugador1,cuando_elimina_enemigo=Tanque1_destruido)

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

        tanques = [Tanque1,Tanque2]

        def bala_a_pared(Bala,paredes):
            Bala.eliminar()
        pilas.colisiones.agregar(Bala,paredes,bala_a_pared)

pilas.escenas.vincular(Menu)
pilas.escenas.vincular(Juego)
pilas.escenas.vincular(Pantalla_puntaje)
pilas.escenas.vincular(Instr)
pilas.escenas.Menu()

pilas.ejecutar()
