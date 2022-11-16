from pynput import keyboard, mouse
from PIL import ImageGrab 

print("-------Color picker on the Screen-----")
def getHex(rgb):
    return '%02X%02X%02X'%rgb

def getColor(x,y):
    bbox = (x,y,x+1,y+1)
    im = ImageGrab.grab(bbox=bbox)
    r,g,b = im.getpixel((0,0))
    print(f'Color: rgb{(r,g,b)} | Hex: #{getHex((r,g,b))}')

def onClick(x,y,button,pressed):
    if pressed and button == mouse.Button.left:
        getColor(x,y)


def onRel(key):
    if key == keyboard.Key.esc:
        mouseListener.stop()
        return False

if __name__ == '__main__':
    with keyboard.Listener(on_release = onRel) as keyboardListener:
        with mouse.Listener(on_click = onClick) as mouseListener:
            keyboardListener.join()
            mouseListener.join()