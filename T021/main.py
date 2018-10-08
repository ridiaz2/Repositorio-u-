from classes import *
from gui.entities import Human, Game, _SCALE
from datetime import datetime, timedelta
from parameters import parametros as par
from collections import deque


gui.init()

_PATH = os.path.dirname(os.path.abspath(__file__))

def conservar_angulos(*objetos):
    for i in objetos:
        i.angle = i.angle

class Simulacion:

    def __init__(self, casino=Casino()):
        self.casino = casino
        self.hora = datetime(1, 1, 1)


    def add_client(self, x=30, y=10, personalidad=[]):
        if not personalidad:
            personalidad = choice(list(Cliente.dicc_personalidades))
        cliente = self.casino.agregar_cliente(personalidad, x, y)
        gui.add_entity(cliente)
        cliente.setFixedSize(73 * _SCALE, 73 * _SCALE)
        return cliente

    def add_something(self, tipo, x=0, y=0, angulo=0, agregar=True):
        if tipo in ("tragamonedas", "ruleta"):
            funcion = self.casino.agregar_juego
        else:
            funcion = self.casino.agregar_instalacion
        objeto = funcion(tipo, x, y)
        if angulo:
            objeto.angle = angulo
        gui.add_entity(objeto)
        id_ = objeto.id
        if tipo == "ruleta":
            simulacion.add_staff("dealer", x-5, y-30, id_)
            simulacion.add_staff("dealer", x+15, y-40, id_)
            simulacion.add_staff("dealer", x+40, y-40, id_)
            simulacion.add_staff("dealer", x+65, y-40, id_)
            simulacion.add_staff("dealer", x+25, y-20, id_)
            simulacion.add_staff("dealer", x+50, y-20, id_)
            simulacion.add_staff("dealer", x+75, y-20, id_)
            simulacion.add_staff("dealer", x+90, y-40, id_)
            simulacion.add_staff("dealer", x+100, y-20, id_)
        elif tipo == "tragamonedas":
            simulacion.add_staff("dealer", x - 32, (y + 20) + (50 * 2), id_)
            simulacion.add_staff("dealer", x + 140, (y + 20) + (50 * 2), id_)
            for i in range(3):
                simulacion.add_staff("dealer", x - 7, (y + 20) + (50 * i), id_)
                simulacion.add_staff("dealer", x + 18, (y + 20) + (50 * i), id_)
                simulacion.add_staff("dealer", x + 43, (y + 20) + (50 * i), id_)
                simulacion.add_staff("dealer", x + 67, (y + 20) + (50 * i), id_)
                simulacion.add_staff("dealer", x + 91, (y + 20) + (50 * i), id_)
                simulacion.add_staff("dealer", x + 115, (y + 20) + (50 * i),
                                     id_)
                simulacion.add_staff("dealer", x - 32, (y - 5) + (50 * i), id_)
                simulacion.add_staff("dealer", x + 140, (y - 5) + (50 * i), id_)

        elif tipo == "tarot":
            objeto.agregar_personal(self.casino.agregar_personal("mrt", x, y))


        elif tipo == "restobar":
            simulacion.add_staff("bartman", x + 22, y + 20, id_)
            simulacion.add_staff("bartman", x + 47, y + 20, id_)
            simulacion.add_staff("bartman", x + 72, y + 20, id_)
            simulacion.add_staff("bartman", x + 97, y + 20, id_)
            simulacion.add_staff("bartman", x - 10, y + 20, id_)
            simulacion.add_staff("bartman", x + 129, y + 20, id_)
            simulacion.add_staff("bartman", x - 10, y + 50, id_)
            simulacion.add_staff("bartman", x + 129, y + 50, id_)

            if agregar:
                simulacion.add_staff("bartman", x, y + 70, id_)
                simulacion.add_staff("bartman", x + 24, y + 70, id_)
                simulacion.add_staff("bartman", x + 52, y + 110, id_)
                simulacion.add_staff("bartman", x + 74, y + 110, id_)
            else:
                simulacion.add_staff("bartman", x + 119, y + 70, id_)
                simulacion.add_staff("bartman", x + 95, y + 70, id_)
                simulacion.add_staff("bartman", x + 63, y + 110, id_)

            simulacion.add_staff("bartman", x - 10, y + 90, id_)
            simulacion.add_staff("bartman", x + 14, y + 90, id_)
            simulacion.add_staff("bartman", x + 38, y + 90, id_)
            simulacion.add_staff("bartman", x + 105, y + 90, id_)
            simulacion.add_staff("bartman", x + 81, y + 90, id_)
            simulacion.add_staff("bartman", x + 129, y + 90, id_)

            simulacion.add_staff("bartman", x - 10, y + 110, id_)
            simulacion.add_staff("bartman", x + 30, y + 110, id_)
            simulacion.add_staff("bartman", x + 129, y + 110, id_)
            simulacion.add_staff("bartman", x + 96, y + 110, id_)

            simulacion.add_staff("bartman", x - 10, y + 140, id_)
            simulacion.add_staff("bartman", x + 14, y + 140, id_)
            simulacion.add_staff("bartman", x + 38, y + 140, id_)
            simulacion.add_staff("bartman", x + 105, y + 140, id_)
            simulacion.add_staff("bartman", x + 81, y + 140, id_)
            simulacion.add_staff("bartman", x + 129, y + 140, id_)
        return objeto

    def add_staff(self, tipo, x=0, y=0, lugar=-1):
        personal = self.casino.agregar_personal(tipo, x, y)
        if lugar != -1:
            if tipo in ("dealer"):
                objeto = self.casino.juegos[lugar]
            else:
                objeto = self.casino.instalaciones[lugar]
            objeto.agregar_personal(personal)
        gui.add_entity(personal)
        return personal

    def tick(self):

        conservar_angulos(*(list(self.casino.juegos.values()) + list(
            self.casino.personal.values()) + list(
            self.casino.clientes.values()) + list(
            self.casino.instalaciones.values())))
        if prob_valor(par.p):
            self.add_client()
        self.hora += timedelta(minutes=1)
        for i in self.casino.personal.values():
            i.tick(self.hora)
        for i in self.casino.instalaciones.values():
            i.tick(self.hora)
        if self.hora.minute == 0:
            print(self.hora)
            print(sum([1 for i in self.casino.personal.values() if i.activo(
                self.hora)]))

        for i in self.casino.clientes.values():
            self.casino.siguiente_accion(i)
            self.casino.mover_cliente(i, self.casino.camino(i))
            self.casino.realizar_accion(i)

    def marcar_mapeo(self):
        for i in range(0, len(self.casino.espacios_ocupados), 2):
            i1 = self.casino.espacios_ocupados[i]
            pixel_ = Pixel(i1[0], i1[1])
            gui.add_entity(pixel_)
            self.casino.pixeles.append(pixel_)

    def run(self):
        gui.set_size(773, 485)
        self.casino.mapeo()
        gui.run(self.tick, 1)

simulacion = Simulacion()
client = Cliente("ludopata")
client2 = Cliente("ludopata")
client.add_decoration("gui/assets/decoration/gris2.png")
traga1 = Game("tragamonedas", 30, 30)
traga2 = Game("tragamonedas", 200, 200)


tragamonedas1 = simulacion.add_something("tragamonedas", 280, 300)


ruleta1 = simulacion.add_something("ruleta", 240, 60)
ruleta2 = simulacion.add_something("ruleta", 390, 60)
ruleta3 = simulacion.add_something("ruleta", 240, 160)
ruleta4 = simulacion.add_something("ruleta", 400, 160)
restobar1 = simulacion.add_something("restobar", 40, 230, agregar=True)
restobar2 = simulacion.add_something("restobar", 580, 20, agregar=False)
tarot1 = simulacion.add_something("tarot", 658, 200, 90)
tarot2 = simulacion.add_something("tarot", 658, 290, 90)
tarot3 = simulacion.add_something("tarot", 658, 380, 90)
baño1 = simulacion.add_something("baños", 120, 20)
baño2 = simulacion.add_something("baños", 40, 410)
baño3 = simulacion.add_something("baños", 530, 410)
baño4 = simulacion.add_something("baños", 520, 20)


'''
clien1 = simulacion.add_client(30, 10)
clien1.destino = (135, 64)
clien2 = simulacion.add_client(30, 10)
clien2.destino = (530, 64)
clien3 = simulacion.add_client(30, 10)
clien3.destino = (540, 370)
clien4 = simulacion.add_client(30, 10)
clien4.destino = (110, 410)
clien5 = simulacion.add_client(30, 10)
clien5. destino = (200, 300)
clien6 = simulacion.add_client(30, 10)
clien6.destino = (540, 80)
clien7 = simulacion.add_client(30, 10)
clien7.destino = (332, 260)

clien8 = simulacion.add_client(30, 10)
clien8.destino = (620, 210)
clien9 = simulacion.add_client(30, 10)
clien9.destino = (620, 300)
clien10 = simulacion.add_client(30, 10)
clien10.destino = (620, 390)
clien11 = simulacion.add_client(30, 10)
clien11.destino = (200, 80)
clien12 = simulacion.add_client(30, 10)
clien12.destino = (350, 80)
clien13 = simulacion.add_client(30, 10)
clien13.destino = (360, 180)
clien14 = simulacion.add_client(30, 10)
clien14.destino = (200, 180)

#clien4 = simulacion.add_client(190, 300)
'''

#for i in simulacion.casino.juegos.values():
 #   print(i.__class__.__name__, len(i.personal))

#for i in simulacion.casino.instalaciones.values():
 #   print(i.tipo, len(i.personal))
#print("hoola")
simulacion.run()





'''simulacion.add_staff("dealer", x-5, y-30)
        simulacion.add_staff("dealer", 405, 20)
        simulacion.add_staff("dealer", 430, 20)
        simulacion.add_staff("dealer", 455, 20)
        simulacion.add_staff("dealer", 415, 40)
        simulacion.add_staff("dealer", 440, 40)
        simulacion.add_staff("dealer", 465, 40)
        simulacion.add_staff("dealer", 480, 20)
        simulacion.add_staff("dealer", 490, 40)'''