def on_gesture_shake():
    global random_number
    basic.clear_screen()
    random_number = randint(0, 4)
    if random_number == 6:
        basic.show_string("DEFINATELY ")
    elif random_number == 5:
        basic.show_string("TRY AGAIN ")
    elif random_number == 4:
        basic.show_string("YES")
    elif random_number == 3:
        basic.show_string("NO")
    elif random_number == 2:
        basic.show_string("MAYBE")
    elif random_number == 1:
        basic.show_string("100%")
    elif random_number == 0:
        basic.show_string("HECK YEAH")
    else:
        basic.show_string("I DONT KNOW")
    basic.show_number(8)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

random_number = 0
basic.show_string("ASK A QUESTION")
basic.show_number(8)

def on_forever():
    pass
basic.forever(on_forever)
