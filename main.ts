led.plotBrightness(1, 1, 75)
let a = [4, 0]
let b = [0, 4]
led.plot(a[0], a[1])
led.plot(b[0], b[1])
function zmena_velikosti() {
    
    led.plot(0, 0)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    zmena_velikosti()
})
