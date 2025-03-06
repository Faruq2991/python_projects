import pyscreenshot as ImageGrab

def screenshot():
    image = ImageGrab.grab()
    image.save("test.png")

screenshot()
