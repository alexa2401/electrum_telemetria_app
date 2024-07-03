import PySimpleGUI as psg

screen_width, screen_height = psg.Window.get_screen_size() #Obtener el tamaño de la pantalla actual

#Columnas dentro del mod_medio
col1_mod_medio = psg.Column([[psg.Canvas(background_color="#2C73B9", size=(screen_width/3, screen_height/3))]])
col2_mod_medio = psg.Column([[psg.Canvas(background_color="#1B5590", size=(screen_width/3, screen_height/3))]])
col3_mod_medio = psg.Column([[psg.Canvas(background_color="#0B3A69", size=(screen_width/3, screen_height/3))]])

#Filas dentro de la ventana
mod_superior = [psg.Canvas(background_color="red", size=(screen_width, screen_height/3))]
mod_medio = [col1_mod_medio, col2_mod_medio, col3_mod_medio]
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