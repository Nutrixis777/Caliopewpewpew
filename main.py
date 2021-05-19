def on_received_string(nutrixis777):
    for index in range(1):
        basic.show_leds("""
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            . . . . .
            """)
radio.on_received_string(on_received_string)

def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
    radio.set_group(10)
    radio.send_string("nutrixis777")
input.on_button_pressed(Button.A, on_button_pressed_a)
