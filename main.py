def on_gesture_shake():
    global Dice_Roll_Results
    Dice_Roll_Results = randint(1, 6)
    music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    if Dice_Roll_Results == 1:
        basic.clear_screen()
        led.plot(2, 2)
    elif Dice_Roll_Results == 2:
        basic.clear_screen()
        led.plot(2, 2)
        led.plot(1, 3)
        led.plot(3, 1)
    elif Dice_Roll_Results == 3:
        basic.clear_screen()
        led.plot(3, 1)
        led.plot(2, 2)
        led.plot(1, 3)
    elif Dice_Roll_Results == 4:
        basic.clear_screen()
        led.plot(1, 1)
        led.plot(3, 1)
        led.plot(1, 3)
        led.plot(3, 3)
    elif Dice_Roll_Results == 5:
        basic.clear_screen()
        led.plot(2, 2)
        led.plot(1, 1)
        led.plot(3, 1)
        led.plot(1, 3)
        led.plot(3, 3)
    else:
        led.plot(1, 0)
        led.plot(1, 0)
        led.plot(1, 0)
        led.plot(3, 0)
        led.plot(3, 0)
        led.plot(3, 0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Dice_Roll_Results = 0
music.set_volume(255)
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
