led.plot_brightness(1, 1, 75)
a = [4, 0]
b = [0, 4]

led.plot(a[0], a[1])
led.plot(b[0], b[1])

def zmena_velikosti():
    global a, b
    led.plot(0, 0)
    



def on_button_pressed_a():
    zmena_velikosti()
input.on_button_pressed(Button.A, on_button_pressed_a)
