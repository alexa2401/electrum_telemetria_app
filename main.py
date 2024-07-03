import PySimpleGUI as psg

psg.set_options(element_padding=(0,0), margins=(0,0), background_color="#353535")

screen_width, screen_height = psg.Window.get_screen_size() #Obtener el tamaño de la pantalla actual

# Layout de las imágenes para cada columna
col1_mod_medio_layout = [
    #[psg.Image(source="imgs/dog.png", size=(screen_width/3, screen_height/3))]
]
col2_mod_medio_layout = [
    #[psg.Image(source="imgs/cat.png", size=(screen_width/3, screen_height/3))]
]
col3_mod_medio_layout = [
    #[psg.Image(source="imgs/hamster.png", size=(screen_width/3, screen_height/3))]
]

# Definición de las columnas utilizando sg.Column
col1_mod_medio_column = psg.Column(col1_mod_medio_layout, size=(screen_width/3, (screen_height/6)*4))
col2_mod_medio_column = psg.Column(col2_mod_medio_layout, size=(screen_width/3, (screen_height/6)*4))
col3_mod_medio_column = psg.Column(col3_mod_medio_layout, size=(screen_width/3, (screen_height/6)*4))

# Definición de los frames para cada columna
col1_mod_medio_frame = psg.Frame('', [[col1_mod_medio_column]], size=(screen_width/3, (screen_height/6)*4))
col2_mod_medio_frame = psg.Frame('', [[col2_mod_medio_column]], size=(screen_width/3, (screen_height/6)*4))
col3_mod_medio_frame = psg.Frame('', [[col3_mod_medio_column]], size=(screen_width/3, (screen_height/6)*4))

# Definición de los layouts de los módulos
mod_superior_layout = []
mod_medio_layout = [
    [col1_mod_medio_frame, col2_mod_medio_frame, col3_mod_medio_frame]
]
mod_inferior_layout = []

# Definición de los frames de los módulos
mod_superior_frame = psg.Frame('', mod_superior_layout, size=(screen_width, screen_height/6))
mod_medio_frame = psg.Frame('', mod_medio_layout, size=(screen_width, (screen_height/6)*4))
mod_inferior_frame = psg.Frame('', mod_inferior_layout, size=(screen_width, screen_height/6))

# Definición del layout principal
master_layout = [
    [mod_superior_frame],
    [mod_medio_frame],
    [mod_inferior_frame]
]

# Definición del layout de la ventana
layout = [
    [psg.Frame('', master_layout, background_color=None ,expand_x=True, expand_y=True)]
]

window = psg.Window("Electrum", layout, size=(screen_width, screen_height), resizable=True) #Creacion de la ventana

while True:
    event,values = window.read()
    print(event,values)
    if event in (None, 'Exit'):
        break
window.close()