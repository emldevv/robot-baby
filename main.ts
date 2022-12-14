let baby = 0
let nappy = 0
let crying = 0
//  This block determines states of baby.
input.onGesture(Gesture.EightG, function on_gesture_eight_g() {
    
    basic.showIcon(IconNames.Skull)
    music.stopMelody(MelodyStopOptions.All)
    music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
    basic.showString("DONT SHAKE BABY!")
    for (let index = 0; index < randint(5, 10); index++) {
        images.iconImage(IconNames.Skull).scrollImage(1, 200)
        images.createImage(`
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        `).scrollImage(1, 200)
    }
    baby = 0
})
input.onGesture(Gesture.FreeFall, function on_gesture_free_fall() {
    
    music.stopMelody(MelodyStopOptions.All)
    while (input.isGesture(Gesture.FreeFall)) {
        basic.showIcon(IconNames.Angry)
        music.playTone(988, music.beat(BeatFraction.Eighth))
        music.playTone(880, music.beat(BeatFraction.Eighth))
    }
    baby = 0
})
input.onGesture(Gesture.ScreenDown, function on_gesture_screen_down() {
    
    music.stopMelody(MelodyStopOptions.All)
    while (input.isGesture(Gesture.ScreenDown)) {
        basic.showIcon(IconNames.Confused)
        basic.pause(100)
        basic.showIcon(IconNames.Surprised)
        basic.pause(100)
        music.playMelody("C5 A B G A F G E ", 650)
    }
    baby = 0
})
/** 

Incident 1:

Face down


 */
/** 

Incident 2.

Dropped.


 */
//  Incident 3.
//  
//  Shake baby.
basic.forever(function on_forever() {
    
    if (baby == 0) {
        nappy = 0
        basic.showIcon(IconNames.Happy)
        music.stopMelody(MelodyStopOptions.All)
        basic.pause(randint(2000, 10000))
        baby = randint(1, 3)
    }
    
    if (baby == 1) {
        crying = 1
    }
    
    while (crying == 1) {
        basic.showIcon(IconNames.Angry)
        basic.pause(100)
        basic.showIcon(IconNames.Confused)
        music.playMelody("C5 B C5 B C5 B C5 B ", 500)
        if (input.isGesture(Gesture.LogoUp)) {
            crying = 0
            basic.showIcon(IconNames.Heart)
            basic.pause(100)
            baby = 0
        }
        
    }
    if (baby == 2) {
        crying = 2
    }
    
    while (crying == 2) {
        basic.showIcon(IconNames.Asleep)
        basic.pause(100)
        basic.showIcon(IconNames.Surprised)
        music.playMelody("C D E F E D C - ", 160)
        if (input.isGesture(Gesture.ScreenUp)) {
            basic.showIcon(IconNames.SmallHeart)
            basic.pause(100)
            basic.showIcon(IconNames.Heart)
            basic.pause(100)
            basic.showIcon(IconNames.Asleep)
            for (let index2 = 0; index2 < randint(4, 10); index2++) {
                music.playMelody("C5 - - - C C - - ", 120)
            }
            basic.showIcon(IconNames.Surprised)
            basic.pause(500)
            crying = 0
        }
        
        if (crying == 0) {
            baby = 0
        }
        
    }
    if (baby == 3) {
        crying = 3
    }
    
    while (crying == 3) {
        basic.showIcon(IconNames.Triangle)
        music.playTone(494, music.beat(BeatFraction.Eighth))
        music.playTone(466, music.beat(BeatFraction.Eighth))
        music.playTone(440, music.beat(BeatFraction.Eighth))
        music.playTone(392, music.beat(BeatFraction.Eighth))
        music.playTone(415, music.beat(BeatFraction.Eighth))
        if (nappy == 0 && input.isGesture(Gesture.TiltRight)) {
            basic.showIcon(IconNames.SmallDiamond)
            nappy = 1
        } else if (nappy == 1 && input.isGesture(Gesture.TiltLeft)) {
            basic.showIcon(IconNames.SmallSquare)
            nappy = 2
        } else if (nappy == 2 && input.isGesture(Gesture.LogoUp)) {
            basic.showIcon(IconNames.Diamond)
            nappy = 3
        } else if (nappy == 3 && input.isGesture(Gesture.LogoUp)) {
            basic.showIcon(IconNames.SmallHeart)
            basic.pause(200)
            crying = 0
        } else {
            crying = 3
        }
        
        if (crying == 0) {
            basic.showIcon(IconNames.Heart)
            basic.pause(1000)
            baby = 0
        }
        
    }
})
