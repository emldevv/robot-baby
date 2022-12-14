baby = 0
nappy = 0
crying = 0
# This block determines states of baby.

def on_gesture_eight_g():
    global baby
    basic.show_icon(IconNames.SKULL)
    music.stop_melody(MelodyStopOptions.ALL)
    music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
    basic.show_string("DONT SHAKE BABY!")
    for index in range(randint(5, 10)):
        images.icon_image(IconNames.SKULL).scroll_image(1, 200)
        images.create_image("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """).scroll_image(1, 200)
    baby = 0
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_gesture_free_fall():
    global baby
    music.stop_melody(MelodyStopOptions.ALL)
    while input.is_gesture(Gesture.FREE_FALL):
        basic.show_icon(IconNames.ANGRY)
        music.play_tone(988, music.beat(BeatFraction.EIGHTH))
        music.play_tone(880, music.beat(BeatFraction.EIGHTH))
    baby = 0
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_gesture_screen_down():
    global baby
    music.stop_melody(MelodyStopOptions.ALL)
    while input.is_gesture(Gesture.SCREEN_DOWN):
        basic.show_icon(IconNames.CONFUSED)
        basic.pause(100)
        basic.show_icon(IconNames.SURPRISED)
        basic.pause(100)
        music.play_melody("C5 A B G A F G E ", 650)
    baby = 0
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

"""

Incident 1:

Face down

"""
"""

Incident 2.

Dropped.

"""
# Incident 3.
# 
# Shake baby.

def on_forever():
    global nappy, baby, crying
    if baby == 0:
        nappy = 0
        basic.show_icon(IconNames.HAPPY)
        music.stop_melody(MelodyStopOptions.ALL)
        basic.pause(randint(2000, 10000))
        baby = randint(1, 3)
    if baby == 1:
        crying = 1
    while crying == 1:
        basic.show_icon(IconNames.ANGRY)
        basic.pause(100)
        basic.show_icon(IconNames.CONFUSED)
        music.play_melody("C5 B C5 B C5 B C5 B ", 500)
        if input.is_gesture(Gesture.LOGO_UP):
            crying = 0
            basic.show_icon(IconNames.HEART)
            basic.pause(100)
            baby = 0
    if baby == 2:
        crying = 2
    while crying == 2:
        basic.show_icon(IconNames.ASLEEP)
        basic.pause(100)
        basic.show_icon(IconNames.SURPRISED)
        music.play_melody("C D E F E D C - ", 160)
        if input.is_gesture(Gesture.SCREEN_UP):
            basic.show_icon(IconNames.SMALL_HEART)
            basic.pause(100)
            basic.show_icon(IconNames.HEART)
            basic.pause(100)
            basic.show_icon(IconNames.ASLEEP)
            for index2 in range(randint(4, 10)):
                music.play_melody("C5 - - - C C - - ", 120)
            basic.show_icon(IconNames.SURPRISED)
            basic.pause(500)
            crying = 0
        if crying == 0:
            baby = 0
    if baby == 3:
        crying = 3
    while crying == 3:
        basic.show_icon(IconNames.TRIANGLE)
        music.play_tone(494, music.beat(BeatFraction.EIGHTH))
        music.play_tone(466, music.beat(BeatFraction.EIGHTH))
        music.play_tone(440, music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.EIGHTH))
        music.play_tone(415, music.beat(BeatFraction.EIGHTH))
        if nappy == 0 and input.is_gesture(Gesture.TILT_RIGHT):
            basic.show_icon(IconNames.SMALL_DIAMOND)
            nappy = 1
        elif nappy == 1 and input.is_gesture(Gesture.TILT_LEFT):
            basic.show_icon(IconNames.SMALL_SQUARE)
            nappy = 2
        elif nappy == 2 and input.is_gesture(Gesture.LOGO_UP):
            basic.show_icon(IconNames.DIAMOND)
            nappy = 3
        elif nappy == 3 and input.is_gesture(Gesture.LOGO_UP):
            basic.show_icon(IconNames.SMALL_HEART)
            basic.pause(200)
            crying = 0
        else:
            crying = 3
        if crying == 0:
            basic.show_icon(IconNames.HEART)
            basic.pause(1000)
            baby = 0
basic.forever(on_forever)
