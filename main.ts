input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    random_number = randint(0, 4)
    if (random_number == 6) {
        basic.showString("DEFINATELY ")
    } else if (random_number == 5) {
        basic.showString("TRY AGAIN ")
    } else if (random_number == 4) {
        basic.showString("YES")
    } else if (random_number == 3) {
        basic.showString("NO")
    } else if (random_number == 2) {
        basic.showString("MAYBE")
    } else if (random_number == 1) {
        basic.showString("100%")
    } else if (random_number == 0) {
        basic.showString("HECK YEAH")
    } else {
        basic.showString("I DONT KNOW")
    }
    basic.showNumber(8)
})
let random_number = 0
basic.showString("ASK A QUESTION")
basic.showNumber(8)
basic.forever(function () {
	
})
