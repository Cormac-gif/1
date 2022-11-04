let Fails = 0
input.onPinPressed(TouchPin.P0, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . . 
        . # . # .
        # . . . #
        `)
    basic.pause(100)
    Fails += 1
    basic.showNumber(Fails)
})
input.onButtonPressed(Button.A, function () {
    basic.showString("Start")
    basic.pause(1000)
    Fails = 0
    basic.showNumber(Fails)
    music.startMelody(music.builtInMelody(Melodies.Prelude), MelodyOptions.OnceInBackground)
})
input.onPinPressed(TouchPin.P2, function () {
    music.playTone(988, music.beat(BeatFraction.Whole))
    music.playTone(349, music.beat(BeatFraction.Whole))
    music.playTone(131, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        `)
    basic.showLeds(`
        . # # # .
        . # . . .
        . # # # .
        . # . . .
        . # # # .
        `)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        `)
    Fails += -1
    basic.showNumber(Fails)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Ooo, cool music!")
    music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.Forever)
    music.stopMelody(MelodyStopOptions.All)
    basic.showNumber(Fails)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.EigthNote)
    music.playMelody("C5 E A E B G F G ", 120)
    music.playMelody("C5 E A E B G F G ", 120)
    music.playMelody("C5 B A G A B C5 B ", 120)
    music.playMelody("D E G F G B G E ", 120)
    basic.pause(1000)
    basic.showNumber(Fails)
})
input.onPinPressed(TouchPin.P1, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Square)
        basic.showIcon(IconNames.SmallSquare)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
    basic.showIcon(IconNames.Scissors)
    basic.showNumber(Fails)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (Fails == 0) {
        basic.showString("You Won!")
        music.playMelody("C F G D F G D C5 ", 120)
        music.playMelody("A C5 B G A C5 B G ", 120)
        music.playMelody("C5 B C5 F G E F A ", 120)
        music.playMelody("C5 - A - B - G - ", 120)
        music.playMelody("A F A E F G F C5 ", 120)
        music.playMelody("F G F G A D E F ", 120)
        music.playMelody("F G A C5 A F E F ", 120)
        music.playMelody("C5 B C5 - - - - - ", 120)
    } else if (Fails >= 3) {
        basic.showString("You lost! Try again!")
        for (let index = 0; index < 10; index++) {
            music.playMelody("C5 B A F E C F E ", 120)
        }
        basic.showLeds(`
            # # . . .
            # # . . #
            . . . . #
            # # . . #
            # # . . .
            `)
        basic.showLeds(`
            . # # # .
            # . . # #
            # . . . #
            # . . # #
            . # # # .
            `)
        Fails = 0
        basic.showNumber(Fails)
    } else if (Fails == 1) {
        basic.showString("So Close!")
        music.playMelody("F G E E F D E C ", 120)
        music.playMelody("D F F E F G F E ", 120)
        music.playMelody("D F F E F G F E ", 120)
    } else if (Fails == 2) {
        basic.showString("So Close!")
        music.playMelody("F G E E F D E C ", 120)
        music.playMelody("D F F E F G F E ", 120)
        music.playMelody("D F F E F G F E ", 120)
    }
})
