#importamos
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController #controlador movimiento

#tamaño ventana
app = Ursina(borderless=False) #opcion abrir y cerrar
random.seed(0) #semilla para ramdom
window.size = (1300, 900) #tamaño ventana

# Definir el jugador
player = FirstPersonController()

# Definir el cubo
class Cubo(Entity): #entidad
    def __init__(self, position=(0, 0, 0)):#posicion por defecto 0
        super().__init__(
            position=position,
            model="cube", #modelo de cubo
            scale=(1, 1), #escala en tupla
            origin_y=-0.5, #centro de origen, -.5 es el centro
            color=color.light_gray, #color cubo
            collider="box" #colisionador
        ) 

# Aparecer arriba del cubo
player.position = Vec3(0, 2, 0) #encima del cubo
Cubo(position=(0, 1, 0)) #altura del cubo

# Cerrar con escape
def input(key):
    if key == "escape":
        quit()

#reinicio de posicion al caer con bucle
def update():
    if(player.position.y <= -30): #hace que pase el
        player.position = Vec3(0,25,0) #efecto de reinicio cae del cielo

#lista para almacenar cubos
cubos=[]

# mas cubos #ramdoms
for z in range(5):
    cubo = Cubo(position=(random.randint(1,6),1,z)) #para q se generen en lugares random
    cubo.texture = load_texture('bloque7.jpg')  # textura bloques

    cubos.append(cubo)

#color winner
cubos[-1].color=color.green

# Fondo
Sky_texture = "cielo4.jpg"
Sky(texture=Sky_texture)

# Musica
music_path = 'USM.mp3'
music = Audio(music_path, loop=True)  # loop=True para que la música se reproduzca en bucle
music.volume = 0.9# Cambiar el volumen de la música (0.0 a 1.0)

music.play() # Reproducir la música

# Ejecutar la aplicación
app.run()

