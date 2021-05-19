input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
    radio.setGroup(10)
    basic.pause(100)
    for (let index = 0; index < 5; index++) {
        radio.sendString("nx7")
    }
})
radio.onReceivedString(function (nx7) {
    radio.setGroup(10)
    basic.showIcon(IconNames.Yes)
})
basic.forever(function () {
    radio.setGroup(10)
})
