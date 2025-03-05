import random
import time
from colorama import Fore, Style

# Definiendo los objetos
class Player:
    # Parametros del jugador
    def __init__(self, hp=100, pp=50, fuerza=10, suerte=10, critico=1, lv=1, veneno=False):
        self.Nombre = None
        self.vida = hp
        self.habilidades = pp
        self.fuerza = fuerza
        self.suerte = suerte
        self.critico = critico
        self.level = lv
        self.veneno = veneno

    def cargar(self):
        self.critico += random.randint(1, 6)
        print(f'La probabilidad de critico es {self.critico}%')
        self.habilidades -= 5
        return self.habilidades

    def escape(self, rival):
        if self.level >= rival.level * 2:
            print(f'{self.Nombre} es demasiado fuerte para pelear contra {rival.nombre}')
        else:
            print(f'{self.Nombre} intento escapar pero se tropezo')
            self.vida -= 1

    def curar(self):
        suma = 100 - self.vida
        if self.vida < 100 and self.habilidades > 10:
            self.vida += suma
            print(f"Se ha regenerado un total de {suma}")
            self.habilidades -= 10
            return self.habilidades
        else:
            print("No se puede regenerar mas")

    def golpe(self, rival):
        if rival.vida > 0:
            critico = self.critico
            golpefuerte = random.randint(1, 100)
            print(golpefuerte)
            if golpefuerte <= critico:
                damage = self.fuerza * 2
                print('Golpe critico \n')
                print(f'{rival.nombre} ha recibido {damage} puntos de daño')
                self.critico = 1
                time.sleep(2)
            else:
                damage = self.fuerza
                print('Golpe normal \n')
                print(f'{rival.nombre} ha recibido {damage} puntos de daño')
                time.sleep(2)
            rival.vida -= damage
            rival.vida = max(rival.vida, 0)
            self.habilidades -= 1
            return self.habilidades

    def corteflama(self, rival):
        level = self.level
        if self.habilidades >= 20:
            if level >= 10:
                rival.vida -= 30
                self.vida -= 2
            elif level < 10:
                rival.vida -= 15
                self.vida -= 5
                print('Un golpe candente, pero no lo suficiente y pierdes 5 puntos de vida \n')

        if self.veneno:
            for i in range(5):
                self.vida -= 1
                time.sleep(5)
            self.veneno = False


class Duende:
    def __init__(self, nombre='duende'):
        # definiendo la aleatoriedad
        self.nombre = nombre
        self.vida = random.randint(10, 50)
        self.daño = random.randint(10, 20)
        self.saqueo = random.randint(10, 50)
        self.level = random.randint(1, 5)

    # Ver estadisticas
    def stats(self):
        print(self.vida, '\n')
        print(self.saqueo, '\n')
        print(self.daño, '\n')

    def atacar(self, rival):
        if rival.vida > 0:
            rival.vida -= self.daño
            print(Fore.RED + f'{rival.Nombre} ha recibido un golpe de {self.daño}' + Style.RESET_ALL)

    def atracar(self, rival):
        robo = random.randint(1, 10)
        if self.saqueo > rival.suerte:
            rival.habilidades -= robo
            print(Fore.RED + f'Duende te ha robado {robo} puntos de magia, que mala suerte' + Style.RESET_ALL)
        else:
            print(f'Duende no pudo robarle a {rival.Nombre}')

    def burla(self, rival):
        robo = random.randint(1, 6)
        rival.critico -= robo
        self.vida += robo
        print(Fore.RED + 'Duende se burla de ti \n')
        print(Fore.RED + f'Encima te baja ja probabilid de critico un {robo} \n')
        print(Fore.RED + f'y se cura {robo} puntos de vida' + Style.RESET_ALL)


class Spider:
    def __init__(self, nombre='Araña'):
        # definiendo la aleatoriedad
        self.nombre = nombre
        self.vida = random.randint(10, 50)
        self.daño = random.randint(10, 15)
        self.saqueo = random.randint(10, 50)
        self.level = random.randint(1, 5)
        self.veneno = random.randint(1, 5)

    def atacar(self, rival):
        probabilidad = 6
        resultado = random.randint(1, 10)
        rival.vida -= self.daño
        print(Fore.RED + f'Araña te ha golpeado y ahora estas sangrando')
        if resultado >= probabilidad and rival.veneno == False:
            rival.veneno = True
            print(Fore.RED + 'Y tambien te han envenenado')

    def atracar(self, rival):
        robo = random.randint(1, 10)
        if self.saqueo > rival.suerte:
            rival.habilidades -= robo
            print(Fore.RED + f'Araña te ha atrabado y te quito {robo} puntos de magia' + Style.RESET_ALL)
        else:
            print(f'Araña fallo su disparo de telaraña hacia {rival.Nombre}')

    def burla(self, rival):
        robo = random.randint(1, 6)
        rival.critico -= robo
        self.vida += robo
        print(Fore.RED + 'Araña te baila sabroso y pierdes vida por humillacion')


enemigoslv1 = [Duende(), Spider()]


def enemigorandom(libreria):
    rival = random.choice(libreria)
    return rival


def combate(rival, player):
    activo = True
    while activo:
        print(f'\n{player.Nombre} - Vida: {player.vida}, Magia: {player.habilidades}, Crítico: {player.critico}%')
        print(f'{rival.nombre} - Vida: {rival.vida}\n')

        print('1. Atacar')
        print('2. Curar')
        print('3. Cargar')
        print('4. Escapar')
        respuesta = input('¿Qué harás?: ').lower()

        if respuesta == '1' or respuesta == 'atacar':
            print('Seleccione un ataque:')
            print('1. Golpe ')
            print('2. CorteIgneo ')
            ataque = input('Selecciona un ataque: ').lower()
            if ataque == '1' or ataque == 'golpe':
                player.golpe(rival)
            elif ataque == '2' or ataque == 'corteigneo':
                player.corteflama(rival)
        elif respuesta == '2' or respuesta == 'curar':
            player.curar()
        elif respuesta == '3' or respuesta == 'cargar':
            player.cargar()
        elif respuesta == '4' or respuesta == 'escapar':
            player.escape(rival)
            break
        else:
            print('Escoge una opción válida.')

        if rival.vida > 0:
            opciones = ['atacar', 'atracar', 'burla']
            accion = random.choice(opciones)
            if accion == 'atacar':
                rival.atacar(player)
            elif accion == 'atracar':
                rival.atracar(player)
            elif accion == 'burla':
                rival.burla(player)
        else:
            print(Fore.GREEN + f'¡Has derrotado al {rival.nombre}!' + Style.RESET_ALL)
            break

        if player.vida <= 0:
            print(Fore.RED + f'{player.Nombre} ha caído en combate. Fin del juego.' + Style.RESET_ALL)
            activo = False


def jugar():
    player = Player()
    print(Fore.YELLOW + 'Bienvenido Aventurero, veo que vienes de muy lejos')
    player.Nombre = input('Como te llamas? ')
    print(f'Un gusto conocerte {player.Nombre}')
    time.sleep(2)
    print('Ya que veo que eres un forastero, deja te presento el lugar \n')
    time.sleep(2)
    print('Estamos en NOSEMEOCURRIOUNNOMBRELANDIA.... Una tierra magica \n')
    time.sleep(2)
    print('Lo se, muy original verdad, pero resumidamente este es un reino magico \n')
    time.sleep(2)
    print('Ahora dejame enseñarte como pelear' + Style.RESET_ALL)
    combate(enemigorandom(enemigoslv1), player)
    print('Wow, has logrado vencer a tu oponente, increible \n')
    time.sleep(2)
    print('por lo que veo tienes un toque magico')


jugar()