import PySimpleGUI as psg

screen_width, screen_height = psg.Window.get_screen_size() #Obtener el tamaño de la pantalla actual

mod_superior = [psg.Canvas(background_color="red", size=(screen_width, screen_height/3))]
mod_medio = [psg.Canvas(background_color="blue", size=(screen_width, screen_height/3))]
mod_inferior = [psg.Canvas(background_color="green", size=(screen_width, screen_height/3))]

layout = [                                                  #Creacion y definido del layout
    mod_superior,
    mod_medio,
    mod_inferior
]

window = psg.Window("Electrum", layout, size=(screen_width, screen_height), resizable=True) #Creacion de la ventana

while True:
    event,values = window.read()
    print(event,values)
    if event in (None, 'Exit'):
        break

window.close()