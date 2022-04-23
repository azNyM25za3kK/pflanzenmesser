let Messwert = 0
basic.forever(function () {
    Messwert = pins.analogReadPin(AnalogPin.C16)
    if (Messwert >= 500) {
        basic.showIcon(IconNames.Happy)
        basic.setLedColor(0x00ff00)
    } else if (300 < Messwert && Messwert < 500) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            `)
        basic.setLedColor(0xffff00)
    } else {
        if (300 >= Messwert) {
            basic.showIcon(IconNames.Sad)
            basic.setLedColor(0xff0000)
        }
    }
})
