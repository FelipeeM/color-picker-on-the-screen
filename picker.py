import PySimpleGUI as sg
from pynput import keyboard, mouse
from PIL import ImageGrab 

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
font = ("Arial", 15)
layout = [  [sg.Text(' Color Picker ',size=(31),justification="center",font=font,key='_Title_')],
            [sg.Text('RGB',size=(6)), sg.Input(readonly=True,size=(25),text_color='black',key='_RGB_')],
            [sg.Text('HEX',size=(6)), sg.Input(readonly=True,size=(25),text_color='black',key='_HEX_')],
            [sg.Text(background_color='#2C2825',size=(30),key='_BoxColor_')],
            [sg.Button('Picker Color'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Picker Color', layout,size=(280, 150))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Picker Color':
        window['_Title_'].update('Select the Color')

        def getHex(rgb):
            return '%02X%02X%02X'%rgb

        def getColor(x,y):
            bbox = (x,y,x+1,y+1)
            im = ImageGrab.grab(bbox=bbox)
            r,g,b = im.getpixel((0,0))
            hexColor = getHex((r,g,b))
            window['_RGB_'].update(f'rgb{(r,g,b)}')
            window['_HEX_'].update(f'#{hexColor}')
            window['_BoxColor_'].update(background_color=f'#{hexColor}')
            window['_Title_'].update('Color Selected')
            onRel('close')
            

        def onClick(x,y,button,pressed):
            if pressed and button == mouse.Button.left:
                getColor(x,y)


        def onRel(key):
            if key == keyboard.Key.esc or key == 'close':
                mouseListener.stop()
                keyboardListener.stop()
                return False
                
        keyboardListener = keyboard.Listener(on_release = onRel)
        mouseListener = mouse.Listener(on_click = onClick)
        keyboardListener.start()
        mouseListener.start()
       
       
    print('You entered ', values)

window.close()