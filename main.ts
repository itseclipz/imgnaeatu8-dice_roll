input.onGesture(Gesture.Shake, function () {
    Dice_Roll_Results = randint(1, 6)
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    if (Dice_Roll_Results == 1) {
        basic.clearScreen()
        led.plot(2, 2)
    } else if (Dice_Roll_Results == 2) {
        basic.clearScreen()
        led.plot(1, 3)
        led.plot(3, 1)
    } else if (Dice_Roll_Results == 3) {
        basic.clearScreen()
        led.plot(3, 1)
        led.plot(2, 2)
        led.plot(1, 3)
    } else if (Dice_Roll_Results == 4) {
        basic.clearScreen()
        led.plot(1, 1)
        led.plot(3, 1)
        led.plot(1, 3)
        led.plot(3, 3)
    } else if (Dice_Roll_Results == 5) {
        basic.clearScreen()
        led.plot(2, 2)
        led.plot(1, 1)
        led.plot(3, 1)
        led.plot(1, 3)
        led.plot(3, 3)
    } else {
        basic.clearScreen()
        led.plot(1, 0)
        led.plot(1, 0)
        led.plot(1, 0)
        led.plot(3, 0)
        led.plot(3, 0)
        led.plot(3, 0)
    }
})
let Dice_Roll_Results = 0
music.setVolume(255)
basic.clearScreen()
basic.forever(function () {
	
})
