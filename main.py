Messwert = 0

def on_forever():
    global Messwert
    Messwert = pins.analog_read_pin(AnalogPin.C16)
    if Messwert >= 500:
        basic.show_icon(IconNames.HAPPY)
        basic.set_led_color(0x00ff00)
    elif 300 < Messwert and Messwert < 500:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            """)
        basic.set_led_color(0xffff00)
    else:
        if 300 >= Messwert:
            basic.show_icon(IconNames.SAD)
            basic.set_led_color(0xff0000)
basic.forever(on_forever)
