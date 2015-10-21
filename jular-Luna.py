# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
fondo=pilas.fondos.Fondo("fondo.jpg")
fondo.definir_escala(2.5)
jugador1=pilas.actores.Torreta()
jugador1.x=-300
jugador2=pilas.actores.Torreta()
jugador2.x=300
jugador1.aprender(pilas.habilidades.MoverseConElTeclado)

jugador1.aprender(pilas.habilidades.LimitadoABordesDePantalla)
pilas.ejecutar()