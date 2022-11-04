Fails = 0

def on_pin_pressed_p0():
    global Fails
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.pause(100)
    Fails += 1
    basic.show_number(Fails)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global Fails
    basic.show_string("Start")
    basic.pause(1000)
    Fails = 0
    basic.show_number(Fails)
    music.start_melody(music.built_in_melody(Melodies.PRELUDE),
        MelodyOptions.ONCE_IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global Fails
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(131, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        # . . . #
                # . . . #
                # # # # #
                # . . . #
                # . . . #
    """)
    basic.show_leds("""
        . # # # .
                . # . . .
                . # # # .
                . # . . .
                . # # # .
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                . . . . .
                . . # . .
    """)
    Fails += -1
    basic.show_number(Fails)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    basic.show_string("Ooo, cool music!")
    music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.FOREVER)
    music.stop_melody(MelodyStopOptions.ALL)
    basic.show_number(Fails)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.EIGTH_NOTE)
    music.play_melody("C5 E A E B G F G ", 120)
    music.play_melody("C5 E A E B G F G ", 120)
    music.play_melody("C5 B A G A B C5 B ", 120)
    music.play_melody("D E G F G B G E ", 120)
    basic.pause(1000)
    basic.show_number(Fails)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    for index in range(4):
        basic.show_icon(IconNames.SQUARE)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    basic.show_icon(IconNames.SCISSORS)
    basic.show_number(Fails)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_logo_pressed():
    global Fails
    if Fails == 0:
        basic.show_string("You Won!")
        music.play_melody("C F G D F G D C5 ", 120)
        music.play_melody("A C5 B G A C5 B G ", 120)
        music.play_melody("C5 B C5 F G E F A ", 120)
        music.play_melody("C5 - A - B - G - ", 120)
        music.play_melody("A F A E F G F C5 ", 120)
        music.play_melody("F G F G A D E F ", 120)
        music.play_melody("F G A C5 A F E F ", 120)
        music.play_melody("C5 B C5 - - - - - ", 120)
    else:
        if Fails >= 3:
            basic.show_string("You lost! Try again!")
            for index2 in range(10):
                music.play_melody("C5 B A F E C F E ", 120)
            basic.show_leds("""
                # # . . .
                                # # . . #
                                . . . . #
                                # # . . #
                                # # . . .
            """)
            basic.show_leds("""
                . # # # .
                                # . . # #
                                # . . . #
                                # . . # #
                                . # # # .
            """)
            Fails = 0
            basic.show_number(Fails)
        else:
            if Fails == 1:
                basic.show_string("So Close!")
                music.play_melody("F G E E F D E C ", 120)
                music.play_melody("D F F E F G F E ", 120)
                music.play_melody("D F F E F G F E ", 120)
            else:
                if Fails == 2:
                    basic.show_string("So Close!")
                    music.play_melody("F G E E F D E C ", 120)
                    music.play_melody("D F F E F G F E ", 120)
                    music.play_melody("D F F E F G F E ", 120)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
